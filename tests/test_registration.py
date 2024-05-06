from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL, NAME, INVALID_PASSWORD
from locators import StellarBurgersRegisterLocators, StellarBurgersLoginLocators
from data import get_email


class TestStellarBurgersRegistration:

    def test_signup(self, driver, signup):
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
            StellarBurgersLoginLocators.TITLE_FORM))
        assert driver.current_url == f'{URL}/login'

    def test_error_invalid_password(self, driver):
        driver.get(f'{URL}/register')
        email_data = get_email()
        driver.find_element(*StellarBurgersRegisterLocators.NAME_FAILED).send_keys(NAME)
        driver.find_element(*StellarBurgersRegisterLocators.EMAIL_FAILED).send_keys(email_data)
        driver.find_element(*StellarBurgersRegisterLocators.PASSWORD_FAILED).send_keys(INVALID_PASSWORD)
        driver.find_element(*StellarBurgersRegisterLocators.SUBMIT_BUTTON).click()
        text_error = driver.find_element(*StellarBurgersRegisterLocators.TEXT_ERROR)
        assert text_error.is_displayed() and ('input_status_error' in driver.find_element(
            *StellarBurgersRegisterLocators.DIV_BORDER).get_attribute('class'))
