from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from phonenumber_field.modelfields import PhoneNumberField
from EdoSchool.data.models import Course

from data.models import Subject

unic_username_validator = UnicodeUsernameValidator()
models.Model

class AccountManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self._create_user(username, password, **extra_fields)


def profile_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    new_filename = "profile/"+timestamp+"."+ext
    return new_filename

class Account(AbstractBaseUser):
    username                            = models.CharField(verbose_name="Username", 
                                                           max_length=30, 
                                                           unique=True, 
                                                           validators=[unic_username_validator], 
                                                           help_text="username must be unique"
                                                           )
    first_name                          = models.CharField("First name", max_length=150)
    last_name                           = models.CharField("Last name", max_length=150)
    birthday                            = models.DateField("Birthday", null=True, blank=True)
    phone                               = PhoneNumberField("Phone number", max_length=15, null=True, blank=True)
    email                               = models.EmailField("Email address", max_length=254)
    is_superuser                        = models.BooleanField(default=False)
    is_active                           = models.BooleanField(default=True)
    is_staff                            = models.BooleanField(default=False)
    last_login                          = models.DateTimeField(auto_now=True)
    profile                             = models.ImageField("Profile", upload_to=profile_image_filename, max_length=200, null=True)
    
    
    created_at                          = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    account = AccountManager()
    
    def __str__(self):
        return self.username  
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name
    
    

    
    class Meta:
        base_manager_name = 'account'
        verbose_name = 'account'
        verbose_name_plural = 'accounts'
        
    def has_perm(self, perm, obj=None):
        return (self.is_active and self.is_superuser)
    
    def has_module_perms(self, app_label):
        return (self.is_active and self.is_superuser)
    

# type of users:

def cs_upload( instance, filename):
    ext = filename.split('.')[-1]
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    new_filename = "teacher_cv/"+timestamp+"."+ext
    return new_filename

class Teacher(models.Model):
    Teacher_type = (
        ("support", "Support"),
        ("teacher", "Teacher"),
    )
    user            = models.OneToOneField(Account, on_delete=models.CASCADE)
    teacher_type    = models.CharField(max_length=50, choices=Teacher_type)
    subject         = models.ForeignKey(Subject, on_delete=models.CASCADE)
    budget          = models.IntegerField()
    cv              = models.FileField(upload_to=None, max_length=200)
    

    
class Staff(models.Model):
    Staff_type = (
        ("reseption", "Reseption"),
        ("accountant", "Accountant"),
        ("manager", "Manager"),
        ("hr","HR"),
    )
    user            = models.OneToOneField(Account, on_delete=models.CASCADE)
    staff_type      = models.CharField(max_length=50, choices=Staff_type)
    budjet          = models.IntegerField()
    
class Student(models.Model):
    user            = models.ForeignKey(Account, on_delete=models.CASCADE)
    course          = models.ForeignKey(Course, on_delete=models.CASCADE)