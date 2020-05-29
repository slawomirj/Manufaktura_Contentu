import pytest
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    failed_before = request.session.testsfailed
    yield
    if request.session.testsfailed != failed_before:
        when_fail = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.save_screenshot("screenshot_if_fail/"+ when_fail+".png")

    driver.quit()