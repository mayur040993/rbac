from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from goto import with_goto
from ...models import Role, Resource,User as model_user
import getpass
from prettytable import PrettyTable

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
        \npress 4 for View Users \npress 5 for Logout"""
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

    def list_of_user(self,user):
        user_list = User.objects.all()
        table = PrettyTable(['Username', 'User Type'])
        for users in user_list:
            if users.is_superuser:
                table.add_row([users.username, 'Admin User'])
            else:
                table.add_row([users.username,'Normal User'])
        print table
        raw_input("Press Enter to continue...")
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
        raw_input("Press Enter to continue...")
        return self.user_options(user)

    @with_goto
    def edit_role(self,user):
        self.view_role_general(user)
        role_name = raw_input("Enter Role Name to Edit : ")
        try:
            role = Role.objects.get(name=role_name)
            label .action_type
            action_type =  raw_input("Action Type (Read, Write, Delete) : ")
            if action_type.lower() in ['read','write','delete']:
                role.action_type = action_type.lower()
                user_update_flag = raw_input("""Press 1 Replace Existing Users \nPress 2 Update Users \nElse Press anything for Main Menu \nInput: """)
                if user_update_flag not in ['1','2']:
                    self.admin_options(user)
                users_input = raw_input("Enter comma seperated: ")
                user_list = users_input.split(',')
                if user_update_flag == '1':
                    users_remove = [users_role.id for users_role in role.users.prefetch_related()]
                    role.users.remove(*tuple(users_remove))
                users_add = [users_id.id for users_id in model_user.objects.filter(user__username__in=user_list)]
                role.users.add(*tuple(users_add))
                role.save()
                print "Role Updated Successfully"
                self.view_role_general(user)
                raw_input("Press Enter to continue...")
            else:
                goto .action_type;
        except:
            print "No Role found with role name {0}".format(role_name)

        return  self.admin_options(user)

    @with_goto
    def access_resource(self,user):
        label .resource
        print "----------------------------------------------------"
        print "List of Resource Access you have"
        user_instance = model_user.objects.get(user__username=user)
        role_list = Role.objects.filter(users=user_instance)
        tuple(role_list)
        table = PrettyTable(['Resource', 'Action'])
        resource_dict={}
        for role in role_list:
            resource_dict[role.resource.resource] = role.action_type
            table.add_row([role.resource.resource,role.action_type])
        if len(role_list) == 0:
            print "You don't have access to any resource"
            return self.user_options(user)
        print(table)
        raw_input("Press Enter to continue...")
        print "----------------------------------------------------\n"
        resource_name = raw_input("Enter Resource Name for the action: ")
        if resource_name in resource_dict.keys():
            print "You have {0} access to {1} ".format(resource_dict[resource_name], resource_name)
            if resource_dict[resource_name].lower() == 'read':
                input = raw_input("Press 1 to Read Data\nEnter Any Key to go to main menu..\n")
                if input not in ['1']:
                    return self.user_options(user)
                else:
                    resource_instance = Resource.objects.get(resource=resource_name)
                    print resource_instance.data
            elif resource_dict[resource_name].lower() == 'write':
                input = raw_input("Press 1 to Read Data\nPress 2 to Update Data\nEnter Any Key to go to main menu..\n")
                if input not in ['1','2']:
                    return self.user_options(user)
                elif input == '1':
                    resource_instance = Resource.objects.get(resource=resource_name)
                    print resource_instance.data
                elif input == '2':
                    resource_instance = Resource.objects.get(resource=resource_name)
                    print resource_instance.data
                    data = raw_input("Enter New Data")
                    resource_instance.data = data
                    resource_instance.save()
            elif resource_dict[resource_name].lower() == 'delete':
                input = raw_input("Press 1 to Delete\nEnter Any Key to go to main menu..\n")
                if input not in ['1']:
                    return self.user_options(user)
                elif input == '1':
                    resource_instance = Resource.objects.get(resource=resource_name)
                    resource_instance.delete()
        else:
            print "Accessing wrong Resource"
            goto .resource

        return self.user_options(user)

    def exit(self,user):
        print "Logout User {0}".format(user)
        return exit()

    def admin_select(self, argument,user):
        switcher = {
            1: self.login_user,
            2: self.create_user,
            3: self.edit_role,
            4: self.list_of_user,
            5: self.exit,
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