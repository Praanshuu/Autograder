import requests
import time
import concurrent.futures
import sys
import random
import os
import django

# Setup Django to fetch users
sys.path.append('/home/anshul/Projects/Autograder/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autograder.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()

BASE_URL = "http://localhost:8000/api"

def get_token(username, password):
    try:
        resp = requests.post(f"{BASE_URL}/auth/simple-login/", json={'username': username, 'password': password})
        if resp.status_code == 200:
            return resp.json()['tokens']['access']
        else:
            print(f"Login failed for {username}: {resp.status_code} {resp.text}")
    except Exception as e:
        print(f"Login exception for {username}: {e}")
        pass
    return None

def get_target_question(token):
    headers = {'Authorization': f'Bearer {token}'}
    # 1. Get Classes
    resp = requests.get(f"{BASE_URL}/classes/", headers=headers)
    if resp.status_code != 200 or not resp.json():
        print(f"No classes found. Resp: {resp.status_code} {resp.text}")
        return None, None
    
    # Debug: print classes
    data = resp.json()
    print(f"Classes response type: {type(data)}")
    
    if isinstance(data, dict) and 'results' in data:
        classes = data['results']
    else:
        classes = data
        
    print(f"Classes found: {len(classes)}")
    
    if not classes:
         print("No classes in list.")
         return None, None
         
    class_id = classes[0]['id']
    
    # 2. Get Assignments
    resp = requests.get(f"{BASE_URL}/assignments/?class_id={class_id}", headers=headers)
    if resp.status_code != 200:
        print(f"Failed to get assignments. Resp: {resp.status_code}")
        return None, None

    data = resp.json()
    if isinstance(data, dict) and 'results' in data:
        assignments = data['results']
    else:
        assignments = data

    if not assignments:
        print(f"No assignments found for class {class_id}.")
        return None, None
        
    # Find an assignment with questions
    for assign in assignments:
        # 3. Get Questions (Detail View)
        q_resp = requests.get(f"{BASE_URL}/assignments/{assign['id']}/", headers=headers)
        if q_resp.status_code == 200:
            data = q_resp.json()
            if data.get('questions') and len(data['questions']) > 0:
                aq = data['questions'][0]
                return assign['id'], aq['id'] # Returning assignment_id, assignment_question_id
                    
    return None, None

def submit_job(user_idx, token, assign_id, aq_id):
    headers = {'Authorization': f'Bearer {token}'}
    
    code = f"""
def solution():
    print("User {user_idx} executing")
    return [1, 2, 3]
"""
    payload = {
        'code': code,
        'language': 'python',
        'assignment_id': assign_id,
        'assignment_question_id': aq_id
    }
    
    start_time = time.time()
    
    # 1. Submit (Async trigger)
    try:
        # Note: Using the 'run' endpoint which is typically for "Run Code" button
        # If we want "Submit", we use the submit endpoint.
        # But 'run_code' in views.py is what we updated to be async in one of the steps?
        # Wait, let's check views.py.
        # I updated `create` (POST /submissions/) AND `run_code`?
        # I updated `create` (SubmissionAttemptViewSet.create).
        # run_code is `@action(detail=False, methods=['post'], url_path='run')`
        # I need to check if I updated `run_code` too.
        # I replaced a large chunk. I should check if I updated run_code.
        # If I only updated `create`, then I should use `POST /submissions/`.
        
        # Let's use `POST /submissions/attempts/` (Submit)
        # But `POST /submissions/attempts/` requires `assignment_question` ID.
        
        submit_payload = {
            'assignment_question_id': aq_id,
            'code_content': code,
            'language': 'python',
            'status': 'submitted' # Initial status?
        }
        
        resp = requests.post(f"{BASE_URL}/submissions/attempts/", json=submit_payload, headers=headers)
        
        if resp.status_code != 201:
            return {'status': 'error', 'error': f"Submit failed: {resp.status_code} {resp.text}"}
            
        data = resp.json()
        attempt_id = data['id']
        initial_status = data['status']
        
        if initial_status not in ['queued', 'processing']:
             return {'status': 'error', 'error': f"Not Async! Status: {initial_status}"}
             
        # 2. Poll
        poll_attempts = 0
        while poll_attempts < 30: # 60s timeout
            time.sleep(2)
            poll_resp = requests.get(f"{BASE_URL}/submissions/attempts/{attempt_id}/", headers=headers)
            if poll_resp.status_code == 200:
                p_data = poll_resp.json()
                curr_status = p_data['status']
                if curr_status in ['success', 'fail', 'error']:
                    total_time = time.time() - start_time
                    return {'status': 'success', 'final_status': curr_status, 'time': total_time}
            poll_attempts += 1
            
        return {'status': 'timeout', 'time': time.time() - start_time}
        
    except Exception as e:
        return {'status': 'error', 'error': str(e)}

def main():
    print("🚀 Starting Scalability Load Test (Async Mode)")
    
    # 1. Setup Validation
    # Get Admin/Teacher to find assignment
    admin_token = get_token('Vaishnavi', 'Rinvu2-ganqyh-rowbyx') # Found in populate_real_data.py 
    # populate_real_data said: teacher.set_password("Rinvu2-ganqyh-rowbyx")
    # I should use that password.
    if not admin_token:
        # Try generic student
        admin_token = get_token('B25CS001', 'B25CS001')
        
    if not admin_token:
        print("❌ Could not login to get assignment data.")
        return

    assign_id, aq_id = get_target_question(admin_token)
    if not aq_id:
        print("❌ Could not find a valid assignment question.")
        return
        
    print(f"✅ Target Found: Assignment {assign_id}, Question {aq_id}")
    
    # 2. Login Concurrent Users
    print(f"🔑 Fetching users from DB...")
    user_list = list(User.objects.filter(role='student').values_list('username', flat=True))
    
    if not user_list:
        print("❌ No student users found.")
        return

    print(f"Found {len(user_list)} students. Logging them in...")
    users = []
    
    # Login sequentially (or parallelize if needed, but sequential is safer for token generation)
    for i, username in enumerate(user_list):
        # Password assumed to be same as username
        token = get_token(username, username)
        if token:
            users.append({'id': i+1, 'username': username, 'token': token})
        
        if (i+1) % 50 == 0:
            print(f"  Logged in {i+1} users...")
            
    print(f"✅ Logged in {len(users)} users.")
    if len(users) == 0: return

    # 3. Execute Async Load
    print(f"\n🔥 Launching {len(users)} concurrent submissions...")
    start_time_global = time.time()
    
    # Cap workers at 50 to avoid client-side resource exhaustion, but process all users
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(submit_job, u['id'], u['token'], assign_id, aq_id): u for u in users}
        
        completed = 0
        success = 0
        
        for future in concurrent.futures.as_completed(futures):
            user = futures[future]
            try:
                res = future.result()
                completed += 1
                if res['status'] == 'success':
                    success += 1
                    print(f"  [User {user['id']}] ✅ {res['final_status']} in {res['time']:.2f}s")
                else:
                    print(f"  [User {user['id']}] ❌ {res['status']} - {res.get('error', '')}")
            except Exception as exc:
                print(f"  [User {user['id']}] 💥 Exception: {exc}")

    total_duration = time.time() - start_time_global
    print("\n" + "="*40)
    print(f"📊 Load Test Results")
    print(f"   Total Requests: {len(users)}")
    print(f"   Successful:     {success}")
    print(f"   Failed:         {len(users) - success}")
    print(f"   Total Time:     {total_duration:.2f}s")
    print(f"   Throughput:     {len(users)/total_duration:.2f} req/s")
    print("="*40)

if __name__ == "__main__":
    main()
