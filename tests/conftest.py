from selenium import webdriver
from config import URL, NAME
from locators import StellarBurgersRegisterLocators, StellarBurgersHomePageLocators, StellarBurgersLoginLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import get_password, get_email
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def signup(driver):
    driver.get(f'{URL}/register')

    email_data = get_email()
    email_password = get_password()

    driver.find_element(*StellarBurgersRegisterLocators.NAME_FAILED).send_keys(NAME)
    driver.find_element(*StellarBurgersRegisterLocators.EMAIL_FAILED).send_keys(email_data)
    driver.find_element(*StellarBurgersRegisterLocators.PASSWORD_FAILED).send_keys(email_password)
    driver.find_element(*StellarBurgersRegisterLocators.SUBMIT_BUTTON).click()

    return {"email": email_data, "password": email_password}


@pytest.fixture(scope="function")
def login(driver, signup):
    email_login = signup["email"]
    password_login = signup["password"]

    driver.get(URL)
    driver.find_element(*StellarBurgersHomePageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located
                                    (StellarBurgersLoginLocators.TITLE_FORM))

    driver.find_element(*StellarBurgersLoginLocators.EMAIL_FAILED).send_keys(email_login)
    driver.find_element(*StellarBurgersLoginLocators.PASSWORD_FAILED).send_keys(password_login)
    driver.find_element(*StellarBurgersLoginLocators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located
                                    (StellarBurgersHomePageLocators.CHECKOUT_BUTTON))
