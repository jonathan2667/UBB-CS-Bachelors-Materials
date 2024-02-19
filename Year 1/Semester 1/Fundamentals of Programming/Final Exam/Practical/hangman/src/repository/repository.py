class Repository:
    def __init__(self):
        self.__all_sentences = []

    def get_all(self):
        """
        :return: the list of all sentences
        """
        return self.__all_sentences

    def add(self, sentence):
        """
        Adds a new sentence to the repository, raises a ValueError if the sentence exists
        :param sentence: string, the sentence that is added
        :return: nothing
        """
        if sentence in self.__all_sentences:
            raise ValueError("Sentence already exists!")
        self.__all_sentences.append(sentence)
