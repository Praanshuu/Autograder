from django.contrib.auth import get_user_model
User = get_user_model()
print("--- Recent Users ---")
for u in User.objects.order_by('-date_joined')[:5]:
    print(f"User: {u.username}, Email: {u.email}, Role: {u.role}, Active: {u.is_active}")
