# Generated by Django 5.0.6 on 2024-06-30 21:56

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyQuiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('question', models.CharField(max_length=100)),
                ('marks', models.IntegerField(default=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('gfg_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('answer', models.CharField(max_length=100)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answer', to='MyQuiz.question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='question',
            name='gfg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gfg', to='MyQuiz.types'),
        ),
    ]
