from steam.client import SteamClient
from dota2.client import Dota2Client
from dotenv import load_dotenv
import os
import time
import logging

# Set up logging
logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)

# Load the environment variables
load_dotenv()
STEAM_USERNAME = os.getenv('STEAM_USERNAME')
STEAM_PASSWORD = os.getenv('STEAM_PASSWORD')


client = SteamClient()
dota = Dota2Client(client)

@client.on('logged_on')
def start_dota():
    dota.launch()

@dota.on('ready')
def create_practice_lobby():
    print('Destroying previous lobby...')
    print(dota.destroy_lobby())

    print('Sleeping for 5 seconds...')
    time.sleep(5)

    print('Creating lobby...')
    dota.create_practice_lobby(password='1234', options={'game_name':'Relative', 'server_region':3})

    # Make sure the lobby is created before we start adding players
    print('Sleeping for 5 seconds...')
    time.sleep(5)

    print('Lobby created')
    print(dota.lobby)

    print('Adding players...')
    dota.invite_to_lobby(steam_id=76561198176726223)


@dota.on('lobby_changed')
def lobby_changed(lobby):
    print('Lobby changed')
    print(lobby)

    print('Sleeping for 5 seconds...')
    time.sleep(5)

    dota.launch_practice_lobby()
    

print('Logging in...')
print("Username: ", STEAM_USERNAME)
print("Password: ", STEAM_PASSWORD)
client.cli_login(username=STEAM_USERNAME, password=STEAM_PASSWORD)
client.run_forever()