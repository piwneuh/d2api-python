from steam.client import SteamClient
from dota2.client import Dota2Client
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)

load_dotenv()
STEAM_USERNAME = os.getenv('STEAM_USERNAME')
STEAM_PASSWORD = os.getenv('STEAM_PASSWORD')

client = SteamClient()
dota = Dota2Client(client)
dota_ready = False

@client.on('logged_on')
def start_dota():
    print('Logged on')
    dota.launch()

@dota.on('ready')
def create_practice_lobby():
    global dota_ready
    dota_ready = True
    print('Dota is ready RADIIIII')

@dota.on('lobby_new')
def on_lobby_new():
    print('Lobby created')


@dota.on('lobby_invite')
def on_lobby_invite(steam_id):
    print(f'Invited to lobby by {steam_id}')

@dota.on('lobby_destroyed')
def on_lobby_destroyed():
    print('Lobby destroyed')

@dota.on('lobby_changed')
def on_lobby_changed():
    print('Lobby changed')