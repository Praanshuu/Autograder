from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        unread_only = self.request.query_params.get('unread_only', 'false')
        
        queryset = Notification.objects.filter(user=user)
        
        if unread_only.lower() == 'true':
            queryset = queryset.filter(is_read=False)
        
        return queryset[:50]  # Limit to 50 most recent
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['put', 'patch'])
    def mark_read(self, request, pk=None):
        """Mark notification as read"""
        notification = self.get_object()
        
        if notification.user != request.user:
            return Response(
                {'message': 'Not authorized'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        notification.is_read = True
        notification.save()
        
        return Response({
            'success': True,
            'data': NotificationSerializer(notification).data
        })
    
    @action(detail=False, methods=['put'])
    def mark_all_read(self, request):
        """Mark all notifications as read"""
        Notification.objects.filter(
            user=request.user,
            is_read=False
        ).update(is_read=True)
        
        return Response({
            'success': True,
            'message': 'All notifications marked as read'
        })
