import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def browser_setup(request):
    driver = webdriver.Firefox()
    request.cls.driver = driver
    yield driver
    driver.quit()
