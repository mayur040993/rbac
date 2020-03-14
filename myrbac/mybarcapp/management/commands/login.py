from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from ...models import Role, Resource
from django.contrib.auth import authenticate, login
import getpass
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = '''login to system'''

    def handle(self, *args, **kwargs):
        user = raw_input("User Name: ")
        password = getpass.getpass(prompt='Password: ', stream=None)
        user = User.objects.get(username=user)
        login = user.check_password(password)
        if login:
            if user.is_superuser:
                print """press 1 for login as another user \npress 2 for create user \npress 3 for edit role"""
                options = input("Please Input: ")
                print options
                if options == 1:
                    self.handle()
            else:
                print "you are normal user"
        else:
            print "Wrong username password"