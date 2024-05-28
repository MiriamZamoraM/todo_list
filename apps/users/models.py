from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class UserManager(BaseUserManager):
    
    use_in_migrations = True

    def create_user(self, email, password=None):

        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            is_staff=True,
            is_superadmin=False,
        )
        user.set_password(password)
        user.save()
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=150, verbose_name="Nombre")
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    status_delete = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        db_table = "users"
        verbose_name = "Usuario"

    def tokens_access(self):
        refresh = RefreshToken.for_user(self)
        return ({'access':str(refresh.access_token)})
 
    def tokens_refresh(self):
        refresh = RefreshToken.for_user(self)
        return {'refresh':str(refresh)}