class Ui:
    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def menu():
        print("         WELCOME TO HANGMAN")
        print()
        print("----------------MENU----------------")
        print()
        print("1 - Add a new sentence that can be played")
        print("2 - Play the game")
        print("0 - Exit")

    def add_sentence(self):
        """
        Verifies the input such that it contains at least 3 chars
        :return: nothing
        """
        try:
            sentence = input("Enter the new sentence: ")
            if len(sentence) < 3:
                print("Length must be greater than 3!")
                return
        except ValueError as ve:
            print("Invalid input!", ve)
            return
        try:
            self.__controller.add(sentence)
        except ValueError as ve:
            print(ve)

    def gameplay(self):
        """
        The game itself:
        - a random sentence is chosen by the computer
        - only the first and the last letters along with all their appearances are sown initially
        - the user needs to guess letters
        - the game end either by guessing the whole sentence or by mistaken until the word "hangman" is formed
        :return: nothing
        """
        sentence = self.__controller.choose_sentence()
        output = ""
        hangman = ""
        game_over = "hangman"
        end_counter = 0
        for letter in sentence:
            if letter == sentence[0]:
                output += letter
            elif letter == sentence[-1]:
                output += letter
            elif letter == " ":
                output += " "
            else:
                output += "_"
        print(f"Sentence: {output} - Status: {hangman}")
        while True:
            while True:
                try:
                    choice = input("Enter your guess: ")
                    if len(choice) != 1:
                        print("Input must be 1 character!")
                        break
                    break
                except ValueError as ve:
                    print("Invalid input!", ve)
            i = 1
            sentence_letters = list(sentence)
            output_letters = list(output)
            new_output = ""
            if choice not in sentence_letters or choice in output_letters:
                hangman += game_over[end_counter]
                end_counter += 1
            elif choice in sentence_letters:
                for i in range(len(sentence_letters)):
                    if sentence_letters[i] == choice:
                        output_letters[i] = choice
            for i in range(len(output_letters)):
                new_output += output_letters[i]
            output = new_output
            print(f"Your guess: '{choice}'  Sentence: {output} - Status: {hangman}")
            print()
            if hangman == "hangman":
                print("YOU LOST! GAME OVER!")
                break
            if output == sentence:
                print("YOU WIN! GAME OVER!")
                break

    def run_app(self):
        self.menu()
        while True:
            while True:
                try:
                    print()
                    option = int(input("Enter your option: "))
                    print()
                    break
                except ValueError as ve:
                    print("Invalid option!", ve)
            if option == 1:
                self.add_sentence()
            elif option == 2:
                self.gameplay()
            elif option == 0:
                print("App exited successfully!")
                break
            else:
                print("Invalid option!")
