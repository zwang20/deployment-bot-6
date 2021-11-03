
class Permisions():
    def __init__(self):
        self.administrator = False


class User():
    def __init__(self):
        self.id = "0"
        self.name = "Tester"
        self.discriminator = "1234"
        self.admin = False

    def permmisions_in(self, *args, **kwargs):
        return Permisions()


class Message():
    def __init__(self):
        self.author = User()
        self.channel = "0"
