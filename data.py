from random import sample


def hash_password(password):
    return "".join(sample(password, len(password)))


class User:
    def __init__(self, email, password):
        self.__email = email
        self.__password = hash_password(password)

    @property
    def email(self):
        return self.__email
