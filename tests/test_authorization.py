from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import (StellarBurgersHomePageLocators, StellarBurgersLoginLocators, StellarBurgersRegisterLocators,
                      StellarBurgersForgotPasswordPageLocators, StellarBurgersHeaderLocators,
                      StellarBurgersProfileLocators)


class TestStellarBurgersLogin:

    def test_login_to_home(self, driver, signup):
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
        assert (driver.current_url == f'{URL}/' and driver.find_element(
                                                        *StellarBurgersHomePageLocators.CHECKOUT_BUTTON).is_displayed())

    def test_login_to_personal_area_button(self, driver, signup):
        email_login = signup["email"]
        password_login = signup["password"]
        driver.get(URL)
        driver.find_element(*StellarBurgersHeaderLocators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
                                                StellarBurgersLoginLocators.TITLE_FORM))
        driver.find_element(*StellarBurgersLoginLocators.EMAIL_FAILED).send_keys(email_login)
        driver.find_element(*StellarBurgersLoginLocators.PASSWORD_FAILED).send_keys(password_login)
        driver.find_element(*StellarBurgersLoginLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
                                                                        StellarBurgersHomePageLocators.CHECKOUT_BUTTON))
        assert (driver.current_url == f'{URL}/' and driver.find_element(
                                                        *StellarBurgersHomePageLocators.CHECKOUT_BUTTON).is_displayed())

    def test_login_button_on_registration_form(self, driver, signup):
        email_login = signup["email"]
        password_login = signup["password"]
        driver.get(f'{URL}/register')
        driver.find_element(*StellarBurgersRegisterLocators.LINK_ON_LOGIN).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
                                                                                StellarBurgersLoginLocators.TITLE_FORM))
        driver.find_element(*StellarBurgersLoginLocators.EMAIL_FAILED).send_keys(email_login)
        driver.find_element(*StellarBurgersLoginLocators.PASSWORD_FAILED).send_keys(password_login)
        driver.find_element(*StellarBurgersLoginLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
                                                                        StellarBurgersHomePageLocators.CHECKOUT_BUTTON))
        assert driver.current_url == f'{URL}/' and driver.find_element(
                                                        *StellarBurgersHomePageLocators.CHECKOUT_BUTTON).is_displayed()

    def test_login_button_on_forgot_password(self, driver, signup):
        email_login = signup["email"]
        password_login = signup["password"]
        driver.get(f'{URL}/forgot-password')
        driver.find_element(*StellarBurgersForgotPasswordPageLocators.LINK_ON_LOGIN).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
                                                                                StellarBurgersLoginLocators.TITLE_FORM))
        driver.find_element(*StellarBurgersLoginLocators.EMAIL_FAILED).send_keys(email_login)
        driver.find_element(*StellarBurgersLoginLocators.PASSWORD_FAILED).send_keys(password_login)
        driver.find_element(*StellarBurgersLoginLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
                                                                        StellarBurgersHomePageLocators.CHECKOUT_BUTTON))
        assert driver.current_url == f'{URL}/' and driver.find_element(
                                                        *StellarBurgersHomePageLocators.CHECKOUT_BUTTON).is_displayed()


class TestStellarBurgersLoginOut:

    def test_log_out(self, driver, login):
        driver.find_element(*StellarBurgersHeaderLocators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located
                                        (StellarBurgersProfileLocators.BUTTON_EXIT))
        driver.find_element(*StellarBurgersProfileLocators.BUTTON_EXIT).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
                                                                                StellarBurgersLoginLocators.TITLE_FORM))
        assert driver.current_url == f'{URL}/login' and driver.find_element(
                                                                *StellarBurgersLoginLocators.TITLE_FORM).is_displayed()



