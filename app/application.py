from pages.base_page import Page
from pages.main_page import MainPage
from pages.log_in_page import LogInPage
from pages.side_menu_page import SideMenuPage
from pages.market_page import MarketPage
from pages.presentation_agency_page import PresentationAgencyPage


class Application:
    def __init__(self,driver):
        self.driver=driver
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.log_in_page =LogInPage(driver)
        self.side_menu_page = SideMenuPage(driver)
        self.market_page = MarketPage(driver)
        self.presentation_agency_page = PresentationAgencyPage(driver)