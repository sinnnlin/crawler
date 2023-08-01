from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class Crawler():
    def __init__(self, use_webdriver, browser='Edge') -> None:
        self.webdriver = use_webdriver
        self.browser = webdriver.Edge(self.webdriver)
    
    def visit(self, url):
        if self.browser:
            self.browser.get(url)
        else:
            print("provide a workable webdriver.")
    
    def maximize_window(self):
        self.browser.maximize_window()
            
    def fill_in(self, target, text, timeout=5):
        WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(('xpath', target)))
        self.browser.find_element(By.XPATH, target).send_keys(text)
        
    def click(self, button,time_sleep=5):
        WebDriverWait(self.browser,time_sleep).until(EC.element_to_be_clickable(('xpath',button)))
        self.browser.find_element(By.XPATH, button).click()
        
    def press_enter(self):
        webdriver.ActionChains(self.browser).send_keys(Keys.ENTER).perform()
    
    def read_text(self, target, timeout=5):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(('xpath', target)))
        text = self.browser.find_element(By.XPATH, target).text
    
    def drop_down_menu(self, target, timeout=5):  
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(('xpath', target)))
        select_element = Select(self.browser.find_element(By.XPATH, target))
        all_text = []
        for i in select_element.options:
            all_text.append(i.text)
        return all_text
    def select_drop_down_menu(self, target,option, timeout=5):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(('xpath', target)))
        select_element = Select(self.browser.find_element(By.XPATH, target))
        select_element.select_by_visible_text(option)
    
    def scroll_down(self):
        time.sleep(10)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
    def switch_window(self,num=1):
        self.browser.switch_to.window(self.browser.window_handles[num])
    def close(self):
        self.browser.close()


        
        
if __name__ == '__main__':
    TEST = Crawler('./data/msedgedriver.exe')
    TEST.visit('https://e-service.cwb.gov.tw/HistoryDataQuery/')
    TEST.maximize_window()
    city_list = TEST.drop_down_menu("/html/body/div[1]/div/div[2]/form/div[1]/div[2]/div[2]/table/tbody/tr[1]/td/select")
    print(city_list)
    TEST.select_drop_down_menu("/html/body/div[1]/div/div[2]/form/div[1]/div[2]/div[2]/table/tbody/tr[1]/td/select",city_list[1])
    
    # # TEST.click("/html/body/div[2]/div/nav/div/div[1]/div/div/div[1]/ul[1]/li[2]/a/span")
    # TEST.fill_in('/html/body/header/div[2]/div/div/div[1]/div[1]/div[1]/div/form/input[1]', 'Python')
    # # TEST.click('/html/body/header/div[2]/div/div/div[1]/div[1]/div[1]/div/form/div[2]/button')
    # TEST.press_enter()
    time.sleep(5)