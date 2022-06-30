# Generated by Django 4.0.4 on 2022-06-30 06:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_skill_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('icon', models.FileField(upload_to='social_icons', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'svg', 'bmp', 'jpeg', 'ico', 'webp'])])),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.socialicon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_social', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
