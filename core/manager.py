from django.contrib.auth.base_user import BaseUserManager
# from . import constants as user_constants
class UserManager(BaseUserManager):
    # use_in_migrations = True
    def create_user(self, username, password = None, **kwargs):
        
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **kwargs):

        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))

        return self.create_user(username=username,password = password ,**kwargs)