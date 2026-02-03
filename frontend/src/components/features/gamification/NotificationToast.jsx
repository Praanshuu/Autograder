/**
 * Notification Toast Component
 * 
 * Displays real-time notifications for achievements, points, and other events
 */

import React, { useState, useEffect } from 'react';
import { X, Award, Star, TrendingUp, CheckCircle, Zap } from 'lucide-react';

const NotificationToast = ({ notification, onClose, duration = 5000 }) => {
  const [isVisible, setIsVisible] = useState(false);
  const [isExiting, setIsExiting] = useState(false);

  useEffect(() => {
    // Animate in
    const showTimer = setTimeout(() => setIsVisible(true), 100);
    
    // Auto-hide after duration
    const hideTimer = setTimeout(() => {
      setIsExiting(true);
      setTimeout(() => onClose(notification.id), 300);
    }, duration);

    return () => {
      clearTimeout(showTimer);
      clearTimeout(hideTimer);
    };
  }, [notification.id, duration, onClose]);

  const handleClose = () => {
    setIsExiting(true);
    setTimeout(() => onClose(notification.id), 300);
  };

  const getNotificationConfig = () => {
    switch (notification.type) {
      case 'achievement':
        return {
          icon: Award,
          title: 'Achievement Unlocked!',
          bgColor: 'bg-gradient-to-r from-yellow-400 to-orange-500',
          textColor: 'text-white',
          iconColor: 'text-yellow-100'
        };
      
      case 'points':
        return {
          icon: Star,
          title: 'Points Earned!',
          bgColor: 'bg-gradient-to-r from-blue-500 to-purple-600',
          textColor: 'text-white',
          iconColor: 'text-blue-100'
        };
      
      case 'practice_completed':
        return {
          icon: CheckCircle,
          title: 'Practice Complete!',
          bgColor: 'bg-gradient-to-r from-green-500 to-emerald-600',
          textColor: 'text-white',
          iconColor: 'text-green-100'
        };
      
      case 'assignment_submitted':
        return {
          icon: TrendingUp,
          title: 'Assignment Submitted!',
          bgColor: 'bg-gradient-to-r from-indigo-500 to-blue-600',
          textColor: 'text-white',
          iconColor: 'text-indigo-100'
        };
      
      case 'streak_update':
        return {
          icon: Zap,
          title: 'Streak Updated!',
          bgColor: 'bg-gradient-to-r from-orange-500 to-red-500',
          textColor: 'text-white',
          iconColor: 'text-orange-100'
        };
      
      default:
        return {
          icon: Star,
          title: 'Notification',
          bgColor: 'bg-gradient-to-r from-gray-500 to-gray-600',
          textColor: 'text-white',
          iconColor: 'text-gray-100'
        };
    }
  };

  const getNotificationContent = () => {
    const { data } = notification;
    
    switch (notification.type) {
      case 'achievement':
        return {
          message: data.name,
          subtitle: data.description,
          extra: data.rarity ? `${data.rarity.charAt(0).toUpperCase() + data.rarity.slice(1)} Badge` : null
        };
      
      case 'points':
        return {
          message: `+${data.points_earned} points`,
          subtitle: `Total: ${data.new_points} points`,
          extra: data.source ? `From ${data.source}` : null
        };
      
      case 'practice_completed':
        return {
          message: data.question_title,
          subtitle: `+${data.points_earned} points`,
          extra: data.attempt_number > 1 ? `Attempt ${data.attempt_number}` : 'First try!'
        };
      
      case 'assignment_submitted':
        return {
          message: data.assignment_title,
          subtitle: `+${data.points_earned} points`,
          extra: data.score ? `Score: ${Math.round(data.score)}%` : null
        };
      
      case 'streak_update':
        return {
          message: `${data.current_streak} day streak!`,
          subtitle: `Keep up the ${data.streak_type} practice`,
          extra: null
        };
      
      default:
        return {
          message: 'New notification',
          subtitle: null,
          extra: null
        };
    }
  };

  const config = getNotificationConfig();
  const content = getNotificationContent();
  const Icon = config.icon;

  return (
    <div
      className={`
        fixed top-4 right-4 z-50 max-w-sm w-full
        transform transition-all duration-300 ease-in-out
        ${isVisible && !isExiting ? 'translate-x-0 opacity-100' : 'translate-x-full opacity-0'}
      `}
    >
      <div className={`
        ${config.bgColor} ${config.textColor}
        rounded-lg shadow-lg p-4 relative overflow-hidden
      `}>
        {/* Background pattern */}
        <div className="absolute inset-0 opacity-10">
          <div className="absolute inset-0 bg-gradient-to-br from-white/20 to-transparent" />
        </div>
        
        {/* Content */}
        <div className="relative flex items-start space-x-3">
          {/* Icon */}
          <div className="flex-shrink-0">
            <Icon className={`w-6 h-6 ${config.iconColor}`} />
          </div>
          
          {/* Text content */}
          <div className="flex-1 min-w-0">
            <div className="text-sm font-medium">
              {config.title}
            </div>
            <div className="text-base font-semibold mt-1">
              {content.message}
            </div>
            {content.subtitle && (
              <div className="text-sm opacity-90 mt-1">
                {content.subtitle}
              </div>
            )}
            {content.extra && (
              <div className="text-xs opacity-75 mt-1">
                {content.extra}
              </div>
            )}
          </div>
          
          {/* Close button */}
          <button
            onClick={handleClose}
            className={`
              flex-shrink-0 ${config.iconColor} hover:text-white
              transition-colors duration-200
            `}
          >
            <X className="w-4 h-4" />
          </button>
        </div>
        
        {/* Progress bar */}
        <div className="absolute bottom-0 left-0 right-0 h-1 bg-black/20">
          <div
            className="h-full bg-white/30 transition-all duration-linear"
            style={{
              animation: `shrink ${duration}ms linear forwards`
            }}
          />
        </div>
      </div>
      
      <style jsx>{`
        @keyframes shrink {
          from { width: 100%; }
          to { width: 0%; }
        }
      `}</style>
    </div>
  );
};

/**
 * Notification Container Component
 * 
 * Manages multiple notifications with stacking
 */
export const NotificationContainer = ({ notifications, onClearNotification }) => {
  return (
    <div className="fixed top-4 right-4 z-50 space-y-2">
      {notifications.map((notification, index) => (
        <div
          key={notification.id}
          style={{
            transform: `translateY(${index * 10}px)`,
            zIndex: 50 - index
          }}
        >
          <NotificationToast
            notification={notification}
            onClose={onClearNotification}
            duration={5000 + (index * 1000)} // Stagger auto-hide
          />
        </div>
      ))}
    </div>
  );
};

export default NotificationToast;