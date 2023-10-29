class Text:

    def __init__(self, text):
        self.__text = text

    def lenText(self):
        return len(self.__text)

    def countLetter(self):
        count = 0

        for i in self.__text:
            if i.isalpha():
                count += 1

        return count

    def countSpace(self):
        count = 0

        for i in self.__text:
            if i == " ":
                count += 1

        return count

    def lenWithoutSpace(self):
        count = 0

        for i in self.__text:
            if i != " ":
                count += 1

        return count

    def textToMassiveByWord(self):

        self.__massive = self.__text.split()

        return self.__massive

    def textToMassiveBySentece(self):

        self.__massive = self.__text.split(".")

        return self.__massive