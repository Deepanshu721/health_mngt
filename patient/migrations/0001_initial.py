# Generated by Django 3.2 on 2021-04-17 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('status', models.CharField(choices=[('A', 'Assigned'), ('D', 'Discharged')], max_length=1)),
                ('bed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bed.bed')),
            ],
        ),
    ]