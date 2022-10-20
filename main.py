

class count:

    def __init__(self) :
        self.intcount=[]
        self.upstrcount=[]
        self.lowstrcount=[]
        self.othercount=[]

    def number(self,a):
        for i in a:
            if i.isdigit():
                self.intcount.append(i)
            elif i.isupper():
                self.upstrcount.append(i)
            elif i.islower():
                self.lowstrcount.append(i)
            else:
                self.othercount.append(i)
    def intnumber(self):
        return len(self.intcount)
    def upstrnumber(self):
        return len(self.upstrcount)
    def lownumber(self):
        return len(self.lowstrcount)
    def othernumber(self):
        return len(self.othercount)
    def outputintnumber(self):
        return tuple(self.intcount)
    def outputupstrnumber(self):
        return tuple(self.upstrcount)
    def outputlownumber(self):
        return tuple(self.lowstrcount)
    def outputothernumber(self):
        return tuple(self.othercount)