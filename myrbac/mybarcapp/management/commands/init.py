from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from ...models import Role, Resource
from django.contrib.auth import authenticate, login
import getpass


class Command(BaseCommand):
    help = '''init system with few Resources, Roles(which have resources with different permission set),
     Admin User(admin) and Normal User(User1)'''

    # def add_arguments(self, parser):
    #     parser.add_argument('-a', '--admin_user', type=str, help='Define a admin username')
    #     parser.add_argument('-n', '--normal_user', type=str, help='Define a normal username ')

    def handle(self, *args, **kwargs):
        admin = raw_input("Admin Name:")
        admin_pass = getpass.getpass(prompt='Admin Password: ', stream=None)
        if admin:
            User.objects.create_superuser(username=admin, email='', password=admin_pass)
        normal_user = raw_input("Normal User:")
        normal_user_password = getpass.getpass(prompt='Normal User Password: ', stream=None)
        if normal_user:
            User.objects.create_user(username=normal_user, email='', password=normal_user_password)
        nresource = input("No of Resource you want : ")
        for i in range(nresource):
            resource = raw_input(" Resource Name {0}: ".format(i+1))
            r = Resource(resource=resource)
            r.save()
        nrole = input("No of Role you want : ")
        for i in range(nrole):
            name = raw_input(" Role Name {0}: ".format(i+1))
            resource = raw_input(" Resource Name :")
            action_type = raw_input("Action Type [Default Read] (Read, Write, Delete) ")
            resource_instance = Resource.objects.get(resource=resource)
            r = Role(resource=resource_instance, name=name, action_type=action_type.lower())
            r.save()