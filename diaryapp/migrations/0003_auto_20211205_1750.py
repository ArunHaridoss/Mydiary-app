# Generated by Django 3.2.9 on 2021-12-05 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diaryapp', '0002_auto_20211205_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='host',
        ),
        migrations.AddField(
            model_name='notes',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='notesUser',
        ),
    ]
