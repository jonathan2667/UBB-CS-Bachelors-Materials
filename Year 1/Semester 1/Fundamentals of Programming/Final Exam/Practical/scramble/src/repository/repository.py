class Repository:
    def __init__(self):
        self.__all_sentences = []
        self.__file_name = "D:\\_DOCUMENTE_RARES\\Desktop\\Semester 1\\Fundamentals of Programming\\Training\\Last Year Subjects\\scramble\\sentences"
        self.__load_data()

    def get_all(self):
        return self.__all_sentences

    def __load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                line = line.strip()
                try:
                    self.add(line)
                except ValueError:
                    continue

    def add(self, sentence):
        if sentence in self.get_all():
            raise ValueError("Sentence already exists!")
        self.__all_sentences.append(sentence)
        with open(self.__file_name) as f:
            f.write(sentence + "\n")
