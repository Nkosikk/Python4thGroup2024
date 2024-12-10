import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/loginDetails.ini")


class ReadLoginProperties():

    def getSauceDemoURL(self):
        return config.get("URLS", "sauceDemoURL")

    def getUsername(self):
        return config.get("Login Details", "username")

    def getPassword(self):
        return config.get("Login Details", "password")

