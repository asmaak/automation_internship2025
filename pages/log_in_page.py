from selenium.webdriver.common.by import By

from pages.base_page import Page

from time import sleep
class LogInPage(Page):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD =(By.ID, 'field')
    CONTINUO_FIELD=(By.CSS_SELECTOR,"a[wized='loginButton']")

    def log_in(self,email,password):
        sleep(8)
        # self.wait_until_visible(*self.EMAIL_FIELD)
        self.input_text(email,*self.EMAIL_FIELD)
        # self.wait_until_visible(*self.PASSWORD_FIELD)
        self.input_text(password,*self.PASSWORD_FIELD)
        self.click(*self.CONTINUO_FIELD)
        print('email',email)
        print('password',password)


