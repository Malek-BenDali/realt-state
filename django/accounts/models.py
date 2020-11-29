from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):#il faut obligatoirement un mot de passe
        if not email:
            raise ValueError('Il faut obligatoirement avoir un e-mail')
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)#built in function pour hacher le mot de passe
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    """ Les propietés d'utilisateur """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects= UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email