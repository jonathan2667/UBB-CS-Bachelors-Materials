from domain import Player
class Repository():
    def __init__(self):
        self.__all_players = []
        self.get_from_text_file_repo()
    def get_all_players_repo(self):
        return self.__all_players

    def add_player_repo(self, player):
        self.__all_players.append(player)

    def get_from_text_file_repo(self):
        with open("src/tennis.txt", 'r') as file:
            rows = file.readlines()
        for row in rows:
            (id, name, strength) = [item.strip() for item in row.split(",")]
            self.add_player_repo(Player(int(id), name, int(strength)))
