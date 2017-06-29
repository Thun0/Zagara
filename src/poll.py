import string

class Poll:

    def __init__(self, message):
        self.message = ""
        command = message.content[7:]
        self.question = command.split(';')[0]
        self.options = command.split(';')[1:]
        print("There are {} options in poll".format(len(self.options)))
        if len(self.options) > 20:
            self.message = "Za duzo opcji w ankiecie!"
        else:
            self.create_poll_message()

    def get_message(self):
        return self.message

    def create_poll_message(self):
        self.message = "Ankieta: "
        self.message += self.question
        self.message += "\n"
        for i in range(len(self.options)):
            self.message += ":regional_indicator_"
            self.message += string.ascii_lowercase[i]
            self.message += ": "
            self.message += self.options[i]
            self.message += "\n"
