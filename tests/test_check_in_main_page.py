import pytest
import random
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import driver
from tests_locators import TestLocator
from tests_locators import Test_recover_form_locators

class Test_Check_in:
    def test_Check_in_main_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocator.SEARCH_Button_PersonalAccount).click()  # переход к форме Авторизации
        driver.find_element(
            *TestLocator.OPEN_REGISTRATION_FORM).click()  # переход к форме регистрации по кнопке Зарегестрироваться
        random_name = f"Lmiakush{random.randint(100, 999)}"  # находим и вводим значение в поле Имя
        driver.find_element(*TestLocator.INPUT_NAME_FIELD).send_keys(
            random_name)
        random_email = f"Lmiakush{random.randint(100, 999)}@gmail.com"  # находим и вводим значение в поле email
        driver.find_element(*TestLocator.INPUT_EMAIL_FIELD).send_keys(
            random_email)
        random_pass = f"Pass{random.randint(100, 999)}"  # находим и вводим значение в поле Пароль
        driver.find_element(*TestLocator.INPUT_Pass_FIELD).send_keys(
            random_pass)
        driver.find_element(*TestLocator.BUTTON_REGISTRATION_SUBMIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]")))
        time.sleep(6)

        driver.find_element(*TestLocator.BUTTON_LOGO_RETURN_MAIN).click()
        driver.find_element(*TestLocator.BUTTON_MAIN_ENTER_ACC).click() # клик по Войти в аккаунт на главной странице

        driver.find_element(*TestLocator.INPUT_AVTORIZATION_EMAIL).send_keys(random_email)  # заполняем форму авторизации
        driver.find_element(*TestLocator.INPUT_AVTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*TestLocator.BUTTON_AVTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))

    def test_Check_in_Through_Perconal_Acc(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocator.SEARCH_Button_PersonalAccount).click()  # переход к форме Авторизации
        driver.find_element(
            *TestLocator.OPEN_REGISTRATION_FORM).click()  # переход к форме регистрации по кнопке Зарегестрироваться
        random_name = f"Lmiakush{random.randint(100, 999)}"  # находим и вводим значение в поле Имя
        driver.find_element(*TestLocator.INPUT_NAME_FIELD).send_keys(
            random_name)
        random_email = f"Lmiakush{random.randint(100, 999)}@gmail.com"  # находим и вводим значение в поле email
        driver.find_element(*TestLocator.INPUT_EMAIL_FIELD).send_keys(
            random_email)
        random_pass = f"Pass{random.randint(100, 999)}"  # находим и вводим значение в поле Пароль
        driver.find_element(*TestLocator.INPUT_Pass_FIELD).send_keys(
            random_pass)
        driver.find_element(*TestLocator.BUTTON_REGISTRATION_SUBMIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                          "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]")))
        driver.find_element(*TestLocator.BUTTON_LOGO_RETURN_MAIN).click()
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(*TestLocator.INPUT_AVTORIZATION_EMAIL).send_keys(
            random_email)  # заполняем форму авторизации
        driver.find_element(*TestLocator.INPUT_AVTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*TestLocator.BUTTON_AVTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))

    def test_Check_in_Through_Check_in_Form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocator.SEARCH_Button_PersonalAccount).click()  # переход к форме Авторизации
        driver.find_element(
            *TestLocator.OPEN_REGISTRATION_FORM).click()  # переход к форме регистрации по кнопке Зарегестрироваться
        random_name = f"Lmiakush{random.randint(100, 999)}"  # находим и вводим значение в поле Имя
        driver.find_element(*TestLocator.INPUT_NAME_FIELD).send_keys(
            random_name)
        random_email = f"Lmiakush{random.randint(100, 999)}@gmail.com"  # находим и вводим значение в поле email
        driver.find_element(*TestLocator.INPUT_EMAIL_FIELD).send_keys(random_email)
        random_pass = f"Pass{random.randint(100, 999)}"  # находим и вводим значение в поле Пароль
        driver.find_element(*TestLocator.INPUT_Pass_FIELD).send_keys(random_pass)
        driver.find_element(*TestLocator.BUTTON_REGISTRATION_SUBMIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                          "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]")))
        driver.find_element(*TestLocator.INPUT_AVTORIZATION_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocator.INPUT_AVTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*TestLocator.BUTTON_AVTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))

    def test_Check_in_Through_Recover_Password_Form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocator.SEARCH_Button_PersonalAccount).click()  # переход к форме Авторизации
        driver.find_element(*TestLocator.OPEN_REGISTRATION_FORM).click()  # переход к форме регистрации по кнопке Зарегестрироваться
        random_name = f"Lmiakush{random.randint(100, 999)}"  # находим и вводим значение в поле Имя
        driver.find_element(*TestLocator.INPUT_NAME_FIELD).send_keys(
            random_name)
        random_email = f"Lmiakush{random.randint(100, 999)}@gmail.com"  # находим и вводим значение в поле email
        driver.find_element(*TestLocator.INPUT_EMAIL_FIELD).send_keys(random_email)
        random_pass = f"Pass{random.randint(100, 999)}"  # находим и вводим значение в поле Пароль
        driver.find_element(*TestLocator.INPUT_Pass_FIELD).send_keys(random_pass)
        driver.find_element(*TestLocator.BUTTON_REGISTRATION_SUBMIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                          "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]")))
        driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']")))

        driver.find_element(*Test_recover_form_locators.BUTTON_RECOVER_PASSWORD_FORM_CHECK_IN).click()
        driver.find_element(*TestLocator.INPUT_AVTORIZATION_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocator.INPUT_AVTORIZATION_PASS).send_keys(random_pass)
        driver.find_element(*TestLocator.BUTTON_AVTORIZATION_CHECK_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))