from steam.client import SteamClient
from dota2.client import Dota2Client
from dotenv import load_dotenv
import os
import time

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
    get_lobby_list = dota.get_lobby_list()
    print(get_lobby_list)

print('Logging in...')
print("Username: ", STEAM_USERNAME)
print("Password: ", STEAM_PASSWORD)
client.cli_login(username=STEAM_USERNAME, password=STEAM_PASSWORD)
client.run_forever()