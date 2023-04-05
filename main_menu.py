#### console application ---> save info about books
from book_crud import create_project, display_all_projects , delete_project, register_user, check_login, update_project,search_by_start_date,search_by_end_date
from colorama import Fore, Back, Style
def enter():
    while True:
        choice = input (f"{Fore.GREEN}Please choose from this list:{Style.RESET_ALL} \n 1-Register \n 2-Login \n 3-Exit \n{Fore.GREEN}Enter your choice:{Style.RESET_ALL} ")
        if choice == '1':
            register_user()
        elif choice == '2':
            check_login()
            f=check_login()
            if f==True:
                mainmenu()
            else:
                enter()
        elif choice == '3':
            print(Fore.YELLOW+ "***** Thanks for using our App *****")
            print(Style.RESET_ALL)
            exit()

def mainmenu():
    while True:
        choice = input(f"{Fore.GREEN}please choose from this list:{Style.RESET_ALL}\n 1-Create new project \n 2-List all projects \n 3-Edit the project \n 4-Delete project \n 5-Search by start date \n 6-Search by end date \n 7-Exit \n{Fore.GREEN}Enter your choice:{Style.RESET_ALL} ")
        if choice=='1':
            create_project()
        elif choice=='2':
            display_all_projects()
        elif choice=='3':
            update_project()
        elif choice=='4':
            delete_project()
        elif choice=='5':
            search_by_start_date()
        elif choice=='6':
            search_by_end_date()
        elif choice=='7':
            print(Fore.YELLOW+ "***** Thanks for using our App *****")
            print(Style.RESET_ALL)
            exit()
print(f"{Fore.MAGENTA}   Welcome To CROWD_FUNDING Console App \n{Fore.MAGENTA}   Telecom Applications Development\n{Fore.CYAN}               ITI\n      {Fore.YELLOW}CREATED BY: Esraa Nasser ")
print(Style.RESET_ALL)
enter()
mainmenu()