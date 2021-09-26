from selenium import webdriver
import booking.constants as const
import os

class Booking(webdriver.Chrome):

    def __init__(self, driver_path= os.pathsep + "C:\chromedriver_win32", teardown=False):
        self.teardown = teardown
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    
    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element_by_css_selector(
            'a[data-modal-header-async-url-param*="selected_currency={}"]'.format(currency)
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_css_selector(
            'input[aria-label="Type your destination"]'
        )
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element_by_css_selector(
            'label[for="xp__guests__input"]'
        )
        selection_element.click()

        while True:

            number_of_adults_frame = self.find_element_by_id("group_adults")

            number_of_adults = number_of_adults_frame.get_attribute('value')

            if int(number_of_adults) < count:

                adults_increase_button = self.find_element_by_css_selector(
                    'button[aria-label="Increase number of Adults"]'
                )

                for times in range(0, count - int(number_of_adults)):

                    adults_increase_button.click()

                    break

            if int(number_of_adults) > count:

                adults_decrease_button = self.find_element_by_css_selector(
                    'button[aria-label="Decrease number of Adults"]'
                )

                for times in range(0, 0, count - int(number_of_adults)):

                    adults_decrease_button.click()

                    break











        