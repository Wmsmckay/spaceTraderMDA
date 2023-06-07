import requests
import sys

title = '''

              _-o#&&*\'\'\'\'?d:>b\\_\r\n          _o/\"`\'\'  \'\',, dMF9MMMMMHo_\r\n       .o&#\'        `\"MbHMMMMMMMMMMMHo.\r\n     .o\"\" \'         vodM*$&&HMMMMMMMMMM?.\r\n    ,\'              $M&ood,~\'`(&##MMMMMMH\\\r\n   /               ,MMMMMMM#b?#bobMMMMHMMML\r\n  &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk\r\n ?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L\r\n|               |MMMMMMMMMMMMMMMMMMMMbMH\'   T,\r\n$H#:            `*MMMMMMMMMMMMMMMMMMMMb#}\'  `?\r\n]MMH#             \"\"*\"\"\"\"*#MMMMMMMMMMMMM\'    -\r\nMMMMMb_                   |MMMMMMMMMMMP\'     :\r\nHMMMMMMMHo                 `MMMMMMMMMT       .\r\n?MMMMMMMMP                  9MMMMMMMM}       -\r\n-?MMMMMMM                  |MMMMMMMMM?,d-    \'\r\n :|MMMMMM-                 `MMMMMMMT .M|.   :\r\n  .9MMM[                    &MMMMM*\' `\'    .\r\n   :9MMk                    `MMM#\"        -\r\n     &M}                     `          .-\r\n      `&.                             .\r\n        `~,   .                     ./\r\n            . _                  .-\r\n              \'`--._,dd###pp=\"\"\'

  ____                             _____                 _             
 / ___|  _ __    __ _   ___  ___  |_   _|_ __  __ _   __| |  ___  _ __ 
 \___ \ | '_ \  / _` | / __|/ _ \   | | | '__|/ _` | / _` | / _ \| '__|
  ___) || |_) || (_| || (__|  __/   | | | |  | (_| || (_| ||  __/| |   
 |____/ | .__/  \__,_| \___|\___|   |_| |_|   \__,_| \__,_| \___||_|   
        |_|                                                            

 +-+ +-+ +-+ +-+ +-+   +-+ +-+ +-+   +-+ +-+ +-+ +-+ +-+ +-+
 |T| |r| |a| |d| |e|   |t| |h| |e|   |G| |a| |l| |a| |x| |y|
 +-+ +-+ +-+ +-+ +-+   +-+ +-+ +-+   +-+ +-+ +-+ +-+ +-+ +-+

 by MaKay Williams

'''

token = ''

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

print(f"{bcolors.HEADER}HEADER{bcolors.ENDC}")
print(f"{bcolors.OKBLUE}OKBLUE{bcolors.ENDC}")
print(f"{bcolors.OKCYAN}OKCYAN{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}OKGREEN{bcolors.ENDC}")
print(f"{bcolors.WARNING}WARNING{bcolors.ENDC}")
print(f"{bcolors.UNDERLINE}UNDERLINE{bcolors.ENDC}")


def display_title():
    print(title)

def authenticate_user():
    # get user api key to authenticate
    print("Please authenticate before using.")
    token = input("API Token: ")
    return token

def server_status():
    url = 'https://api.spacetraders.io/v2/'
    response = requests.get(url,)
    if response.status_code == 200:
        response_data = response.json()
        print(f"{bcolors.OKGREEN}{response_data['status']}{bcolors.ENDC}")
    else:
        print(f"{bcolors.WARNING}{response_data['status']}{bcolors.ENDC}")
        print('Error connecting to server. Program terminated.')
        sys.exit()
    return response_data['status']

def runMenu():
    while True:
        # print menu
        # wait for input
        pass
        sys.exit()
        
def new_user():
    # register a new user
    pass


def start_app():
    display_title()
    server_status()
    token = authenticate_user()
    print(token)
    print("you are authenticated!")
    runMenu()


start_app()