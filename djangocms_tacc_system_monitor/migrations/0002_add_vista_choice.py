from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_tacc_system_monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taccsitesystemmonitor',
            name='system',
            field=models.CharField(choices=[
                ('frontera.tacc.utexas.edu', 'Frontera'),
                ('stampede2.tacc.utexas.edu', 'Stampede2'),
                ('maverick2.tacc.utexas.edu', 'Maverick2'),
                ('longhorn.tacc.utexas.edu', 'Longhorn'),
                ('vista.tacc.utexas.edu', 'Vista')
            ], default='frontera.tacc.utexas.edu', max_length=255, verbose_name='System'),
        ),
    ]
