from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer, UserRegistrationSerializer, UserSettingsSerializer


# Simple function-based view for testing
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    """Get current user - simple function-based view"""
    serializer = UserSerializer(request.user)
    return Response({'success': True, 'user': serializer.data})


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def simple_login(request):
    """Simple login function-based view"""
    print(f"=== SIMPLE LOGIN CALLED ===")
    print(f"Method: {request.method}")
    print(f"Headers: {dict(request.headers)}")
    print(f"Content-Type: {request.content_type}")
    print(f"Raw body: {request.body}")
    print(f"Request data: {request.data}")
    
    if request.method == 'GET':
        return Response({'message': 'Simple login endpoint is working'})
    
    username = request.data.get('username')
    password = request.data.get('password')
    
    print(f"Extracted - Username: '{username}', Password: '{password}'")
    
    if not username or not password:
        print("Missing username or password")
        return Response(
            {'success': False, 'message': 'Username and password are required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Let's also check if the user exists
    try:
        from .models import User
        user_exists = User.objects.filter(username=username).first()
        print(f"User exists in database: {user_exists}")
        if user_exists:
            print(f"User active: {user_exists.is_active}")
            print(f"User role: {user_exists.role}")
    except Exception as e:
        print(f"Error checking user: {e}")
    
    user = authenticate(username=username, password=password)
    print(f"Authentication result: {user}")
    
    if user and user.is_active:
        print(f"User authenticated successfully: {user.username}")
        refresh = RefreshToken.for_user(user)
        return Response({
            'success': True,
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        })
    
    print(f"Login failed for username: '{username}'")
    return Response(
        {'success': False, 'message': 'Invalid credentials'},
        status=status.HTTP_401_UNAUTHORIZED
    )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action == 'create' or self.action == 'register' or self.action == 'login':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        """User registration"""
        print(f"=== REGISTRATION ATTEMPT ===")
        print(f"Request data: {request.data}")
        
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'success': True,
                'user': UserSerializer(user).data,
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }, status=status.HTTP_201_CREATED)
        
        print(f"Validation errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        """User login"""
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response(
                {'message': 'Username and password are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            return Response({
                'success': True,
                'user': UserSerializer(user).data,
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            })
        return Response(
            {'message': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Get current user"""
        serializer = self.get_serializer(request.user)
        return Response({'success': True, 'user': serializer.data})
    
    @action(detail=False, methods=['put', 'patch'], permission_classes=[IsAuthenticated])
    def update_me(self, request):
        """Update current user"""
        serializer = self.get_serializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'user': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['put', 'patch'], permission_classes=[IsAuthenticated], url_path='settings')
    def user_settings(self, request):
        """Update user settings"""
        serializer = UserSettingsSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'user': UserSerializer(request.user).data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
