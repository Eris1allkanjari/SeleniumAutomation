import celesi.constants as const
import os
from selenium import webdriver



class Celesi(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/Users/User/Desktop/Projects/SeleniumDriver",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Celesi, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def hap_faqen_kryesore(self):
        self.get(const.BASE_URL)

    def zgjidh_prona_te_patundshme(self):
        prona_te_patundshme_element = self.find_element_by_css_selector(
                'a[href="https://www.gazetacelesi.al/njoftime-kerko/prona-te-patundshme.html"]'
            )   
        prona_te_patundshme_element.click()   

    def hiq_popup(self,closeClass):
     try: 
       close_button_element = self.find_element_by_class_name(closeClass)
       close_button_element.click()
     except: 
         print("Popup nuk u gjet") 

    def hiq_popup2(self):
     try: 
       close_button_element = self.find_element_by_css_selector(
                'div.bhr-ip__c__close.ip-close-event.bhr-ip__c__close--3'
            )   
       close_button_element.click()
     except: 
         print("Popup nuk u gjet")       

    def menyra_kerkimit(self, veprimi):
        veprimi_field = self.find_element_by_css_selector(
             'select[data-place="Zgjidhni veprime"]'
         )
       
        veprimi_field.click()

    # def select_dates(self, check_in_date, check_out_date):
    #     check_in_element = self.find_element_by_css_selector(
    #         f'td[data-date="{check_in_date}"]'
    #     )
    #     check_in_element.click()

    #     check_out_element = self.find_element_by_css_selector(
    #         f'td[data-date="{check_out_date}"]'
    #     )
    #     check_out_element.click()

    # def select_adults(self, count=1):
    #     selection_element = self.find_element_by_id('xp__guests__toggle')
    #     selection_element.click()

    #     while True:
    #         decrease_adults_element = self.find_element_by_css_selector(
    #             'button[aria-label="Decrease number of Adults"]'
    #         )
    #         decrease_adults_element.click()
    #         #If the value of adults reaches 1, then we should get out
    #         #of the while loop
    #         adults_value_element = self.find_element_by_id('group_adults')
    #         adults_value = adults_value_element.get_attribute(
    #             'value'
    #         ) # Should give back the adults count

    #         if int(adults_value) == 1:
    #             break

    #     increase_button_element = self.find_element_by_css_selector(
    #         'button[aria-label="Increase number of Adults"]'
    #     )

    #     for _ in range(count - 1):
    #         increase_button_element.click()

    # def click_search(self):
    #     search_button = self.find_element_by_css_selector(
    #         'button[type="submit"]'
    #     )
    #     search_button.click()

    # def apply_filtrations(self):
    #     filtration = BookingFiltration(driver=self)
    #     filtration.apply_star_rating(4, 5)

    #     filtration.sort_price_lowest_first()

