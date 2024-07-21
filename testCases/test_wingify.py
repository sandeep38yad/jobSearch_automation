from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from PageObjects.WingifyCareers import wingifyPage
from selenium.webdriver.common.by import By
from utilities.customLogger import Logger
from utilities.readProperties import wingifyConfig

baseUrl = wingifyConfig.getbaseURL()
logger = Logger.get_logger('Wingify')
urls = []


@pytest.mark.usefixtures("browser_setup")
class Test_001_career:

    def test_pageOpening(self):
        try:
            self.driver.get(baseUrl)
            logo = WebDriverWait(self.driver, 30).until(
                ec.presence_of_element_located((By.XPATH, wingifyConfig.getlogoXpath())))

            if logo:
                print("Career page opened successfully")
                logger.info("Career page opened successfully")
                assert True
            else:
                print("Failed to open career page")
                logger.info("Failed to open career page")
                assert False
        except Exception as e:
            print(f"Error in test_pageOpening: {str(e)}")
            logger.error(f"Error in test_pageOpening: {str(e)}")
            assert False


    def test_countVacancy(self):
        try:
            self.obj = wingifyPage(self.driver)
            count = self.obj.OpenPositionsCount()
            if count > 0:
                print("Openings found for QA role")
                logger.info("Openings found for QA role")
                assert True
            else:
                print("NO openings found for QA role")
                logger.info("NO openings found for QA role")
                assert False
        except Exception as e:
            print(f'Error in test_countVacancy: {str(e)}')
            logger.error(f'Error in test_countVacancy: {str(e)}')

    def test_fetchLinks(self):
        try:
            self.obj1 = wingifyPage(self.driver)
            global urls
            urls = self.obj1.collectLinks()
            if len(urls) > 0:
                print(f"Links: {urls}")
                logger.info(f"Links: {urls}")
                assert True
            else:
                assert False
        except Exception as e:
            print(f'Error in test_fetchLinks: {str(e)}')
            logger.error(f'Error in test_fetchLinks: {str(e)}')

    def test_getdetails(self):
        try:
            self.obj2 = wingifyPage(self.driver)
            flag = -1
            global urls
            for url in urls:
                result = self.obj2.getDetails(url)
                if len(result) > 0:
                    print(result)
                    logger.info(result)
                    flag += 1

            if flag != -1:
                assert True
            else:
                assert False

        except Exception as e:
            print(f'Error in test_getdetails:{str(e)}')
            logger.error(f'Error in test_getdetails:{str(e)}')









