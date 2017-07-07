class Poll:

    def create(self, message):
        command = message.content[7:]
        self.question = command.split(';')[0]
        self.options = command.split(';')[1:]
        self.votes = [0 for i in range(len(self.options))]
        self.voters = [[] for i in range(len(self.options))]
        if len(self.options) > 20:
            return "Za duzo opcji w ankiecie!"
        else:
            return "@everyone\n\n" + self.get_poll_message()

    def vote(self, message):
        options = message.content[6:]
        for opt in options:
            idx = ord(opt) - 97
            if idx < 0 or idx > len(self.options):
                return "Niepoprawny glos"
        caster = message.author
        for opt in options:
            idx = ord(opt)-97
            if caster not in self.voters[idx]:
                self.votes[idx] += 1
                self.voters[idx].append(caster)
        return "Oddano głos(y) na: " + options


    def get_poll_message(self):
        msg = "Ankieta: "
        msg += self.question
        msg += "\n"
        for i in range(len(self.options)):
            msg += ":regional_indicator_"
            msg += chr(i+97)
            msg += ": "
            msg += self.options[i]
            msg += "\n"
        return msg

    def get_results(self):
        msg = self.get_poll_message()
        msg += "\n"
        for i in range(len(self.options)):
            msg += ":regional_indicator_"
            msg += chr(i + 97)
            msg += ": "
            msg += str(self.votes[i])
            msg += ": "
            for voter in self.voters[i]:
                msg += voter.name
                msg += ", "
            msg = msg[:-2]
            msg += "\n"
        return msg