class person(object):
    def __init__(self, richness, name):
        self.richness = richness
        self.next_person = None
        self.next_rich = None
        self.counselor = False
        self.name = name

    def add_next(self, person):
        self.next_person = person

    def add_next_rich(self, person):
        self.next_rich = person

    def __str__(self):
        return self.name + "(" + str(self.richness) + ", " + str(self.counselor) + ")"


class queue(object):
    def __init__(self, person):
        self.first = person
        self.last = person
        self.counseled = person
        if person != None:
            self.first.counselor = True

    def pop(self):
        r = self.first
        self.first.next_rich.counselor = True
        self.first = self.first.next_person
        return r

    def add(self, person):
        if person == None:
            return
        else:
            self.last.add_next(person)
            self.last = person
            if person.richness >= self.counseled.richness:
                self.counseled.counselor = False
                person.counselor = True
                self.counseled = person
                print 0, person
                return
            else:
                self.current = self.counseled
                while self.current.next_rich != None and self.current.richness > person.richness:
                    self.current = self.current.next_rich
                self.current.add_next_rich(person)
                print 1, person

    def __str__(self):
        p = self.first
        while p != None:
            print p
            p = p.next_person
        return ''


bob = person(2, "bob")
rob = person(11, "rob")
alice = person(7, "alice")
laure = person(5, "laure")
frank = person(12, "frank")
marie = person(9, "marie")
ned = person(6, "ned")

bank = queue(bob)
bank.add(rob)
bank.add(alice)
bank.add(laure)
bank.add(frank)
bank.add(marie)
bank.add(ned)

print bank