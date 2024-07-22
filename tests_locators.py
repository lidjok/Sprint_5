import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import driver

class TestLocator:

    SEARCH_Button_PersonalAccount = By.LINK_TEXT, "Личный Кабинет"
    OPEN_REGISTRATION_FORM = By.CLASS_NAME, "Auth_link__1fOlj"
    INPUT_NAME_FIELD = By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']"
    INPUT_EMAIL_FIELD = By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']"
    INPUT_Pass_FIELD = By.XPATH, "//label[text()='Пароль']/following-sibling::input[@name='Пароль']"
    BUTTON_REGISTRATION_SUBMIT = By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]"
    BUTTON_CHECK_IN = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]"
    BUTTON_LOGO_RETURN_MAIN = By.CLASS_NAME, "AppHeader_header__logo__2D0X2"
    BUTTON_MAIN_ENTER_ACC = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"
    INPUT_AVTORIZATION_EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']"
    INPUT_AVTORIZATION_PASS = By.CSS_SELECTOR, "input[name='Пароль']"
    BUTTON_AVTORIZATION_CHECK_IN = By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa"
    BUTTON_MAIN_PAIG_MAKE_ORDER = By.XPATH, "//button[contains(text(), 'Оформить заказ')]"
    BUTTON_LINK_DISIGNER_HEADER = By.LINK_TEXT, "Конструктор"

class Test_burger_designer_locators:

    BUTTON_MENU_SAUCES = By.XPATH, "//span[text()='Соусы']"
    BUTTON_MENU_FILLINGS = By.XPATH, "//span[text()='Начинки']"
    BUTTON_MENU_BREADS = By.XPATH, "//span[text()='Булки']"

class Test_recover_form_locators:
    BUTTON_RECOVER_PASSWORD_FORM_CHECK_IN = By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']"