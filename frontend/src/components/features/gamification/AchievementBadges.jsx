import React, { useState, useEffect, useRef } from 'react';
import { Award, Star, Crown, Zap, Target, Flame, Trophy, Lock, CheckCircle2, Sparkles } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { Card, CardContent, CardHeader, CardTitle } from '../../ui/card';
import { Badge } from '../../ui/badge';
import { Button } from '../../ui/button';
import { Dialog, DialogContent, DialogHeader, DialogTitle } from '../../ui/dialog';
import { gamificationService } from '../../../services/gamificationService';
import websocketService from '../../../services/websocketService';
import './MobileResponsive.css';

const AchievementBadges = ({ 
  showProgress = true, 
  showNotifications = true,
  compact = false,
  limit = null,
  className = '' 
}) => {
  const [earnedAchievements, setEarnedAchievements] = useState([]);
  const [availableAchievements, setAvailableAchievements] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedAchievement, setSelectedAchievement] = useState(null);
  const [newAchievements, setNewAchievements] = useState([]);
  const [showAllDialog, setShowAllDialog] = useState(false);
  const wsRef = useRef(null);

  // Fetch achievements data
  const fetchAchievements = async () => {
    try {
      setLoading(true);
      const [earnedResponse, availableResponse] = await Promise.all([
        gamificationService.getUserAchievements(),
        gamificationService.getAvailableAchievements()
      ]);

      if (earnedResponse.success) {
        const earnedData = earnedResponse.data.results || earnedResponse.data;
        setEarnedAchievements(Array.isArray(earnedData) ? earnedData : []);
      }

      if (availableResponse.success) {
        const availableData = availableResponse.data.results || availableResponse.data;
        setAvailableAchievements(Array.isArray(availableData) ? availableData : []);
      }

      setError(null);
    } catch (err) {
      console.error('Failed to fetch achievements:', err);
      setError('Failed to load achievements');
    } finally {
      setLoading(false);
    }
  };

  // Setup WebSocket connection for real-time achievement notifications
  useEffect(() => {
    fetchAchievements();

    // Setup WebSocket for real-time updates using the service
    const connectWebSocket = async () => {
      try {
        if (websocketService.isAuthenticated) {
          await websocketService.connect('game');
          
          // Add event listeners for achievement updates
          websocketService.addEventListener('game', 'achievement_earned', (data) => {
            console.log('Achievement earned:', data);
            
            // Show notification for new achievement
            if (showNotifications) {
              setNewAchievements(prev => [...prev, data.achievement]);
              setTimeout(() => {
                setNewAchievements(prev => prev.filter(a => a.name !== data.achievement.name));
              }, 5000);
            }
            
            // Refresh achievements data
            fetchAchievements();
          });
          
          console.log('Achievements WebSocket connected');
        }
      } catch (error) {
        if (process.env.NODE_ENV === 'development') {
          console.warn('Achievements WebSocket not available, using polling fallback:', error);
        }
        // Fallback to polling every 60 seconds
        const interval = setInterval(fetchAchievements, 60000);
        return () => clearInterval(interval);
      }
    };

    connectWebSocket();

    return () => {
      // Clean up WebSocket listeners
      websocketService.removeEventListener('game', 'achievement_earned', fetchAchievements);
    };
  }, [showNotifications]);

  // Get achievement icon based on type
  const getAchievementIcon = (achievement) => {
    const iconMap = {
      first_completion: CheckCircle2,
      streak: Flame,
      perfect_score: Star,
      speed: Zap,
      milestone: Trophy,
      default: Award
    };
    
    const IconComponent = iconMap[achievement.badge_type] || iconMap.default;
    return <IconComponent className="w-5 h-5" />;
  };

  // Get rarity styling
  const getRarityStyling = (rarity) => {
    const styles = {
      common: 'bg-gray-100 border-gray-300 text-gray-700',
      uncommon: 'bg-green-100 border-green-300 text-green-700',
      rare: 'bg-blue-100 border-blue-300 text-blue-700',
      legendary: 'bg-gradient-to-br from-purple-100 to-pink-100 border-purple-300 text-purple-700'
    };
    return styles[rarity] || styles.common;
  };

  // Get rarity glow effect
  const getRarityGlow = (rarity) => {
    const glows = {
      common: '',
      uncommon: 'shadow-green-200',
      rare: 'shadow-blue-200',
      legendary: 'shadow-purple-300 shadow-lg'
    };
    return glows[rarity] || '';
  };

  const displayedEarned = limit && Array.isArray(earnedAchievements) ? earnedAchievements.slice(0, limit) : (Array.isArray(earnedAchievements) ? earnedAchievements : []);
  const displayedAvailable = limit && Array.isArray(availableAchievements) ? availableAchievements.slice(0, limit) : (Array.isArray(availableAchievements) ? availableAchievements : []);

  if (loading) {
    return (
      <Card className={`${className}`}>
        <CardHeader className="pb-3">
          <CardTitle className="text-lg flex items-center gap-2">
            <Award className="w-5 h-5 text-indigo-600" />
            Achievements
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-3 gap-3">
            {[...Array(6)].map((_, i) => (
              <div key={i} className="aspect-square bg-gray-100 rounded-lg animate-pulse"></div>
            ))}
          </div>
        </CardContent>
      </Card>
    );
  }

  return (
    <>
      {/* Achievement Notifications */}
      <AnimatePresence>
        {newAchievements.map((achievement, index) => (
          <motion.div
            key={achievement.name}
            initial={{ opacity: 0, y: -50, scale: 0.8 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -50, scale: 0.8 }}
            className="fixed top-4 right-4 z-50 bg-white border-2 border-yellow-300 rounded-xl p-4 shadow-2xl max-w-sm achievement-notification mobile-notification"
            style={{ marginTop: index * 80 }}
          >
            <div className="flex items-center gap-3">
              <div className={`
                w-12 h-12 rounded-full flex items-center justify-center
                ${getRarityStyling(achievement.rarity)}
                ${getRarityGlow(achievement.rarity)}
              `}>
                <span className="text-2xl">{achievement.icon}</span>
              </div>
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <h4 className="font-bold text-gray-900">Achievement Unlocked!</h4>
                  <Sparkles className="w-4 h-4 text-yellow-500" />
                </div>
                <p className="text-sm font-semibold text-gray-800">{achievement.name}</p>
                <p className="text-xs text-gray-600">{achievement.description}</p>
              </div>
            </div>
          </motion.div>
        ))}
      </AnimatePresence>

      <Card className={`${className}`}>
        <CardHeader className="pb-3">
          <CardTitle className="text-lg flex items-center justify-between">
            <div className="flex items-center gap-2">
              <Award className="w-5 h-5 text-indigo-600" />
              Achievements
            </div>
            <div className="flex items-center gap-2">
              <Badge variant="secondary" className="text-xs">
                {earnedAchievements.length}/{earnedAchievements.length + availableAchievements.length}
              </Badge>
              {limit && (earnedAchievements.length + availableAchievements.length) > limit && (
                <Button 
                  variant="ghost" 
                  size="sm" 
                  onClick={() => setShowAllDialog(true)}
                  className="text-xs"
                >
                  View All
                </Button>
              )}
            </div>
          </CardTitle>
        </CardHeader>
        
        <CardContent className="pt-0">
          {error ? (
            <div className="text-center py-4">
              <p className="text-gray-500 text-sm mb-2">{error}</p>
              <p className="text-xs text-gray-400">
                Backend gamification API not available yet
              </p>
            </div>
          ) : (
            <>
              {/* Earned Achievements */}
              {displayedEarned.length > 0 && (
                <div className="mb-4">
                  <h4 className="text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2">
                    <Trophy className="w-4 h-4 text-yellow-500" />
                    Earned ({earnedAchievements.length})
                  </h4>
                  <div className="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-6 gap-3">
                    {displayedEarned.map((achievement, index) => (
                      <motion.div
                        key={achievement.achievement.id}
                        initial={{ opacity: 0, scale: 0.8 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ delay: index * 0.1 }}
                        whileHover={{ scale: 1.05 }}
                        whileTap={{ scale: 0.95 }}
                        onClick={() => setSelectedAchievement(achievement.achievement)}
                        className={`
                          aspect-square rounded-lg border-2 flex flex-col items-center justify-center p-2 cursor-pointer transition-all achievement-badge touch-target
                          ${getRarityStyling(achievement.achievement.rarity)}
                          ${getRarityGlow(achievement.achievement.rarity)}
                          hover:shadow-md
                        `}
                      >
                        <span className="text-2xl mb-1">{achievement.achievement.icon}</span>
                        {!compact && (
                          <span className="text-xs font-semibold text-center leading-tight achievement-badge-text">
                            {achievement.achievement.name}
                          </span>
                        )}
                      </motion.div>
                    ))}
                  </div>
                </div>
              )}

              {/* Available Achievements */}
              {showProgress && displayedAvailable.length > 0 && (
                <div>
                  <h4 className="text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2">
                    <Target className="w-4 h-4 text-gray-500" />
                    Available ({availableAchievements.length})
                  </h4>
                  <div className="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-6 gap-3">
                    {displayedAvailable.map((achievement, index) => (
                      <motion.div
                        key={achievement.id}
                        initial={{ opacity: 0, scale: 0.8 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ delay: index * 0.1 }}
                        whileHover={{ scale: 1.05 }}
                        whileTap={{ scale: 0.95 }}
                        onClick={() => setSelectedAchievement(achievement)}
                        className="aspect-square rounded-lg border-2 border-gray-200 bg-gray-50 flex flex-col items-center justify-center p-2 cursor-pointer transition-all hover:bg-gray-100 hover:border-gray-300 relative"
                      >
                        <div className="absolute inset-0 bg-gray-200 opacity-50 rounded-lg"></div>
                        <Lock className="w-4 h-4 text-gray-400 mb-1 relative z-10" />
                        {!compact && (
                          <span className="text-xs font-semibold text-center leading-tight text-gray-500 relative z-10">
                            {achievement.name}
                          </span>
                        )}
                      </motion.div>
                    ))}
                  </div>
                </div>
              )}

              {/* Empty State */}
              {earnedAchievements.length === 0 && availableAchievements.length === 0 && (
                <div className="text-center py-8">
                  <Award className="w-12 h-12 text-gray-300 mx-auto mb-3" />
                  <p className="text-gray-500 mb-2">No achievements yet</p>
                  <p className="text-xs text-gray-400">Complete practice questions to unlock achievements!</p>
                </div>
              )}
            </>
          )}
        </CardContent>
      </Card>

      {/* Achievement Detail Dialog */}
      <Dialog open={!!selectedAchievement} onOpenChange={() => setSelectedAchievement(null)}>
        <DialogContent className="max-w-md mobile-dialog">
          {selectedAchievement && (
            <>
              <DialogHeader>
                <DialogTitle className="flex items-center gap-3">
                  <div className={`
                    w-12 h-12 rounded-full flex items-center justify-center
                    ${getRarityStyling(selectedAchievement.rarity)}
                  `}>
                    <span className="text-2xl">{selectedAchievement.icon}</span>
                  </div>
                  <div>
                    <h3 className="text-lg font-bold">{selectedAchievement.name}</h3>
                    <Badge variant="outline" className="text-xs capitalize">
                      {selectedAchievement.rarity}
                    </Badge>
                  </div>
                </DialogTitle>
              </DialogHeader>
              
              <div className="space-y-4">
                <p className="text-gray-600">{selectedAchievement.description}</p>
                
                {selectedAchievement.point_threshold && (
                  <div className="bg-gray-50 p-3 rounded-lg">
                    <p className="text-sm text-gray-700">
                      <strong>Requirement:</strong> {selectedAchievement.point_threshold} points
                    </p>
                  </div>
                )}
                
                <div className="flex items-center justify-between text-sm text-gray-500">
                  <span>Badge Type: {selectedAchievement.badge_type.replace('_', ' ')}</span>
                  {earnedAchievements.find(e => e.achievement.id === selectedAchievement.id) && (
                    <div className="flex items-center gap-1 text-green-600">
                      <CheckCircle2 className="w-4 h-4" />
                      <span>Earned</span>
                    </div>
                  )}
                </div>
              </div>
            </>
          )}
        </DialogContent>
      </Dialog>

      {/* View All Achievements Dialog */}
      <Dialog open={showAllDialog} onOpenChange={setShowAllDialog}>
        <DialogContent className="max-w-4xl max-h-[80vh] overflow-y-auto mobile-dialog mobile-dialog-content">
          <DialogHeader>
            <DialogTitle>All Achievements</DialogTitle>
          </DialogHeader>
          
          <div className="space-y-6">
            {/* All Earned Achievements */}
            {earnedAchievements.length > 0 && (
              <div>
                <h4 className="text-lg font-semibold text-gray-800 mb-4 flex items-center gap-2">
                  <Trophy className="w-5 h-5 text-yellow-500" />
                  Earned ({earnedAchievements.length})
                </h4>
                <div className="grid grid-cols-4 sm:grid-cols-6 md:grid-cols-8 gap-3">
                  {earnedAchievements.map((achievement) => (
                    <div
                      key={achievement.achievement.id}
                      onClick={() => setSelectedAchievement(achievement.achievement)}
                      className={`
                        aspect-square rounded-lg border-2 flex flex-col items-center justify-center p-2 cursor-pointer transition-all
                        ${getRarityStyling(achievement.achievement.rarity)}
                        ${getRarityGlow(achievement.achievement.rarity)}
                        hover:shadow-md
                      `}
                    >
                      <span className="text-xl mb-1">{achievement.achievement.icon}</span>
                      <span className="text-xs font-semibold text-center leading-tight">
                        {achievement.achievement.name}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* All Available Achievements */}
            {availableAchievements.length > 0 && (
              <div>
                <h4 className="text-lg font-semibold text-gray-800 mb-4 flex items-center gap-2">
                  <Target className="w-5 h-5 text-gray-500" />
                  Available ({availableAchievements.length})
                </h4>
                <div className="grid grid-cols-4 sm:grid-cols-6 md:grid-cols-8 gap-3">
                  {availableAchievements.map((achievement) => (
                    <div
                      key={achievement.id}
                      onClick={() => setSelectedAchievement(achievement)}
                      className="aspect-square rounded-lg border-2 border-gray-200 bg-gray-50 flex flex-col items-center justify-center p-2 cursor-pointer transition-all hover:bg-gray-100 hover:border-gray-300 relative"
                    >
                      <div className="absolute inset-0 bg-gray-200 opacity-50 rounded-lg"></div>
                      <Lock className="w-4 h-4 text-gray-400 mb-1 relative z-10" />
                      <span className="text-xs font-semibold text-center leading-tight text-gray-500 relative z-10">
                        {achievement.name}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </DialogContent>
      </Dialog>
    </>
  );
};

export default AchievementBadges;