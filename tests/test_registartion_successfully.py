import pytest
import random
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import driver
from tests_locators import TestLocator

class Test_Registration:
    def test_avtorization_valid(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocator.SEARCH_Button_PersonalAccount).click() # переход к форме Авторизации
        driver.find_element(*TestLocator.OPEN_REGISTRATION_FORM).click() # переход к форме регистрации по кнопке Зарегестрироваться
        random_name = f"Lmiakush{random.randint(100, 999)}" # находим и вводим значение в поле Имя
        driver.find_element(*TestLocator.INPUT_NAME_FIELD).send_keys(
            random_name)
        random_email = f"Lmiakush{random.randint(100, 999)}@gmail.com" # находим и вводим значение в поле email
        driver.find_element(*TestLocator.INPUT_EMAIL_FIELD).send_keys(
            random_email)
        random_pass = f"Pass{random.randint(100, 999)}" # находим и вводим значение в поле Пароль
        driver.find_element(*TestLocator.INPUT_Pass_FIELD).send_keys(
            random_pass)
        driver.find_element(*TestLocator.BUTTON_REGISTRATION_SUBMIT).click() # завершаем регистрацию и кликаем на Зарегестрироваться
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]")))
        button = driver.find_element(*TestLocator.BUTTON_CHECK_IN)

        assert button.is_displayed(), "Кнопка 'Войти' не видна на странице."