class Scanner(object):

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
            if word in wordList[i]:
                print word, 'is in', wordListname[i]
                return (wordListname[i], word)

        print 'check to see if word is actually a number'
        return self.is_int(word)

    def is_int(self, s):
        try:
            int(s)
            return ('number', s)

        except ValueError:
            return ('error', s)

    def scan(self, usrinput):
        usrinput = usrinput.lower().split()
        for word in usrinput:
            print self.findWord(word)

lexicon = Scanner('north south east west',
                  'go kill eat',
                  'the in of then',
                  'bear princess witch mage warrior')
