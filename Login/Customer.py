import uuid
from Login import User


def generate_random_id():
    # Generate a random UUID (version 4)
    random_id = uuid.uuid4()

    # Convert the UUID to a string and remove hyphens
    id_str = str(random_id).replace('-', '')

    return id_str


class Customer(User.User):
    count_id = 0

    def __init__(self, username, first_name, last_name, gender, membership, email, date_joined, address, password):
        #super().__init__(first_name, last_name, gender, membership='F', remarks='')
        Customer.count_id += 1  # This shit is useless
        self.__username = username
        self.__customer_id = generate_random_id()
        self.__email = email
        self.__date_joined = date_joined
        self.__address = address
        self.__password = password


    def set_username(self, username):
        self.__username = username

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_email(self, email):
        self.__email = email

    def set_date_joined(self, date_joined):
        self.__date_joined = date_joined

    def set_address(self, address):
        self.__address = address

    def set_password(self, password):
        self.__password = password


    def get_username(self):
        return self.__username

    def get_customer_id(self):
        return self.__customer_id

    def get_email(self):
        return self.__email

    def get_date_joined(self):
        return self.__date_joined

    def get_address(self):
        return self.__address

    def get_password(self):
        return self.__password
