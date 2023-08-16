import configparser
config= configparser.RawConfigParser()

config.read("E:\\Automation Project\\credence\\Configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def getUrl():
        Url = config.get('common info', 'URL')
        return Url

    @staticmethod
    def getEmail():
        Email = config.get('common info', 'Email')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get('common info', 'Password')
        return Password

    @staticmethod
    def getFirstname():
        Firstname = config.get('common info', 'First_Name')
        return Firstname

    @staticmethod
    def getLastname():
        Lastname = config.get('common info', 'Last_Name')
        return Lastname


