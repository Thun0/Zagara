from poll import Poll
from dice import Dice

class Model:

    def __init__(self):
        self.poll = None
        self.message = ""
        self.poll_message = ""

    def create_poll(self, message):
        self.poll = Poll(message)
        self.poll_message = self.poll.get_message()
        return "@everyone\n" + self.get_poll_message()

    def roll_dice(self, message):
        sides = message.content[6:]
        if sides.isdigit and int(sides) > 0:
            val = Dice.roll(int(sides))
            return "Wyrzucono: " + str(val)

    def get_message(self):
        return self.message

    def get_poll_message(self):
        if self.poll is None:
            return "Obecnie nie trwa żadna ankieta"
        return self.poll_message

    def end_poll(self):
        if self.poll is None:
            return "Obecnie nie trwa żadna ankieta"
        self.poll = None
        return "@everyone Ankieta zakończona!\n" + self.poll_message[9:]

    def get_help_message(self):
        msg = "Dostępne komendy:\n"
        msg += "!help\t\t\t\t\t\t\t\t\t\t\t - wyświetla tę pomoc\n"
        msg += "!pollc pytanie;odp1;odp2;... \t - stworzenie ankiety\n"
        msg += "!poll \t\t\t\t\t\t\t\t\t\t\t  - wyświetlenie obecnie trwającej ankiety\n"
        msg += "!pollend\t\t\t\t\t\t\t\t\t\t  - zakończenie obecnej ankiety\n"
        msg += "!roll n\t\t\t\t\t\t\t\t\t\t\t- rzut n-ścienną kostką\n"
        return msg
