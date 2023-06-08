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

'''

def read_token():
    try:
        with open("token.txt", "r") as file:
            token = file.read().strip()
            return token
    except FileNotFoundError:
        print("Please authenticate by putting token into token.txt file.")
        exit()

headers = {
    "Authorization": f"Bearer {read_token()}",
}


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
# print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

# print(f"{bcolors.HEADER}HEADER{bcolors.ENDC}")
# print(f"{bcolors.OKBLUE}OKBLUE{bcolors.ENDC}")
# print(f"{bcolors.OKCYAN}OKCYAN{bcolors.ENDC}")
# print(f"{bcolors.OKGREEN}OKGREEN{bcolors.ENDC}")
# print(f"{bcolors.WARNING}WARNING{bcolors.ENDC}")
# print(f"{bcolors.UNDERLINE}UNDERLINE{bcolors.ENDC}")

base_url = 'https://api.spacetraders.io/v2/'

def display_title():
    print(title)

def authenticate_user():
    try:
        with open("token.txt", "r") as file:
            token = file.read().strip()
    except FileNotFoundError:
        print("Please authenticate by putting token into token.txt file.")
        exit()

    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = "https://api.spacetraders.io/v2/my/ships"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Authentication successful. Continuing program...")
    else:
        print("Authentication failed. Please check your token.")
        exit()

def server_status():
    # url = 'https://api.spacetraders.io/v2/'
    response = requests.get(base_url)
    if response.status_code == 200:
        response_data = response.json()
        print(f"{bcolors.OKGREEN}{response_data['status']}{bcolors.ENDC}")
    else:
        print(f"{bcolors.WARNING}{response_data['status']}{bcolors.ENDC}")
        print('Error connecting to server. Program terminated.')
        sys.exit()
    return response_data['status']

def get_input():
    response = input(">")
    return response

def view_ships(ship_id=None):
    url = f"{base_url}my/ships"
    if ship_id is not None:
        url += f"/{ship_id}"
    response = requests.get(url, headers=headers)
    print(response)
    print(url)
    if response.status_code == 200:
        # Process and display ship details
        ship_details = response.json()
        if isinstance(ship_details, list):
            for ship in ship_details:
                # Display ship information
                print(ship)
        else:
            # Display ship information
            print(ship_details)
    else:
        print("Error retrieving ship details.")


def print_menu():
    menu = '''\n
    Space Traders Terminal Application - Help

    Welcome to the Space Traders Terminal Application! This application allows you to interact with the Space Traders API and manage your space trading operations. Below are the available commands and their usage:

    help: Displays the help information for the terminal application.

    Example: help
    view ships [options]: Displays information about your ships.

    Options:
    --all: Display all ship details.
    --ship <ship_id>: Display details for a specific ship.
    Example:
    view ships: Displays basic ship details for all your ships.
    view ships --all: Displays all ship details for all your ships.
    view ships --ship ABC123: Displays all details for the ship with ID ABC123.
    view docked: Displays a list of ships currently docked at your location.

    Example: view docked
    buy cargo <ship_id> <good> <quantity>: Buys a specified quantity of cargo for a ship.

    Example: buy cargo ABC123 water 10
    sell cargo <ship_id> <good> <quantity>: Sells a specified quantity of cargo from a ship.

    Example: sell cargo ABC123 water 5
    view transit: Displays a list of ships currently in transit and their estimated time of arrival.

    Example: view transit
    time left <ship_id>: Displays the estimated time left for a ship to reach its destination.

    Example: time left ABC123
    exit: Exits the terminal application.

    Example: exit
    Please note that <ship_id> refers to the unique identifier of your ship, and <good> refers to the type of cargo you want to buy or sell.

    Feel free to explore the features of the Space Traders Terminal Application and reach out if you have any further questions or need assistance! Happy trading!
    '''
    print(menu)

def runMenu():
    while True:
        user_input = get_input().lower()  # Read user input
        tokens = user_input.split()  # Split input into tokens
        command = tokens[0]  # Identify the command
        if command == "help":
            print_menu()
        elif command == "view":
            if len(tokens) > 1 and tokens[1] == "ships":
                if "--all" in tokens:
                    view_ships()
                elif "--ship" in tokens:
                    ship_id = tokens[tokens.index("--ship") + 1]
                    view_ships(ship_id)
                else:
                    # Invalid or incomplete command
                    print("Invalid command. Please specify '--all' or '--ship <ship_id>'.")
            elif len(tokens) > 1 and tokens[1] == "docked":
                # Execute code to view docked ships
                pass
            elif len(tokens) > 1 and tokens[1] == "transit":
                # Execute code to view ships in transit
                pass
            else:
                # Invalid command
                print("Invalid command. Please use 'view ships', 'view docked', or 'view transit'.")
        elif command == "buy":
            # Handle 'buy' command
            pass
        elif command == "sell":
            # Handle 'sell' command
            pass
        elif command == "time":
            # Handle 'time' command
            pass
        elif command == "exit":
            break  # Exit the loop to end the program
        else:
            # Invalid command
            print("Invalid command. Please try again or type 'exit' to quit.")
            # sys.exit()
        
def new_user():
    # register a new user
    pass

def start_app():
    
    server_status()
    token = authenticate_user()
    display_title()
    runMenu()


start_app()