import json

class file:
    def __init__(self, file_name):
        self.file_name = file_name

    def clear(self):
        config = self.read()

        for x in config.keys():
            config[x] = ""

        self.write(config)
    
    def write(self, content):
        w = json.dumps(content)
        with open(self.file_name, "w") as f:
            f.write(w)

    def read(self):
        with open(self.file_name, "r") as f:
            w = f.read()
        fin = json.loads(w)
        return fin

    def print_config(self):
        exclude = ['setup']
        config_data = self.read()

        for item in exclude:
            del config_data[item]

        if config_data:
            for con, val in config_data.items():
                print('{}: {}'.format(con, val))

        else:
            return 0

    def edit_config(self):
        config_data = self.read()

        if config_data:
            for con, val in config_data.items():
                print('{}: {}'.format(con, val))

            change_again = True
            while change_again:
                config_change = input("what would you like to change?")

                if config_change in config_data.keys():
                    change_to = input("change value to:")
                    config_data[config_change] = change_to
                    print("value changed")
                    ignore_my_terrible_var_names = input("change another value?(Y/N)")

                    if ignore_my_terrible_var_names == 'Y':
                        change_again = True
                    else:
                        change_again = False

                else:
                    print("unknown key")
                    change_again = True
            
            self.write(config_data)


    def write_config(self):
        format_dict = {'connect.sid': '', '_csrf': '', 'username': '', 'weather_api': '', 'setup': '0'}
        skip = input("skip tutorial?(y/n):")

        if skip == 'y':
            format_dict['username'] = input('enter username here:')
            format_dict['connect.sid'] = input('enter connect.sid here:')
            format_dict['_csrf'] = input('enter _csrf here:')
            format_dict['setup'] = '1'
            format_dict['weather_api'] = input('input api token(openweathermap, leave blank if you dont want weather):')
            self.write(format_dict)

        elif skip == 'n':
            print('''First time setup:
Beginning setup process...''')

            print('''Creating a pytextnow account:
head to textnow.com and create an account. Once created find your username, should be in the settings tab
            ''')

            format_dict['username'] = input('enter username here:')

            print('''Now, enter inspect element, (ctrl shift I)
enter Application tab
Expand cookies and hit the "textnow.com" option
search for "connect.sid"''')

            format_dict['sid'] = input('enter connect.sid here:')

            print('''now search for "_csrf"''')

            format_dict['csrf'] = input('enter _csrf here:')

            if_weather = input('use weather api?(y/n):')
            if if_weather == 'y':
                format_dict['weather_api'] = input('input api token(openweathermap):')

            else:
                format_dict['setup'] = '1'
                self.write(format_dict)

        else:
            print("invalid")
            self.write_config()











