from threading import Thread
from api import app, client, STEAM_PASSWORD, STEAM_USERNAME

if __name__ == '__main__':
    client.cli_login(username=STEAM_USERNAME, password=STEAM_PASSWORD)
    app.run(host="0.0.0.0", port=5000, debug=True)