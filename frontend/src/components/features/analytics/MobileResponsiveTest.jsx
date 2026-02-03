import React from 'react';
import { StudentAnalyticsDashboard } from './index';
import { ClassAnalyticsDashboard } from './index';
import { LeaderboardWidget, PointsDisplay, AchievementBadges, ErrorBoundary } from '../gamification';

/**
 * Test component to verify mobile responsiveness of all gamification features
 * This component can be used for testing and development purposes
 */
const MobileResponsiveTest = () => {
  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <div className="max-w-7xl mx-auto space-y-8">
        {/* Header */}
        <div className="text-center">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Mobile Responsiveness Test</h1>
          <p className="text-gray-600">Testing all gamification components across different screen sizes</p>
        </div>

        {/* Gamification Components */}
        <section>
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">Gamification Components</h2>
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <ErrorBoundary title="Leaderboard Error">
              <LeaderboardWidget 
                type="global" 
                limit={5} 
                showUserRank={true}
                className="lg:col-span-1"
              />
            </ErrorBoundary>
            <ErrorBoundary title="Points Error">
              <PointsDisplay 
                showHistory={true}
                showBreakdown={true}
                className="lg:col-span-1"
              />
            </ErrorBoundary>
            <ErrorBoundary title="Achievements Error">
              <AchievementBadges 
                showProgress={true}
                showNotifications={false}
                limit={6}
                className="lg:col-span-1"
              />
            </ErrorBoundary>
          </div>
        </section>

        {/* Student Analytics */}
        <section>
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">Student Analytics Dashboard</h2>
          <StudentAnalyticsDashboard />
        </section>

        {/* Class Analytics */}
        <section>
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">Class Analytics Dashboard</h2>
          <ClassAnalyticsDashboard classId="test-class-id" />
        </section>

        {/* Mobile Testing Instructions */}
        <section className="bg-blue-50 border border-blue-200 rounded-lg p-6">
          <h3 className="text-lg font-semibold text-blue-900 mb-3">Mobile Testing Instructions</h3>
          <div className="space-y-2 text-sm text-blue-800">
            <p><strong>Desktop (1024px+):</strong> All components should display in full grid layouts</p>
            <p><strong>Tablet (641px - 1024px):</strong> Components should adapt to 2-column layouts</p>
            <p><strong>Mobile (≤640px):</strong> Components should stack vertically with touch-friendly interactions</p>
            <p><strong>Touch Targets:</strong> All interactive elements should be at least 44px in height/width</p>
            <p><strong>Scrolling:</strong> Horizontal scrolling should be smooth and hide scrollbars</p>
            <p><strong>Notifications:</strong> Should position correctly on mobile screens</p>
          </div>
        </section>

        {/* Responsive Breakpoint Indicators */}
        <section className="bg-gray-100 rounded-lg p-4">
          <h3 className="text-lg font-semibold text-gray-800 mb-3">Current Breakpoint</h3>
          <div className="flex gap-2">
            <div className="block sm:hidden px-3 py-1 bg-red-500 text-white rounded text-sm">
              Mobile (≤640px)
            </div>
            <div className="hidden sm:block md:hidden px-3 py-1 bg-yellow-500 text-white rounded text-sm">
              Small Tablet (641px - 768px)
            </div>
            <div className="hidden md:block lg:hidden px-3 py-1 bg-blue-500 text-white rounded text-sm">
              Large Tablet (769px - 1024px)
            </div>
            <div className="hidden lg:block px-3 py-1 bg-green-500 text-white rounded text-sm">
              Desktop (1024px+)
            </div>
          </div>
        </section>
      </div>
    </div>
  );
};

export default MobileResponsiveTest;