from models.rank_model import RankModel


class UserModel:
    def __init__(self):
        self.__id = 1
        self.__username = "John Doe"
        self.__email = "johndoe1111@gmail.com"
        self.__rank = RankModel(453)

    @property
    def id(self):
        return self.__id
    
    @property
    def username(self):
        return self.__username
    
    @property
    def email(self):
        return self.__email
    
    @property
    def rank(self):
        return self.__rank.current_rank
    
    def update_username(self, new_username):
        self.__username = new_username
        return True
    
    def update_email(self, new_email):
        self.__email = new_email
        return True
    
if __name__ == "__main__":
    test_user = UserModel()

    print(test_user.id)
    print(test_user.username)
    print(test_user.email)

    test_user.update_username("janedoe1313")
    test_user.update_email("janedoe1313@gmail.com")

    print(test_user.id)
    print(test_user.username)
    print(test_user.email)