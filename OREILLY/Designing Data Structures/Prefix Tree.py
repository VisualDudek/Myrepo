
wordkey = '\n'  #Nie rozumiem tego zastosowania DONE EVERNOTE

class PrefixTree:
    def __init__(self, *start):
        self.head = {}

        for x in start:
            self.add(x.lower())

    def add(self, value):
        """Add value to prefix tree,
        Return TRUE if updated
        poprzez value mozemy przekazywac slowa"""
        d = self.head

        #sprawdzam czy dana litera jest juz w slowniku
        while len(value) > 0:
            c = value[0]
            if c not in d:
                d[c] = {}

            d = d[c]
            value = value[1:]

        if wordkey in d:
            return False

        d[wordkey] = True
        return True

    def __contains__(self, item):   # pozwala na używanie 'in' np.  ('inch' in d)
        """Determine if item in prefix tree"""
        d = self.head
        while len(item) > 0:
            c = item[0]
            if c not in d:   #Juz nna tym etapie moge rozpoznać czy dane slowo jest w PT dlategu 'not in' zamiast 'in'
                return False

            d = d[c]
            item = item[1:]
        #return True ŹLE np. w PT jest już inch a my szukamu in
        return wordkey in d   #Sprytnie zapisane
