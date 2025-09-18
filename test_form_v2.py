import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from form_page_v2 import FormPageV2

testdata = {
    "name": "Auto Bot",
    "password": "Secr3t!",
    "drink": "Coffee",
    "color": "Blue",
    "automation": "yes",
    "email": "bot@automate.now",
    "message": "Selenium + Pytest = ❤"
}

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        wd = webdriver.Chrome(service=ChromeService())
    else:
        wd = webdriver.Firefox(service=FirefoxService())
    wd.maximize_window()
    yield wd
    wd.quit()

def test_fill_and_submit(driver):
    page = FormPageV2(driver)
    page.open()
    page.fill_form(testdata)
    page.submit()
    assert page.is_success_alert_present(), "Не появился alert об успехе"
    page.close_alert()