from datetime import datetime

class spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.chats=[]


class addchat:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy_admin = spy('Manan', 'Mr.', 19, 4.7)


friend_list = [spy('mridul','Mr.',20,3.8),spy('nitesh','Mr.',22,4.2)]
