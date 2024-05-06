from config import URL
from locators import StellarBurgersHomePageLocators


class TestTransitionsInConstructor:
    def test_transition_to_sauces(self, driver):
        driver.get(URL)
        driver.find_element(*StellarBurgersHomePageLocators.DIV_SAUCES).click()
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(
            *StellarBurgersHomePageLocators.DIV_SAUCES).get_attribute('class')

    def test_transition_to_fillings(self, driver):
        driver.get(URL)
        driver.find_element(*StellarBurgersHomePageLocators.DIV_FILLINGS).click()
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(
            *StellarBurgersHomePageLocators.DIV_FILLINGS).get_attribute('class')

    def test_transition_to_buns(self, driver):
        driver.get(URL)
        driver.find_element(*StellarBurgersHomePageLocators.DIV_FILLINGS).click()
        driver.find_element(*StellarBurgersHomePageLocators.DIV_BUNS).click()
        assert ('tab_tab_type_current__2BEPc' in driver.find_element(*StellarBurgersHomePageLocators.DIV_BUNS)
                .get_attribute('class'))
