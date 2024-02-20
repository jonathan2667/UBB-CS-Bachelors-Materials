from services import Service
import random
class UI:
    def __init__(self):
        self.__service = Service()

    def print_players(self, players):
        for player in players:
            print(player)
        print()

    def run(self):

        while True:
            client_input = input("1.Display descending\n2.Play qualification rounds and play tournament")

            if client_input == "1":
                all_players_sorted_by_strength = self.__service.sort_players_by_strength()
                for player in all_players_sorted_by_strength:
                    print(player)
            elif client_input == "2":
                try:
                    all_players = self.__service.get_all_data()
                    if len(all_players) & (len(all_players) - 1) == 0:
                        print("No qualification needed!")
                    else:
                        players_that_play_qualification = self.__service.player_playing_qualification()
                        print("\nPlayer playing in qual round are:\n")
                        self.print_players(players_that_play_qualification)

                        players_wining_qualification = self.players_wining_qualification(players_that_play_qualification)

                        print("\nPlayers that won after qual are:\n")
                        self.print_players(players_wining_qualification)

                        print("Final list of players for tounament is:\n ")
                        tournament_players = self.__service.get_final_list_for_tournament(players_wining_qualification)
                        self.print_players(tournament_players)


                        print("Tournament begins!")
                        self.play_tournament(tournament_players)
                except Exception as ex:
                    print(str(ex))


            else:
                print("Invalid command!")

    def play_tournament(self, players):
        rounds = len(players)
        while rounds > 1:
            print("\nRound nr: " + str(int(rounds)) + "\n Players remaining are: \n")
            self.print_players(players)

            rounds = rounds / 2

            random.shuffle(players)
            winners = []
            for i in range(0, len(players), 2):
                print("\nCurrent game: " + str(players[i]) + " vs " + str(players[i + 1]) + "\n")

                client_input = input("1. Player 1 wins\n2.Player 2 wins\n")
                if client_input == "1":
                    players[i].strength += 1
                    winners.append(players[i])
                elif client_input == "2":
                    players[i + 1].strength += 1
                    winners.append(players[i + 1])
                else:
                    raise Exception("Invalid input.")

            players = winners

        print("\n\nWINNER IS : " + str(players[0]))


    def players_wining_qualification(self, players):
        random.shuffle(players)
        winners = []
        for i in range(0, len(players), 2):
            print("\nCurrent game: " + str(players[i]) + " vs " + str(players[i + 1]) + "\n")

            client_input = input("1. Player 1 wins\n2.Player 2 wins\n")
            if client_input == "1":
                players[i].strength += 1
                winners.append(players[i])
            elif client_input == "2":
                players[i + 1].strength += 1
                winners.append(players[i + 1])
            else:
                raise Exception("Invalid input.")
        return winners
