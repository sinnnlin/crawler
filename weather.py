from crawler import Crawler
import time

driver = Crawler('./data/msedgedriver.exe')
driver.visit('https://e-service.cwb.gov.tw/HistoryDataQuery/')
driver.maximize_window()
city_list = driver.drop_down_menu("/html/body/div[1]/div/div[2]/form/div[1]/div[2]/div[2]/table/tbody/tr[1]/td/select")
print(city_list)
place_dict = {}
for city in city_list:
    driver.select_drop_down_menu("/html/body/div[1]/div/div[2]/form/div[1]/div[2]/div[2]/table/tbody/tr[1]/td/select",city)
    node_list = driver.drop_down_menu("/html/body/div[1]/div/div[2]/form/div[1]/div[2]/div[2]/table/tbody/tr[2]/td/select")
    place_dict[city] = node_list
print(place_dict) 
# for city,node in place_dict.items():
#     driver.select_drop_down_menu("/html/body/div[1]/div/div[2]/form/div[1]/div[2]/div[2]/table/tbody/tr[1]/td/select",city)
#     for each_node in node:
#         time.sleep(5)
#         driver.select_drop_down_menu("/html/body/div[1]/div/div[2]/form/div[1]/div[2]/div[2]/table/tbody/tr[2]/td/select",each_node)
#         time.sleep(5)
#         driver.select_drop_down_menu("/html/body/div[1]/div/div[2]/form/div[1]/div[2]/div[2]/table/tbody/tr[4]/td/select","日報表 (daily data)")
#         driver.select_drop_down_menu("/html/body/div[1]/div/div[2]/form/div[1]/div[2]/div[2]/table/tbody/tr[4]/td/select","月報表 (monthly data)")
#         driver.fill_in('/html/body/div[1]/div/div[2]/form/div[1]/div[2]/div[2]/table/tbody/tr[5]/td/input','2023-07')
#         driver.click("/html/body/div[1]/div/div[2]/form/div[1]/div[2]/div[2]/table/tbody/tr[5]/td/img[2]")
#         driver.switch_window(1)
#         driver.click("/html/body/div[1]/table/tbody/tr/td[8]/a")
#         driver.close()
#         driver.switch_window(0)
        

