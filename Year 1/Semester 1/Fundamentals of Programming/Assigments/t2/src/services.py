from repository import Repository
import random
class Service:
    def __init__(self):
        self.__data = Repository()

    def get_all_data(self):
        return self.__data.get_all_players_repo()

    def sort_players_by_strength(self):
        all_players = self.get_all_data()
        for i in range(len(all_players)):
            for j in range(i + 1, len(all_players)):
                if all_players[i].strength < all_players[j].strength:
                    all_players[i], all_players[j] = all_players[j], all_players[i]
        return all_players

    def smaller_power_of_2(self, number ):
        power = 1
        while power * 2 <= number:
            power = power * 2
        return power


    def player_playing_qualification(self):
        all_players_sorted_increasing = self.sort_players_by_strength()
        all_players_sorted_increasing.reverse()

        total_players_allowed = (len(self.get_all_data()) - self.smaller_power_of_2(len(self.get_all_data()))) * 2
        player_that_play_qualification = all_players_sorted_increasing[0:total_players_allowed]
        return player_that_play_qualification

    def get_final_list_for_tournament(self, players_wining_qualification):
        all_players_sorted_increasing = self.sort_players_by_strength()
        all_players_sorted_increasing.reverse()
        total_players_allowed = (len(self.get_all_data()) - self.smaller_power_of_2(len(self.get_all_data()))) * 2

        strongest_players = all_players_sorted_increasing[total_players_allowed:len(self.get_all_data())]

        for player in players_wining_qualification:
            strongest_players.append(player)

        return strongest_players

    def get_random_pairings(self, players):
        """

        :param players: The list of all players
        :return: Using random function, we randomize the players
        """
        return random.shuffle(players)