from users.models import AbstractUser

def verify(username):
    if AbstractUser.objects.filter(username=username).count() == 0:
        return False
    return True