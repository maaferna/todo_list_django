# Generated by Django 4.2.7 on 2023-11-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('priority', models.CharField(choices=[('', 'Select Priority'), ('low', 'Bajo'), ('medium', 'Medio'), ('high', 'Alto'), ('important', 'Importante')], default='', max_length=10)),
                ('effort', models.CharField(choices=[('', 'Select Effort'), ('low', 'Bajo'), ('medium', 'Medio'), ('high', 'Alto')], default='', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
