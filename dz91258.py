class WordLengthIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        length = len(self.words[self.index])
        self.index += 1
        return length

words = ['Blabla', 'sea', 'Step']
iterator = WordLengthIterator(words)

for length in iterator:
    print(length)
