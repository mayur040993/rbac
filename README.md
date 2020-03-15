# rbac

This rbac project is build on Django Framework which is totally based on CLI.

## How to Set UP
git clone <>

After cloning this you can find requirenment.txt

Install Dependency

pip install -r requirenment.txt

Initialize the System by using following command.

You can init system with few Resources, Roles(which have resources with different permission set), Admin User(admin) and Normal User(User1)

python manage.py init 

When you enter the init command

Admin Name: Admin
Admin Password: 
Normal User:User1
Normal User Password: 
No of Resource you want : 2
Resource Name 1: Resource1
Resource Data 1: Data of Resource1
Resource Name 2: Resource2
Resource Data 2: Data of Resource2
No of Role you want : 1
Role Name 1: Role-1
Resource Name :Resource1
Action Type [Default Read] (Read, Write, Delete)


##For Login
python manage.py login

If you login using admin user, you will get the following options.

press 1 for Login as another user 
press 2 for Create user 
press 3 for Edit role         
press 4 for View Users 
press 5 for Logout
Please Input:

Every Options is self explanatory.

##In Edit Role: 
You can change action_type and assigned user on a paricular resource based on role name.
On selecting options 3, It will list all the role with the following options.

###Example

Enter Role Name to Edit : role1
Action Type (Read, Write, Delete) : Read
Press 1 Replace Existing Users 
Press 2 Update Users 
Else Press anything for Main Menu 
Input: 2
Enter comma seperated: user1,user2


If you login using normal user, you will get the following options

hi! you are logged in as user1 
press 1 for Login as another user 
press 2 for View roles                        
press 3 for access resource 
press 4 for Logout
Please Input:

