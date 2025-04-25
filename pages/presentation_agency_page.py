from selenium.webdriver.common.by import By
from pages.base_page import Page

class PresentationAgencyPage(Page):

      PUBLISH_COMPANY_BUTTON=(By.CSS_SELECTOR,"[class*='publish-button']")

      def verify_page_open(self):
           self.verify_url(f'{self.base_url}/presentation-for-the-agency')
           print('presentation_agency_page')

      def verify_button_publish_my_company_is_available(self):
           self.wait_until_visible(*self.PUBLISH_COMPANY_BUTTON)