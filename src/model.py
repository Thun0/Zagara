from poll import Poll
from dice import Dice

class Model:

    def __init__(self):
        self.poll = None

    def create_poll(self, message):
        self.poll = Poll()
        return self.poll.create(message)

    def roll_dice(self, message):
        sides = message.content[6:]
        if sides.isdigit and int(sides) > 0:
            val = Dice.roll(int(sides))
            return "Wyrzucono: " + str(val)

    def get_poll_message(self):
        if self.poll is None:
            return "Obecnie nie trwa żadna ankieta"
        return self.poll.get_results()

    def end_poll(self):
        if self.poll is None:
            return "Obecnie nie trwa żadna ankieta"
        msg = "@everyone Ankieta zakończona!\n\n" + self.poll.get_results()[9:]
        self.poll = None
        return msg

    def get_help_message(self):
        msg = "Dostępne komendy:\n"
        msg += "!help\t\t\t\t\t\t\t\t\t\t\t - wyświetla tę pomoc\n"
        msg += "!pollc pytanie;odp1;odp2;... \t - stworzenie ankiety\n"
        msg += "!poll \t\t\t\t\t\t\t\t\t\t\t  - wyświetlenie obecnie trwającej ankiety\n"
        msg += "!pollend\t\t\t\t\t\t\t\t\t\t  - zakończenie obecnej ankiety\n"
        msg += "!roll n\t\t\t\t\t\t\t\t\t\t\t- rzut n-ścienną kostką\n"
        return msg
