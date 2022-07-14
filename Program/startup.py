from Program.commands import ptn_init
from Program.funcs import file
import sys


config_file = 'config.json'
main_config = file(config_file)

def global_startup():

    print('''Startup, what would you like to do:
1: bot startup
2: edit config
3: view config
4: clear config''')

    startup_choice = int(input("choice:"))
    
    if startup_choice == 2:
        main_config.edit_config()
        global_startup()
    
    elif startup_choice == 3:
        main_config.print_config()
        global_startup()
    
    elif startup_choice == 1:
        ac_numbers = []
        ptn_init(ac_numbers)

    elif startup_choice == 4:
        main_config.clear()
        print("config cleared")
    
    else:
        print("invalid")
        global_startup()

def init_start():
    if main_config.read()['setup'] == "":
        print("starting first time setup")
        main_config.write_config()
    
    else:
        global_startup()


 





