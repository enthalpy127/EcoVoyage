class Customer():
    count_id = 0

    def __init__(self, first_name, last_name, gender, email, birthdate, address):
        Customer.count_id += 1
        self.__customer_id = ""
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__email = email
        self.__birthdate = birthdate
        self.__address = address


    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_gender(self, gender):
        self.__gender = gender

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_email(self, email):
        self.__email = email

    def set_birthdate(self, birthdate):
        self.__birthdate = birthdate

    def set_address(self, address):
        self.__address = address

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_customer_id(self):
        return self.__customer_id

    def get_email(self):
        return self.__email

    def get_birthdate(self):
        return self.__birthdate

    def get_address(self):
        return self.__address

