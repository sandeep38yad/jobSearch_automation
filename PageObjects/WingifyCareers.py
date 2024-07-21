from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.readProperties import wingifyConfig
import time

class wingifyPage:
    def __init__(self, driver):
        self.driver = driver

    def OpenPositionsCount(self):
        time.sleep(3)
        position = self.driver.find_element(By.ID, wingifyConfig.getQaID())
        count = position.find_elements(By.XPATH, wingifyConfig.getQaXpath())
        return len(count)

    def collectLinks(self):
        position = self.driver.find_element(By.ID, wingifyConfig.getQaID())
        roles = position.find_elements(By.TAG_NAME, 'a')
        links = []
        for role in roles:
            links.append(role.get_attribute('href'))
        return links

    def getDetails(self, url):
        result =[]
        self.driver.get(url)
        self.driver.implicitly_wait(3)
        jobTitle = self.driver.find_element(By.XPATH, wingifyConfig.getjobTitleXpath()).text
        banner = self.driver.find_element(By.XPATH, wingifyConfig.getbannerXpath())
        jobtype = banner.find_element(By.XPATH, wingifyConfig.getjobType()).text
        location = banner.find_element(By.XPATH, wingifyConfig.getlocationXpath()).text
        experience = banner.find_element(By.XPATH, wingifyConfig.getexperienceXpath()).text
        result.append(jobTitle)
        result.append(jobtype)
        result.append(location)
        result.append(experience)
        return result
