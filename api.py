import time
from flask import Flask, jsonify, request
from events import *

app = Flask(__name__)

@app.post('/create-lobby')
def create_lobby():
    try:
        req = request.json
        password = req.get('password') or '1234'
        game_name = req.get('game_name') or 'relative'
        server_region = req.get('server_region') or 3

        print('Destroying previous lobby...')
        print(dota.destroy_lobby())

        print('Sleeping for 5 seconds...')
        time.sleep(5)

        print('Creating lobby...')
        dota.create_practice_lobby(password=password, options={'game_name': game_name, 'server_region': server_region})

        # Going to spectator mode
        dota.join_practice_lobby_team(1, 3)
        time.sleep(5)

        # Adding bot
        dota.add_bot_to_practice_lobby()

        return jsonify({'message': 'Lobby created'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.post('/destroy-lobby')
def destroy_lobby():
    try:
        print('Destroying lobby...')
        dota.destroy_lobby()
        return jsonify({'message': 'Lobby destroyed'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.post('/invite-players')
def invite_players():
    try:
        req = request.json
        steam_ids = req.get('steam_ids')

        print('Inviting players...')
        for steam_id in steam_ids:
            print(f'Inviting {steam_id}...')
            dota.invite_to_lobby(steam_id)
            time.sleep(5)

        return jsonify({'message': 'Players invited'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.post('/start-game')
def start_game():
    try:
        print('Starting game...')
        dota.launch_practice_lobby()
        time.sleep(5)
        dota.abandon_current_game()
        return jsonify({'message': 'Game started'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    