# filepath: /c:/Users/om/Desktop/aissmsioit/webapp/firstapp/migrations/0001_initial.py
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aissm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('bmi', models.FloatField()),
                ('children', models.IntegerField()),
                ('smoker', models.CharField(max_length=10)),
                ('region', models.CharField(max_length=20)),
                ('charges', models.FloatField()),
            ],
        ),
    ]