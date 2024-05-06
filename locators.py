from selenium.webdriver.common.by import By


class StellarBurgersHeaderLocators: #Лакоторы для шапки сайта
    PERSONAL_AREA_BUTTON = (By.XPATH, "//a[.='Личный Кабинет']")  # Кнопка "личный кабинет" в шапке
    LINK_LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]/a")  # Логотип
    LINK_Constructor = (By.XPATH, "//p[text() = 'Конструктор']/parent::a")  # Ссылка на конструктор


class StellarBurgersRegisterLocators: #Лакоторы для страницы регистрации
    NAME_FAILED = (By.XPATH, "//label[text() = 'Имя']/following::input[1]") # поле ввода имени
    EMAIL_FAILED = (By.XPATH, "//label[text() = 'Email']/following::input[1]") # поле ввода email
    PASSWORD_FAILED = (By.XPATH, "//input[@name = 'Пароль']") # поле ввода пароля
    SUBMIT_BUTTON = (By.XPATH, "//button[text()= 'Зарегистрироваться']") # кнопка 'Зарегистрироваться'
    TEXT_ERROR = (By.XPATH, "//p[contains(@class,'input__error')]") # текст ошибки
    DIV_BORDER = (By.XPATH, "//div[contains(@class,'input_status_error')]") # Обёртка поля пароля
    LINK_ON_LOGIN = (By.XPATH, "//a[text() = 'Войти']") # Ссылка на страницу авторизации


class StellarBurgersLoginLocators: #Лакоторы для страницы авторизиции
    TITLE_FORM = (By.XPATH, "//h2[text()='Вход']") # Название формы авторизации
    EMAIL_FAILED = (By.XPATH, "//input[@name = 'name']") # поле ввода email
    PASSWORD_FAILED = (By.XPATH, "//input[@name = 'Пароль']") # поле ввода пароля
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
