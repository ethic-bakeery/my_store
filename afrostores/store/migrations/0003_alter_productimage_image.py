# Generated by Django 4.2.9 on 2024-07-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/images'),
        ),
    ]