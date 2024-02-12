class Order:

    # initializer method
    def __init__(self, order_id, firstname, lastname, email, phone, airport, destination, departure, 
                 adults, children, cardnumber, cardholder, cardexpiry, cardsec, total_amount):
        self.__order_id = order_id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__phone = phone
        self.__airport = airport
        self.__destination = destination
        self.__departure = departure
        self.__adults = adults
        self.__children = children
        self.__cardnumber = cardnumber
        self.__cardholder = cardholder
        self.__cardexpiry = cardexpiry
        self.__cardsec = cardsec
        # self.__destination_price = destination_price
        self.__total_amount = total_amount

    # accessor methods
    def get_order_id(self):
        return self.__order_id

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_airport(self):
        return self.__airport

    def get_destination(self):
        return self.__destination

    def get_departure(self):
        return self.__departure

    def get_adults(self):
        return self.__adults

    def get_children(self):
        return self.__children

    def get_cardnumber(self):
        return self.__cardnumber

    def get_cardholder(self):
        return self.__cardholder

    def get_cardexpiry(self):
        return self.__cardexpiry

    def get_cardsec(self):
        return self.__cardsec

    # def get_destination_price(self):
    #     return self.__destination_price

    def get_total_amount(self):
        return self.__total_amount

    # mutator methods
    def set_order_id(self, order_id):
        self.__order_id = order_id

    def set_firstname(self, firstname):
        self.__firstname = firstname

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def set_email(self, email):
        self.__email = email

    def set_phone(self, phone):
        self.__phone = phone

    def set_airport(self, airport):
        self.__airport = airport

    def set_destination(self, destination):
        self.__destination = destination

    def set_departure(self, departure):
        self.__departure = departure

    def set_adults(self, adults):
        self.__adults = adults

    def set_children(self, children):
        self.__children = children

    def set_cardnumber(self, cardnumber):
        self.__cardnumber = cardnumber

    def set_cardholder(self, cardholder):
        self.__cardholder = cardholder

    def set_cardexpiry(self, cardexpiry):
        self.__cardexpiry = cardexpiry

    def set_cardsec(self, cardsec):
        self.__cardsec = cardsec

    # def set_destination_price(self, destination_price):
    #     self.__destination_price = destination_price

    def set_total_amount(self, total_amount):
        self.__total_amount = total_amount


def calculate_price(destination, num_adults, num_children):
    # Destination pricing data (inclusive of tax)
    prices = {
        # Denmark
        "Denmark": {
            "Givskud Zoo Zootopia": (250, 180),  # Adult, child price
            "The Ancient Viking Stronghold of Aros": (180, 120),
            "Tour with Odense River Cruise": (320, 240),
            "Street Art and Rooftops of Aarhus": (200, 150),
            "SUP - Stand Up Paddle - Kitesurfing - Wingfoil & Kitefoil courses": (350, 280),
            "Explore the Instaworthy Spots of Aarhus with a Local": (380, 300),
        },
        # Switzerland
        "Switzerland": {
            "Swiss National Park & Ofenpass Area Nature Trail": (300, 240),
            "Luke Lucerne Lake": (220, 160),
            "Mount Rigi": (400, 320),
            "Mount Pilatus Summit": (450, 360),
        },
        # Thailand
        "Thailand": {
            "Similan Islands": (500, 400),
            "Charuchak Park": (80, 60),
            "Bangkok Butterfly Garden and Insectarium": (120, 90),
            "Erawan Waterfall": (150, 100),
            "Bamboo Bicycle Tour in twilight": (200, 150),
            "Temple of the Golden Buddha": (100, 70),
        },
        # Singapore
        "Singapore": {
            "Garden by the bay": (150, 100),
            "Botanic Gardens": (80, 60),
            "Singapore Zoo": (200, 150),
            "Universal Studios": (350, 280),
            "S.E.A Aquarium": (220, 180),
        },
    }

    # print(prices)
    # for i in prices.values():
    #     print(f"{i}")
    #     if destination in i:
    #         print(f"{destination}, {prices[prices][destination]}")
    # if destination not in i:
    #     raise ValueError(f"Invalid destination: {destination}")

    for country, packages in prices.items():
        if destination in packages:
            price = packages[destination]  # Access price directly from current package
            print(f"Destination: {destination}, Price: {price}")
            break  # Stop iterating once found

        # Retrieve adult and child prices for the selected destination
    adult_price, child_price = price

    # Calculate total price based on group size
    total_price = (adult_price * num_adults) + (child_price * num_children)

    return adult_price, child_price, total_price



