import configparser
config = configparser.RawConfigParser()
config.read(r'.\configurations\config.ini')

class wingifyConfig:

    @staticmethod
    def getbaseURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getlogoXpath():
        logo = config.get('page1 info', 'logoXpath')
        return logo

    @staticmethod
    def getQaID():
        qaid = config.get('page1 info', 'qaID')
        return qaid

    @staticmethod
    def getQaXpath():
        qaXpath = config.get('page1 info', 'qaXpath')
        return qaXpath

    @staticmethod
    def getjobTitleXpath():
        jobTitleXpath = config.get('page2 info', 'jobTitleXpath')
        return jobTitleXpath

    @staticmethod
    def getbannerXpath():
        bannerXpath = config.get('page2 info', 'bannerXpath')
        return bannerXpath

    @staticmethod
    def getjobType():
        jobType = config.get('page2 info', 'jobType')
        return jobType

    @staticmethod
    def getlocationXpath():
        locationXpath = config.get('page2 info', 'locationXpath')
        return locationXpath

    @staticmethod
    def getexperienceXpath():
        experienceXpath = config.get('page2 info', 'experienceXpath')
        return experienceXpath

