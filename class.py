#defining a class with attibute associated to function printing all strings in variables instantiated and called on later

#defining a class with init contructor and passing on attribute
class Song():
    def __init__(self,lyrics):
        self.lyrics = lyrics 

#defining a function printing all strings in attibute defined 
    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line) 

#Instantiating object 1
happy_bday = Song(["happy birthday to you","I don't want to get sued","So I'll stop right there"])

#Instantiating object 2
bulls_on_parade = Song(["the rally around the family","with pockets full of shells"])

#calling function through different objects created
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()     
