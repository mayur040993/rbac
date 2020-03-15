# RBAC 

This rbac project is build on Django Framework which is totally based on CLI.

## How to Set UP
git clone https://github.com/mayur040993/rbac.git

After cloning this you can find requirenment.txt

##Install Dependency

**pip install -r requirenment.txt**

## Initialize System

You can init system with few Resources, Roles(which have resources with different permission set), Admin User(admin) and Normal User(User1)

Run Following command to initialize the system with basic info.

**python manage.py init** 

When you enter the init command it will ask you to input some data 

#### Example:

>`Admin Name: Admin` <br>
`Admin Password:` <br>
`Normal User:User1`<br>
`Normal User Password:` <br>
`No of Resource you want : 2`<br>
`Resource Name 1: Resource1`<br>
`Resource Data 1: Data of Resource1`<br>
`Resource Name 2: Resource2`<br>
`Resource Data 2: Data of Resource2`<br>
`No of Role you want : 1`<br>
`Role Name 1: Role-1`<br>
`Resource Name :Resource1`<br>
`Action Type [Default Read] (Read, Write, Delete)`<br>


## For Login
**python manage.py login**

If you login using admin user, you will get the following options.

>`press 1 for Login as another user`<br>
`press 2 for Create user `<br>
`press 3 for Edit role`  
`press 4 for View Users `<br>
`press 5 for Logout`<br>
`Please Input:`<br>

Every Options is self explanatory.

**In Edit Role:** 
You can change action_type,users of a particular role based on role name.
On selecting options 3, It will list all the role with the following options.

#### Example

>`Enter Role Name to Edit : <role_name>`<br>
`Action Type (Read, Write, Delete) : Read`<br>
`Press 1 Replace Existing Users`<br>
`Press 2 Update Users`<br>
`Else Press anything for Main Menu `<br>
`Input: 2`<br>
`Enter comma seperated: user1,user2`<br>

If you login using normal user, you will get the following options

>`hi! you are logged in as user1` <br>
`press 1 for Login as another user `<br>
`press 2 for View roles`                       
`press 3 for access resource`<br> 
`press 4 for Logout`<br>
`Please Input:`<br>

**In Option 3:**
It will list all the resource user has access to it with action_type (read,write,delete) in a tabular form.
User can alter the resource data based on the action type.
