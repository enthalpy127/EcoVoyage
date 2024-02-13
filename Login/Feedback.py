class Feedback:

    def __init__(self, name, star_rating, title, message, date_submitted):
        self.name = name
        self.star_rating = int(star_rating)
        self.title = title
        self.message = message
        self.date_submitted = date_submitted


    def __str__(self):
        return 'Feedback Obj'