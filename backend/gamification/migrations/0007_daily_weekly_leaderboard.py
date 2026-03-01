from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0006_alter_practiceprogress_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboardentry',
            name='leaderboard_type',
            field=models.CharField(
                choices=[
                    ('global', 'Global'),
                    ('daily', 'Daily'),
                    ('weekly', 'Weekly'),
                    ('class', 'Class-specific'),
                ],
                max_length=20,
            ),
        ),
    ]
