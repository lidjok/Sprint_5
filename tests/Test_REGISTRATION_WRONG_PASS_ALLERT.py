import pytest
import random
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import driver
from tests_locators import TestLocator

class Test_Avtorisation:
    def test_avtorization_not_valid(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocator.SEARCH_Button_PersonalAccount).click() # переход к форме Авторизации
        driver.find_element(*TestLocator.OPEN_REGISTRATION_FORM).click() # переход к форме регистрации по кнопке Зарегестрироваться
        random_pass = f"P{random.randint(100, 999)}"  # находим и вводим значение в поле Пароль
        driver.find_element(*TestLocator.INPUT_Pass_FIELD).send_keys(random_pass)  # вводим пароль в 4 символа
        driver.find_element(*TestLocator.BUTTON_REGISTRATION_SUBMIT).click()  # подтверждаем регистрацию и вызываем ошибку кликм по Зарегестрироваться
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")))

        error_message = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")))
        assert error_message.is_displayed()