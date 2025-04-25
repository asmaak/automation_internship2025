from selenium.webdriver.common.by import By
from pages.base_page import Page

class MarketPage(Page):
    COMPANY_BUTTON=(By.CSS_SELECTOR,"[class*='add-company-button']")
    def verify_market_page(self):
        self.verify_url(f'{self.base_url}/market-companies')

    def click_company_button(self):
        self.wait_until_clickable_click(*self.COMPANY_BUTTON)
        # self.click(*self.COMPANY_BUTTON)
        print('company_button',self.COMPANY_BUTTON)