from abc import abstractmethod, ABC

class Logger(ABC):

    @abstractmethod
    def log(self, message, level):
        ...

    def info(self, message, level):
        print(message)

class FileLogger(Logger):

    def log(self, message, level):
        print(f"Message{message} level{level}")

class DataBaseLogger(Logger):

    def log(self, message, level):
        print(f"Loggin to Database. Message{message} level{level}")