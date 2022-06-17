# Generated by Django 4.0.4 on 2022-05-27 02:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_delete_image_category_name_en_skill_name_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner_project', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='progress',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='curriculum',
            field=models.FileField(blank=True, upload_to=projects.models.user_dir_path, validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx'])]),
        ),
    ]
