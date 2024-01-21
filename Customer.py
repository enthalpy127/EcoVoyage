class Customer():
    count_id = 0

    def __init__(self, first_name, last_name,gender, membership, remarks, email, date_joined, address,username,password):
        Customer.count_id += 1
        self.__customer_id = Customer.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__email = email
        self.__date_joined = date_joined
        self.__address = address
        self.__membership = membership
        self.__remarks = remarks
        self.__username = username
        self.__password = password


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

    def set_date_joined(self, date_joined):
        self.__date_joined = date_joined

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

    def get_date_joined(self):
        return self.__date_joined

    def get_address(self):
        return self.__address
    def get_password(self):
        return self.__password
    def get_username(self):
        return self.__username
    def get_remarks(self):
        return self.__remarks
    def get_membership(self):
        return self.__membership

