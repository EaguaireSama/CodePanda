# Generated by Django 3.2 on 2021-05-02 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='vote_ques',
            field=models.ManyToManyField(blank=True, default=None, related_name='vote_ques', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='VoteQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField(default=True)),
                ('question', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='questionid', to='home.question')),
                ('user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='userid1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
