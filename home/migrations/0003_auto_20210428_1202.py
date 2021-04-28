# Generated by Django 3.2 on 2021-04-28 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20210428_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='vote_ans',
            field=models.ManyToManyField(blank=True, default=None, related_name='vote_ans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='VoteAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField(default=True)),
                ('answer', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='answerid', to='home.answer')),
                ('user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='userid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
