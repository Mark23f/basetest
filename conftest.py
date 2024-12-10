from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
@pytest.fixture()
def browser():
    options = Options()
    # Запуск Chrome не используя UI
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3)   #Неявное ожидание
    yield browser
    browser.close()