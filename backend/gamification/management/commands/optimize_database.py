"""
Django management command to optimize database performance for gamification features.

This command:
- Creates recommended database indexes
- Analyzes query performance
- Sets up cache warming schedules
- Provides performance recommendations
"""

import logging
from django.core.management.base import BaseCommand, CommandError
from django.db import connection, transaction
from django.utils import timezone

from gamification.query_optimizer import query_optimizer
from gamification.cache_service import cache_service
from gamification.cached_leaderboard_manager import cached_leaderboard_manager
from gamification.cached_analytics_aggregator import cached_analytics_aggregator

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Optimize database performance for gamification features'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--create-indexes',
            action='store_true',
            help='Create recommended database indexes',
        )
        parser.add_argument(
            '--analyze-performance',
            action='store_true',
            help='Analyze current query performance',
        )
        parser.add_argument(
            '--warm-caches',
            action='store_true',
            help='Warm frequently accessed caches',
        )
        parser.add_argument(
            '--clear-caches',
            action='store_true',
            help='Clear all gamification caches',
        )
        parser.add_argument(
            '--full-optimization',
            action='store_true',
            help='Run complete optimization (indexes + cache warming)',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be done without making changes',
        )
    
    def handle(self, *args, **options):
        """Execute the optimization command."""
        self.stdout.write(
            self.style.SUCCESS('Starting database optimization for gamification features...')
        )
        
        try:
            if options['full_optimization']:
                self._run_full_optimization(options['dry_run'])
            else:
                if options['create_indexes']:
                    self._create_indexes(options['dry_run'])
                
                if options['analyze_performance']:
                    self._analyze_performance()
                
                if options['warm_caches']:
                    self._warm_caches(options['dry_run'])
                
                if options['clear_caches']:
                    self._clear_caches(options['dry_run'])
            
            self.stdout.write(
                self.style.SUCCESS('Database optimization completed successfully!')
            )
            
        except Exception as e:
            logger.error(f"Error during database optimization: {e}")
            raise CommandError(f'Optimization failed: {e}')
    
    def _run_full_optimization(self, dry_run: bool):
        """Run complete optimization process."""
        self.stdout.write('Running full optimization...')
        
        # Step 1: Analyze current performance
        self.stdout.write('Step 1: Analyzing current performance...')
        self._analyze_performance()
        
        # Step 2: Create indexes
        self.stdout.write('Step 2: Creating database indexes...')
        self._create_indexes(dry_run)
        
        # Step 3: Clear old caches
        self.stdout.write('Step 3: Clearing old caches...')
        self._clear_caches(dry_run)
        
        # Step 4: Warm caches
        self.stdout.write('Step 4: Warming caches...')
        self._warm_caches(dry_run)
        
        # Step 5: Final performance check
        self.stdout.write('Step 5: Final performance analysis...')
        self._analyze_performance()
    
    def _create_indexes(self, dry_run: bool):
        """Create recommended database indexes."""
        self.stdout.write('Creating recommended database indexes...')
        
        # Get index recommendations
        recommendations = query_optimizer.get_index_recommendations()
        
        self.stdout.write(f'Found {len(recommendations)} index recommendations:')
        for i, rec in enumerate(recommendations, 1):
            self.stdout.write(
                f'  {i}. {rec["table"]}.({", ".join(rec["columns"])}) - {rec["reason"]}'
            )
        
        if dry_run:
            self.stdout.write(self.style.WARNING('DRY RUN: Would create indexes but not executing'))
            return
        
        # Create indexes
        try:
            with transaction.atomic():
                results = query_optimizer.create_recommended_indexes()
                
                success_count = sum(1 for success in results.values() if success is True)
                total_count = len([k for k in results.keys() if not k == 'error'])
                
                if 'error' in results:
                    self.stdout.write(
                        self.style.ERROR(f'Error creating indexes: {results["error"]}')
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(f'Created {success_count}/{total_count} indexes successfully')
                    )
                    
                    # Show detailed results
                    for index_name, success in results.items():
                        if index_name != 'error':
                            status = 'SUCCESS' if success else 'FAILED'
                            style = self.style.SUCCESS if success else self.style.ERROR
                            self.stdout.write(style(f'  {index_name}: {status}'))
                            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to create indexes: {e}'))
            raise
    
    def _analyze_performance(self):
        """Analyze current query performance."""
        self.stdout.write('Analyzing query performance...')
        
        try:
            # Get performance statistics
            perf_stats = query_optimizer.analyze_query_performance()
            
            if 'error' in perf_stats:
                self.stdout.write(
                    self.style.WARNING(f'Performance analysis error: {perf_stats["error"]}')
                )
                return
            
            # Display connection info
            conn_info = perf_stats.get('connection_info', {})
            self.stdout.write(f'Database vendor: {conn_info.get("vendor", "unknown")}')
            self.stdout.write(f'Query count: {conn_info.get("queries_count", "unknown")}')
            
            # Display slow queries
            slow_queries = perf_stats.get('slow_queries', [])
            if slow_queries:
                self.stdout.write(f'Found {len(slow_queries)} slow queries:')
                for i, query_info in enumerate(slow_queries[:5], 1):  # Show top 5
                    if len(query_info) >= 4:
                        query, calls, total_time, mean_time = query_info[:4]
                        self.stdout.write(
                            f'  {i}. Mean time: {mean_time:.2f}ms, Calls: {calls}'
                        )
                        # Truncate long queries
                        query_preview = query[:100] + '...' if len(query) > 100 else query
                        self.stdout.write(f'     Query: {query_preview}')
            else:
                self.stdout.write('No slow query data available')
            
            # Display table statistics
            table_stats = perf_stats.get('table_statistics', [])
            if table_stats:
                self.stdout.write(f'Table statistics available for {len(table_stats)} columns')
            
            # Get cache performance
            leaderboard_stats = cached_leaderboard_manager.get_cache_performance_stats()
            analytics_stats = cached_analytics_aggregator.get_cache_performance_stats()
            
            self.stdout.write('Cache Performance:')
            self.stdout.write(f'  Leaderboard hit rate: {leaderboard_stats.get("hit_rate_percentage", 0):.1f}%')
            self.stdout.write(f'  Analytics hit rate: {analytics_stats.get("analytics_hit_rate_percentage", 0):.1f}%')
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Performance analysis failed: {e}'))
    
    def _warm_caches(self, dry_run: bool):
        """Warm frequently accessed caches."""
        self.stdout.write('Warming frequently accessed caches...')
        
        if dry_run:
            self.stdout.write(self.style.WARNING('DRY RUN: Would warm caches but not executing'))
            return
        
        try:
            # Warm leaderboard caches
            self.stdout.write('  Warming leaderboard caches...')
            leaderboard_results = cached_leaderboard_manager.preload_popular_data()
            
            success_count = sum(1 for result in leaderboard_results.values() 
                              if result is True or (isinstance(result, dict) and 'error' not in result))
            total_count = len(leaderboard_results)
            
            self.stdout.write(f'    Leaderboard caches: {success_count}/{total_count} successful')
            
            # Warm analytics caches
            self.stdout.write('  Warming analytics caches...')
            analytics_results = cached_analytics_aggregator.preload_popular_analytics()
            
            if 'error' not in analytics_results:
                # Count successful analytics warming
                analytics_success = 0
                analytics_total = 0
                
                for key, result in analytics_results.items():
                    if isinstance(result, dict):
                        if 'successful' in result:
                            analytics_success += result['successful']
                            analytics_total += result.get('attempted', result['successful'])
                        elif 'error' not in result:
                            analytics_success += len(result)
                            analytics_total += len(result)
                
                self.stdout.write(f'    Analytics caches: {analytics_success}/{analytics_total} successful')
            else:
                self.stdout.write(
                    self.style.WARNING(f'    Analytics warming error: {analytics_results["error"]}')
                )
            
            # Display cache statistics
            cache_stats = cache_service.get_cache_stats()
            total_keys = cache_stats.get('total_keys', 0)
            self.stdout.write(f'  Total cached keys: {total_keys}')
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Cache warming failed: {e}'))
            raise
    
    def _clear_caches(self, dry_run: bool):
        """Clear all gamification caches."""
        self.stdout.write('Clearing all gamification caches...')
        
        if dry_run:
            self.stdout.write(self.style.WARNING('DRY RUN: Would clear caches but not executing'))
            return
        
        try:
            # Get current cache stats
            cache_stats_before = cache_service.get_cache_stats()
            keys_before = cache_stats_before.get('total_keys', 0)
            
            # Clear caches
            success = cache_service.clear_all_caches()
            
            if success:
                self.stdout.write(self.style.SUCCESS(f'Cleared {keys_before} cache entries'))
            else:
                self.stdout.write(self.style.ERROR('Failed to clear caches'))
            
            # Reset performance counters
            cached_leaderboard_manager.reset_performance_counters()
            cached_analytics_aggregator.reset_performance_counters()
            
            self.stdout.write('Reset cache performance counters')
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Cache clearing failed: {e}'))
            raise
    
    def _display_recommendations(self):
        """Display performance recommendations."""
        self.stdout.write(self.style.SUCCESS('\nPerformance Recommendations:'))
        
        recommendations = [
            '1. Run this command with --full-optimization weekly',
            '2. Monitor cache hit rates and adjust timeouts as needed',
            '3. Consider adding more specific indexes for your query patterns',
            '4. Use bulk operations for large data updates',
            '5. Monitor slow query logs and optimize problematic queries'
        ]
        
        for rec in recommendations:
            self.stdout.write(f'  {rec}')
        
        self.stdout.write('\nFor ongoing monitoring, use:')
        self.stdout.write('  python manage.py optimize_database --analyze-performance')