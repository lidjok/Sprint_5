import pytest
import random
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import driver
from tests_locators import TestLocator
from tests_locators import Test_burger_designer_locators

class Test_designer_transfer_to_breads_sauces_fillings:
    def test_designer_transfer_to_sauces(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Test_burger_designer_locators.BUTTON_MENU_SAUCES).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG tab_tab_type_current__2BEPc') and span[text()='Соусы']]")))


    def test_designer_transfer_to_breads(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Test_burger_designer_locators.BUTTON_MENU_FILLINGS).click()
        driver.find_element(*Test_burger_designer_locators.BUTTON_MENU_BREADS).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                          "//div[contains(@class, 'tab_tab__1SPyG tab_tab_type_current__2BEPc') and span[text()='Булки']]")))
    def test_designer_transfer_to_fillings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Test_burger_designer_locators.BUTTON_MENU_FILLINGS).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                          "//div[contains(@class, 'tab_tab__1SPyG tab_tab_type_current__2BEPc') and span[text()='Начинки']]")))
