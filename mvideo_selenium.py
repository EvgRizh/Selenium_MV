#!/home/jenia/.virtualenvs/Selenium_mv/bin/python
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

url = "https://www.mvideo.ru"
Options = Options()
Options.headless = True
browser = webdriver.Firefox(options=Options)
articuls = [
            "30054781",
            "30056687",
            "30055123",
            "30063680",
            "30059533",
            ]
city = 'Ярославль'

try:
    file = open("result.txt", "a")
    file.write(str(datetime.now())+"\n")
    browser.get(url=url)
    time.sleep(5)
    # установка необходимого города
    set_city = browser.find_element(By.CLASS_NAME, 'location-text')
    if set_city.text != city:
        set_city.click()
        input_city = browser.find_element(By.ID, "3")
        input_city.send_keys(city)
        time.sleep(5)
        input_city.send_keys(Keys.ENTER)
        time.sleep(5)
    # перебор артикулов и вывод информации по ним
    for i in articuls:
        input_field = browser.find_element(By.ID, "1")
        input_field.send_keys(i)
        input_field.send_keys(Keys.ENTER)
        time.sleep(10)
        title = browser.find_element(By.XPATH, "//h1[@class='title']").text
        price = browser.find_element(By.CLASS_NAME, "price__main-value")
        try:
            price_sale = browser.find_element(By.CLASS_NAME, "price__sale-value")
            price_sale = float(price_sale.text.replace(" ", ""))
            price = float(price.text.replace(" ", "")[0:-1])
            sale = 100 - price * 100 / price_sale
            file.write("На {} цена со скидкой - {}, цена без скидки - {}, скидка - {}%\n".format(title, price, price_sale, round(sale)))
        except Exception:
            file.write("На {} скидки нет!\n".format(title))
        browser.implicitly_wait(5)
except Exception as ex:
    file.write("Ошибка: {}".format(ex))
finally:
    x = "-*"*15
    file.write(x)
    browser.close()
    browser.quit()
    file.close()