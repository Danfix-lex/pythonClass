print("Welcome to your Nokia Phone!");
print("To start please Select an option:");
def menu(Call):
    match call:
        case 1:
            return "dialing number!!!"
def menu(message):
    match message:
        case 1:
            message_center = input("Enter your message: ")
            print("Sending Message!!!")
        case 2:
            return "message_settings"
    def message(message_settings):
                    match message_settings:
                        case 1:
                            return "set1"
                    def message_settings(set1):
                                    match set1:
                                        case 1:
                                            return "message center number"
                                        case 2:
                                            return "message sent as"
                                        case 3:
                                            return "message validity"
        case 2:
                            return "common"
                                def message_settings(common):
                                    match common:
                                        case 1:
                                            return "delivery reports"
                                        case 2:
                                            return "reply via same center"
                                        case 3:
                                            return "character support"
                                        case 4:
                                            return "info service"
                                        case 5:
                                            return "voice mailbox number"
                                        case 6:
                                            return "service command editor"
def menu(contacts):
    match contacts:
        case 1:
            return "Sensie"
        case 2:
            return "Fame"
        case 3:
            return "SK"
def menu(settings):
    match settings:
        case 1:
            return "adjust brightness"
        case 2:
            return "adjust sound"
        case 3:
            return "security"
        case 4:
            return "restore factory settings"
def menu(clock):
    match clock:
        case 1:
            return "adjust time"
        case 2:
            return "adjust date"
        case 3:
            return "set alarm"
        case 4:
            return "stop watch"
        case 5:
            return "time tracker"
def menu(chat):
    match chat:
        case 1:
            return "facebook"
        case 2:
            return "opera mini"
        case 3:
            return "2go"
        case 4:
            return "ebbudy"
        case 5:
            return "message"
def menu(call_register):
    match call_register:
        case 1:
            return "missed calls"
        case 2:
            return "dialled calls"
        case 3:
            return "received calls"
        case 4:
            return "call settings"
        case 5:
            return "blacklisted numbers"
        case 6
            return "whitelisted numbers"
def menu(games):
    match games:
        case 1:
            return "snake"
        case 2:
            return "ludo"
        case 3:
            return "X & O"
        case 4:
            return "GTA V"
        case 5:
            return "asphat 1"
        case 6:
            return "prince of persia"
def menu(tone):
    match tone:
        case 1:
            return "change tone settings"
        case 2:
            return "adjust tone settings"
        case 3:
            return "increase tone volume"
        case 4:
            return "decrease tone volume"
        case 5:
            return "change tone"
        case 6:
            return "vibration settings"
        case 7:
            return "mute"
def menu(exit):
    match exit:
        case 1:
            return "exiting..."
