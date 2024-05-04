from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import (StellarBurgersProfileLocators, StellarBurgersHeaderLocators, StellarBurgersHomePageLocators)
import pytest


@pytest.mark.usefixtures("login")
class TestStellarBurgersRedirect:

    def test_redirect_personal_account(self, driver):
        driver.find_element(*StellarBurgersHeaderLocators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located
                                        (StellarBurgersProfileLocators.BUTTON_EXIT))
        assert driver.current_url == f'{URL}/account/profile'

    def test_redirect_personal_account_in_constructor_click_constructor(self, driver):
        driver.find_element(*StellarBurgersHeaderLocators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located
                                        (StellarBurgersProfileLocators.BUTTON_EXIT))
        driver.find_element(*StellarBurgersHeaderLocators.LINK_Constructor).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located
                                        (StellarBurgersHomePageLocators.CHECKOUT_BUTTON))
        assert driver.current_url == f'{URL}/'

    def test_redirect_personal_account_in_constructor_click_logo(self, driver):
        driver.find_element(*StellarBurgersHeaderLocators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located
                                        (StellarBurgersProfileLocators.BUTTON_EXIT))
        driver.find_element(*StellarBurgersHeaderLocators.LINK_LOGO).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located
                                        (StellarBurgersHomePageLocators.CHECKOUT_BUTTON))
        assert driver.current_url == f'{URL}/'
