# Generated by Django 3.1.5 on 2021-05-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_quizmodel_secs'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizmodel',
            name='totalQues',
            field=models.IntegerField(null=True),
        ),
    ]
