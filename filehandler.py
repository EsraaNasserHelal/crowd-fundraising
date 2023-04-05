from colorama import Fore, Back, Style
def save_name_to_the_file(users_data):
    try:
        fileobj =open("users.txt", 'a')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.write(users_data)
        fileobj.close()
        return True
  
def save_project_to_the_file(project_data):
    try:
        fileobj =open("project.txt", 'a')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.write(project_data)
        fileobj.close()
        return True

def get_all_projects_from_file():
    try:
        fileobj =open("project.txt", 'r')
    except Exception as e:
        print(e)
        return False
    else:
        projects = fileobj.readlines()
        return projects


def find_project_by_id(project_id):
    projects = get_all_projects_from_file()
    for project in projects:
        print(project)
        project_details = project.strip('\n').split(":") 
        if project_details[0]==str(project_id):
            return True , project
    else:
        return False
    
def find_project_by_start_date(project_date):
    projects = get_all_projects_from_file()
    for found in projects:
        
        project_details = found.strip('\n').split(":")  
        if project_details[4]==str(project_date) :
            print(found)
            return True , found
    else:
        return False
def find_project_by_end_date(project_date):
    projects = get_all_projects_from_file()
    for found in projects:
        
        project_details = found.strip('\n').split(":")  
        if project_details[5]==str(project_date) :
            print(found)
            return True , found
    else:
        return False

#################################
#check and get EMAIL & PASSWORD  from users.txt
#################################
def get_all_users_from_file():
    try:
        fileobj =open("users.txt", 'r')
    except Exception as n:
        print(n)
        return False
    else:
        users = fileobj.readlines()
        return users


def find_user_by_pass_email(e,g):
    users = get_all_users_from_file()
    for user in users:
        # print(user)
        user_details = user.strip('\n').split(":")  # list user_details
        if user_details[3]==str(e) and user_details[2]==str(g) :
            #print("User logged in successfully!")
            return True , user      
    else:
            return False

#####################################
def save_projects_to_file(listofprojects):
    try:
        fileobj =open("project.txt", 'w')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.writelines(listofprojects)
        fileobj.close()
        return True


def delete_project_from_file(project):
    projects= get_all_projects_from_file()
    projects.remove(project)  # list
    removed = save_projects_to_file(projects)
    return removed


def update_project_in_file(project):
    while True:
        choice = input(f"{Fore.GREEN}please choose from this list:{Style.RESET_ALL}\n 1-Update the name of project \n 2-Update the details of project \n 3-Update the total target \n 4-Exit \n {Fore.GREEN}Enter the choice:{Style.RESET_ALL} ")
        if choice=='1':
            new_name=input(f"{Fore.BLUE}Enter the new name of project:{Style.RESET_ALL} ")
            projects= get_all_projects_from_file()
            for project in projects:
                project_details = project.strip('\n').split(":")  # list book_details
                b=project.replace(project_details[1], new_name)  # list
                updated = save_projects_to_file(b)
                return updated
            ###################
        elif choice=='2':
            new_details=input(f"{Fore.BLUE}Enter the new details of project:{Style.RESET_ALL} ")
            projects= get_all_projects_from_file()
            for project in projects:
                project_details = project.strip('\n').split(":")  # list book_details
                b=project.replace(project_details[2], new_details)  # list
                updated = save_projects_to_file(b)
                return updated
        elif choice=='3':
            new_target=input(f"{Fore.BLUE}Enter the new target of project:{Style.RESET_ALL} ")
            projects= get_all_projects_from_file()
            for project in projects:
                project_details = project.strip('\n').split(":")  # list book_details
                b=project.replace(project_details[3], new_target)  # list
                updated = save_projects_to_file(b)
                return updated
        elif choice=='4':
            print(Fore.YELLOW+ "***** Thanks for using our App *****")
            print(Style.RESET_ALL)
            exit()
    # new_name=input("enter the new name of project: ")
    # projects= get_all_projects_from_file()
    # for project in projects:
    #     # if str(book_id) in book:
    #     #     return True, book
    #    # print(book)
    #     project_details = project.strip('\n').split(":")  # list book_details
    #     b=project.replace(project_details[1], new_name)  # list
    #     updated = save_projects_to_file(b)
    #     return updated