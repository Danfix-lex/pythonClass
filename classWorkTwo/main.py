class Chief:
    def greeting(self):
        return "You bloody whips"

class Chibuzo:
    def greeting(self):
        return "People of God"

class Femi:
    def greeting(self):
        return "How una dey?"

class SK:
    def greeting(self):
        return "Sho wa okay?"

class Chinedu:
    def greeting(self):
        return "Oh, you don't say?"

class Dapo:
    def greeting(self):
        return "I saw Dele yesterday"

chibuzo = Chibuzo()

for chibuzo in [Chief(), Chibuzo(), Femi(), Chinedu(), SK(), Dapo()]:
    print(chibuzo.greeting())