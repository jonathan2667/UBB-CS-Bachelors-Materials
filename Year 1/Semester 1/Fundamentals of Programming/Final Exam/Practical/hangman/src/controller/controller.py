import random


class Controller:
    def __init__(self, repository):
        self.__repository = repository

    def return_all(self):
        """
        :return: the list of all sentences
        """
        return self.__repository.get_all()

    def add(self, sentence):
        """
        Adds a new sentence
        :param sentence: string, a sentence that is passed to be added to the repository
        :return: nothing
        """
        self.__repository.add(sentence)

    def choose_sentence(self):
        """
        Picks a random sentence form the list of sentences
        :return: the chosen sentence
        """
        sentences = self.return_all()
        sentence = random.choice(sentences)
        return sentence

