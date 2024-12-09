import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/loginDetails.ini")


class ReadLoginProperties():

    def getSauceDemoURL(self):
        return config.get("URLS", "sauceDemoURL")

