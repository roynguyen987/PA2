from src.tournament import Tournament
from server import Server

class ServerApplication:
    # Runs the server
    tournament = Tournament("", "", "")
    server = Server(10003, 7)
    server.run_server()

