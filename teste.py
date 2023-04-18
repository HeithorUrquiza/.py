class User():
    def __init__(self, id=0):
        self.id = id
        
user1 = User()
print(user1.id)
user2 = User(2)
print(user2.id)