from selenium.webdriver.common.by import By


class StellarBurgersHeaderLocators: #Лакоторы для шапки сайта
    PERSONAL_AREA_BUTTON = (By.XPATH, "//header/nav/a[@href = '/account']")  # Кнопка "личный кабинет" в шапке
    LINK_LOGO = (By.XPATH, "//header/*/div[contains(@class,'AppHeader_header__logo')]/a")  # Логотип
    LINK_Constructor = (By.XPATH, "//p[text() = 'Конструктор']/parent::a")  # Ссылка на конструктор


class StellarBurgersRegisterLocators: #Лакоторы для страницы регистрации
    NAME_FAILED = (By.XPATH, '//fieldset[1]/div/div/input') # поле ввода имени
    EMAIL_FAILED = (By.XPATH, '//fieldset[2]/div/div/input') # поле ввода email
    PASSWORD_FAILED = (By.XPATH, '//fieldset[3]/div/div/input') # поле ввода пароля
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class,'button_button__33qZ0')]") # кнопка 'Зарегистрироваться'
    TEXT_ERROR = (By.XPATH, "//p[contains(@class,'input__error')]") # текст ошибки
    DIV_BORDER = (By.XPATH, "//fieldset[3]/*/div[contains(@class,'input_status_error')]") # Обёртка поля пароля
    LINK_ON_LOGIN = (By.XPATH, "//a[text() = 'Войти']") # Ссылка на страницу авторизации


class StellarBurgersLoginLocators: #Лакоторы для страницы авторизиции
    TITLE_FORM = (By.XPATH, "//h2[text()='Вход']") # Название формы авторизации
    EMAIL_FAILED = (By.XPATH, "//form/fieldset[1]/div/div/input[@name = 'name']") # поле ввода email
    PASSWORD_FAILED = (By.XPATH, "//form/fieldset[2]/div/div/input[@name = 'Пароль']") # поле ввода пароля
    BUTTON_LOGIN = (By.XPATH, "//button[text()= 'Войти']")  # кнопка 'Войти'


class StellarBurgersHomePageLocators: #Лакоторы для главной страницы
    LOGIN_BUTTON = (By.XPATH, "//section[2]/div/button[text()= 'Войти в аккаунт']") # Кнопка авторизации на главной странице
    CHECKOUT_BUTTON = (By.XPATH, "//section[2]/div/button[text()= 'Оформить заказ']") # Оформить заказ
    DIV_BUNS = (By.XPATH, "//span[text() = 'Булки']/parent::div")  # Тап раздела булки
    DIV_SAUCES = (By.XPATH, "//span[text() = 'Соусы']/parent::div") # Тап раздела соусы
    DIV_FILLINGS = (By.XPATH, "//span[text() = 'Начинки']/parent::div")  # Тап раздела начинки



class StellarBurgersForgotPasswordPageLocators: #Лакоторы для страницы восстановления пароля
    LINK_ON_LOGIN = (By.XPATH, "//a[text() = 'Войти']")  # Ссылка на страницу авторизации


class StellarBurgersProfileLocators: #Лакоторы для страницы личного кабинета
    BUTTON_EXIT = (By.XPATH, "//ul/li/button[contains(@class, 'Account_button__14Yp3')]") # Кнопка разлогина
