from selenium.webdriver.common.by import By

from pages.base_page import Page
from time import sleep
class SideMenuPage(Page):

    MARKET_LINK=(By.CSS_SELECTOR,"[href='/market-companies']")

    def click_menu(self,name_menu):
        self.wait_until_clickable_click(*self.MARKET_LINK)
        print('menu',name_menu)
        sleep(8)
