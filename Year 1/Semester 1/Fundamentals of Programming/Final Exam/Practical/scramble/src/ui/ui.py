class Ui:
    def __init__(self, controller):
        self.__controller = controller

    def gameplay(self):
        sentence = self.__controller.choose_sentence()
        output = self.__controller.shuffle(sentence)
        sentence_letters = list(sentence)
        score = len(sentence_letters)
        for letter in sentence_letters:
            if letter == " ":
                score -= 1
        print(f"Sentence: {output} [score is: {score}]")
        old_output = output
        while True:
            while True:
                try:
                    print()
                    command_string = input("> ")
                    print()
                    break
                except ValueError as ve:
                    print("Invalid command!", ve)
            command = command_string.split(" ")
            if len(command) > 3:
                if command[0] == "swap" and command[3] == "-":
                    if command[1].isnumeric() and command[2].isnumeric() and command[4].isnumeric() and command[5].isnumeric():
                        word1 = int(command[1])
                        letter1 = int(command[2])
                        word2 = int(command[4])
                        letter2 = int(command[5])
                        old_output = output
                        try:
                            output = self.__controller.swap(output, word1, letter1, word2, letter2)
                        except ValueError as ve:
                            print(ve)
                            continue
                        score -= 1
                        if output.strip() == sentence.strip():
                            print(f"Sentence: {output} [score is: {score}]")
                            print()
                            print("YOU WON!")
                            break
                        elif score == 0:
                            print(f"Sentence: {output} [score is: {score}]")
                            print()
                            print("YOU LOSE!")
                            break
                    else:
                        print("Invalid input for command swap!")
                        print()
                    print(f"Sentence: {output} [score is: {score}]")
            elif command[0] == "undo":
                output = old_output
                print(f"Sentence: {output} [score is: {score}]")
            else:
                print("Invalid command!")

    def run_menu(self):
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
                self.gameplay()
            elif option == 0:
                print("App exited successfully!")
                break
            else:
                print("Invalid option!")
