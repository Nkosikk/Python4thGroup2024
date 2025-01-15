import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/UserInformation.ini")


class ReadUserInformationProperties():

    def getFirstName(self):
        return config.get("UserInformation", "firstName")
    def getLastName(self):
        return config.get("UserInformation", "lastName")
