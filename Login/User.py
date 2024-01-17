import uuid


def generate_random_id():
    # Generate a random UUID (version 4)
    random_id = uuid.uuid4()

    # Convert the UUID to a string and remove hyphens
    id_str = str(random_id).replace('-', '')

    return id_str


class User:
    count_id = 0

    # initializer method
    def __init__(self, first_name, last_name, gender, membership, remarks, password=''):
        User.count_id += 1 # This shit is useless
        self.__user_id = generate_random_id()
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__membership = membership
        self.__remarks = remarks
        self.__password = password

    # accessor methods
    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_membership(self):
        return self.__membership

    def get_remarks(self):
        return self.__remarks

    def get_password(self):
        return self.__password

    # mutator methods
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_gender(self, gender):
        self.__gender = gender

    def set_membership(self, membership):
        self.__membership = membership

    def set_remarks(self, remarks):
        self.__remarks = remarks

    def set_password(self, password):
        self.__password = password
