class Message:

    def __init__(self, number):
        self.number = number

    def content(self):
        return "MSG%d" % self.number

    def increment(self):
        self.number += 1
