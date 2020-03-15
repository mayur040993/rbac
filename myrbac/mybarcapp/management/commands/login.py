from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from goto import with_goto
from ...models import Role, Resource
# from django.contrib.auth import authenticate, login
import getpass
from prettytable import PrettyTable
# from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = '''login to system'''

    def handle(self, *args, **kwargs):
        user = raw_input("User Name: ")
        password = getpass.getpass(prompt='Password: ', stream=None)
        getuser = User.objects.get(username=user)
        login = getuser.check_password(password)
        if login:
            if getuser.is_superuser:
                self.admin_options(user)
            else:
                self.user_options(user)
        else:
            print "Wrong username password"

    def admin_options(self,user):
        print """press 1 for Login as another user \npress 2 for Create user \npress 3 for Edit role \
        \npress 4 for Logout"""
        options = input("Please Input: ")
        self.admin_select(options,user)

    def user_options(self,user):
        print """hi! you are logged in as {0} \npress 1 for Login as another user \npress 2 for View roles \
                       \npress 3 for access resource \npress 4 for Logout""".format(user)
        options = input("Please Input: ")
        self.user_select(options,user)

    def login_user(self,user):
        return self.handle()

    def check_admin_flag(self,is_admin):
        if is_admin.lower() not in ['y','n','yes','no']:
            return False
        else:
            if is_admin.lower() in ['y','yes']:
                return 1
            else:
                return -1

    @with_goto
    def create_user(self,user):
        username = raw_input("Enter User Name :")
        password = getpass.getpass(prompt='Enter Password: ', stream=None)
        label .begin
        is_admin = raw_input("Is this user admin or not (Yes/No): ")
        is_admin_flag = self.check_admin_flag(is_admin)
        if is_admin_flag == False:
            print "Please select yes or no"
            goto .begin;
        if is_admin_flag == 1:
            User.objects.create_superuser(username=username,email='',password=password)
        else:
            User.objects.create_user(username=username,email='',password=password)
        print "User with username {0} Created Successfully: ".format(username)
        return self.admin_options(user)

    def view_role_general(self,user):
        role_list = Role.objects.all()
        tuple(role_list)
        table = PrettyTable(['Role Name', 'Action', 'Resource', 'Users'])
        for role in role_list:
            users = [ user_list.user.username  for user_list in role.users.all()]
            table.add_row([role.name, role.action_type, role.resource, ','.join(users)])

        print(table)
        return  "Viewing Role"

    def view_role(self,user):
        self.view_role_general(user)
        return self.user_options(user)


    def edit_role(self,user):
        self.view_role(user)
        return "Editing Role"

    def access_resource(self,user):
        return "Access Resource"

    def exit(self,user):
        print "Logout User {0}".format(user)
        return exit()

    def admin_select(self, argument,user):
        switcher = {
            1: self.login_user,
            2: self.create_user,
            3: self.edit_role,
            4: self.exit,
        }
        func = switcher.get(argument, lambda :"Invalid Option")
        func(user)

    def user_select(self, argument,user):
        switcher = {
            1: self.login_user,
            2: self.view_role,
            3: self.access_resource,
            4: self.exit,
        }
        func = switcher.get(argument, lambda :"Invalid Option")
        func(user)