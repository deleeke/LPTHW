class Lexicon(object):
    """Searches user input for words in lexicon and returns
    a tuple that classifies each known word with a type"""
    def __init__(self, directions,
                 verbs, stops, nouns):
        self.directions = directions.split()
        self.verbs = verbs.split()
        self.stops = stops.split()
        self.nouns = nouns.split()

    def findWord(self, word):
        wordList = [self.directions, self.verbs,
                    self.stops, self.nouns]
        wordListname = ['direction', 'verb',
                        'stop', 'noun']
        for i in range(0, len(wordList)):
            if word.lower() in wordList[i]:
                # checks each word list
                # if it is in the list, it returns a tuple
                # with the typename and the word
                return (wordListname[i], word.lower())

        # Now that it has checked all words in the lexicon,
        # check to see if word is actually a number
        return self.is_int(word)

    def is_int(self, s):
        try:
            int(s)
            return ('number', int(s))

        except ValueError:
            # if it is not a number
            return ('error', s)

    def scan(self, usrinput):
        splitInput = usrinput.split()
        returnList = []
        for word in splitInput:
             returnList.append(self.findWord(word))
        return returnList
