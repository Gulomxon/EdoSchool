# Generated by Django 4.1.7 on 2023-04-02 10:57

import account.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.manager
import image_cropping.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(help_text='username must be unique', max_length=30, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Username')),
                ('first_name', models.CharField(max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last name')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Birthday')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=15, null=True, region=None, verbose_name='Phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('profile', models.ImageField(max_length=200, null=True, upload_to=account.models.profile_image_filename, verbose_name='Profile')),
                ('x', models.IntegerField(null=True)),
                ('y', models.IntegerField(null=True)),
                ('width', models.IntegerField(null=True)),
                ('height', models.IntegerField(null=True)),
                ('image', image_cropping.fields.ImageCropField(upload_to='images')),
                ('image_ratio', image_cropping.fields.ImageRatioField('image', '100x100', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='image ratio')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'account',
                'verbose_name_plural': 'accounts',
                'base_manager_name': 'account',
            },
            managers=[
                ('account', django.db.models.manager.Manager()),
            ],
        ),
    ]
