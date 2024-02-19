import random


class Controller:
    def __init__(self, repository):
        self.__repository = repository

    def return_all(self):
        return self.__repository.get_all()

    def choose_sentence(self):
        sentences = self.return_all()
        sentence = random.choice(sentences)
        return sentence

    @staticmethod
    def shuffle(sentence):
        output = ""
        sentence_words = sentence.split(" ")
        for word in sentence_words:
            word_letters = list(word)
            output += word_letters[0]
            del word_letters[0]
            last_letter = word_letters[-1]
            del word_letters[-1]
            random.shuffle(word_letters)
            for letter in word_letters:
                output += letter
            output += last_letter
            output += " "
        return output

    @staticmethod
    def swap(output, word1, letter1, word2, letter2):
        output_words = output.split(" ")
        if letter1 == 0 or letter1 == len(output_words[word1]) - 1 or letter2 == 0 or letter2 == len(
                output_words[word2]) - 1:
            raise ValueError("Index cannot be first or last character!")
        auxiliary = output_words[word1][letter1]
        output_words[word1] = output_words[word1][:letter1] + output_words[word2][letter2] + output_words[word1][
                                                                                             letter1 + 1:]
        output_words[word2] = output_words[word2][:letter2] + auxiliary + output_words[word2][
                                                                          letter2 + 1:]
        return " ".join(output_words)
