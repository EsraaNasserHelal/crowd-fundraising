
from inputshelper import  askforstring, askforInt, generate_id
from filehandler import  save_project_to_the_file, get_all_projects_from_file,save_name_to_the_file, \
    find_project_by_id, delete_project_from_file , find_user_by_pass_email, update_project_in_file, find_project_by_start_date,find_project_by_end_date
from colorama import Fore, Back, Style
import re
import datetime

def register_user():
    #asked for fname,lname,password,confirm password, email
    def first_name():
        while True:
            fname = input(Fore.BLUE+"Enter your first name: "+Style.RESET_ALL)
            if fname.isalpha():
                return fname
            else:
                print(Fore.RED+"Not a Valid Name, retry with right name: "+Style.RESET_ALL)
                # first_name();
                ###################################
    def last_name():
         while True:
            lname = input(Fore.BLUE+"Enter your last name: "+Style.RESET_ALL)
            if lname.isalpha():
               return lname
            else:
               print(Fore.RED+"Not a Valid Name, retry with right name: "+Style.RESET_ALL)
            #    last_name();
        
            ###################################
    def verify_email():
        while True:
            email = input(Fore.BLUE+"Enter your E-mail: "+Style.RESET_ALL)
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if(re.fullmatch(regex, email)):
               return email
        
            else:
               print (Fore.RED+"Not a Valid email , retry with right email: "+Style.RESET_ALL)
            #    verify_email();
   
            ###################################
    def set_password():
        while True:
            password = input(Fore.BLUE+"Set your password: "+Style.RESET_ALL)
            if password.isdigit():
               return password
            else:
               print(Fore.RED+"Not a Valid password, retry: "+Style.RESET_ALL)
            #    set_password();
               
            ####################################
    def confirm_password():
        # password=set_password()
        password2 = input(Fore.BLUE+"Confirm password: "+Style.RESET_ALL)
        return password2
    #############################################
    def verify_phone():
        while True:
            phone = input(Fore.BLUE+"Enter your Egyptian mobile number: "+Style.RESET_ALL)
            regex = r"^01[0-2,5]\d{8}$"
            if(re.fullmatch(regex, phone)):
               return phone
            else:
                print(Fore.RED+"Not a valid number, Retry with valid number"+Style.RESET_ALL)
    
             
    f= first_name();
    l=last_name();
    
    p=verify_phone();
    # p=confirm_password();
    s=set_password(); 
    
    def check_password():
        c=confirm_password();  
        while c!=s:
            c=confirm_password();
        return c
    g=check_password();
    e=verify_email();
    #print(f, l, e, g,p)
    users_data = f"{f}:{l}:{g}:{e}:{p}\n"
    added = save_name_to_the_file(users_data)
    if added:
            print(Fore.GREEN+"---name added successfully---"+Style.RESET_ALL)
    else:
            print(Fore.RED+"=== problem happended ---> try again please ----"+Style.RESET_ALL)
######################################################################################################

 

def check_login():
    user_mail = input(Fore.BLUE+"Please enter your mail: "+Style.RESET_ALL) 
    user_password = input(Fore.BLUE+"Please enter your password: "+Style.RESET_ALL) 
    ## search if user exists in the users
    found = find_user_by_pass_email(user_mail , user_password)
    if found :
        print(Fore.GREEN+"--- login successfuly--- ")
        print(Style.RESET_ALL)
        
        return True
    else:
        print(Fore.RED+"user not found, please try again !!! "+Style.RESET_ALL)
        return False
   
######################################################################################################
def verify_date():
        while True:
            start_date_of_project = input(Fore.BLUE+"Please enter project start date: "+Style.RESET_ALL)
            # end_date_of_project = input(Fore.BLUE+"Please enter project end date: "+Style.RESET_ALL)
            return  start_date_of_project
def verify_date2():
        while True:
            # start_date_of_project = input(Fore.BLUE+"Please enter project start date: "+Style.RESET_ALL)
            end_date_of_project = input(Fore.BLUE+"Please enter project end date: "+Style.RESET_ALL)
            return   end_date_of_project
            

            
                         
def create_project():
    ## ask for title , no_of_pages
    title = askforstring(Fore.BLUE+"Please enter project title: "+Style.RESET_ALL)
    details = input(Fore.BLUE+"Please enter project details: "+Style.RESET_ALL)
    total_target = askforInt(Fore.BLUE+"Please enter project total target (EGP): "+Style.RESET_ALL)
    
    # date_of_project = input("Please enter project date: ")
    d=verify_date()
    d2=verify_date2()
    # if d==date_of_project:
    print(title, details, total_target, d,d2)

    project_id = generate_id()
    project_data = f"{project_id}:{title}:{details}:{total_target}:{d}:{d2}\n"
    added = save_project_to_the_file(project_data)
    if added:
                print(f" {Fore.GREEN}---project added successfully---")
                print(Style.RESET_ALL)
                return
    else:
                print(Fore.RED+"=== problem happended ---> try again please ----"+Style.RESET_ALL)



def display_all_projects():
    projects = get_all_projects_from_file()
    if projects:
        print(projects)
        for project in projects:
            print(project)
    else:
        print(Fore.RED+'---- the list is empty ----')
        print(Style.RESET_ALL)




def delete_project():
    project_id = askforInt(Fore.BLUE+"Please enter the id of the project you want to delete: "+Style.RESET_ALL) # int
    ## search if book exists in the books
    found = find_project_by_id(project_id)
    if found :
        print(Fore.GREEN+"--- projects found--- ")
        removed=delete_project_from_file(found[1])
        if removed:
            print(Fore.GREEN+'--- project deleted successfully ---')
            print(Style.RESET_ALL)

        else:
            print(Fore.RED+"--- problem happened while deleting the project ---")
            print(Style.RESET_ALL)

    else:
        print(Back.YELLOW+"project not found, please try again with valid id ")
        print(Style.RESET_ALL)

    ## delete ?
def search_by_start_date():
    project_date = input(Fore.BLUE+"Please enter the date of the project you want: "+Style.RESET_ALL) # int
    ## search if book exists in the books
    found = find_project_by_start_date(project_date)
    if found :
        print(Fore.GREEN+"--- project found--- ")
        print(Style.RESET_ALL) 
    else:
        print(Back.YELLOW+"project not found, please try again with valid date ")
        print(Style.RESET_ALL)
def search_by_end_date():
    project_date = input(Fore.BLUE+"Please enter the date of the project you want: "+Style.RESET_ALL) # int
    ## search if book exists in the books
    found = find_project_by_end_date(project_date)
    if found :
        print(Fore.GREEN+"--- project found--- ")
        print(Style.RESET_ALL) 
    else:
        print(Back.YELLOW+"project not found, please try again with valid date ")
        print(Style.RESET_ALL)

    
    
def update_project():
        project_id = askforInt(Fore.BLUE+"Please enter the id of the project you want to edit: "+Style.RESET_ALL) # int
    ## search if book exists in the books
        found = find_project_by_id(project_id)
        if found :
            print(Fore.GREEN+"--- project found--- ")
            print(Style.RESET_ALL)
  
            updated=update_project_in_file(found)
            if updated:
                print(Back.GREEN+'--- project updated successfully ---')
                print(Style.RESET_ALL)
            else:
                print(Back.RED+"--- problem happened while updating the project ---")
                print(Style.RESET_ALL)
        else:
            print(Back.YELLOW+"project not found, please try again with valid id ")
            print(Style.RESET_ALL)
    ## UPDATE ?
    
