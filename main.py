from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time

#设置购买时间
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
buytime = "2023-02-06 19:59:57.000000"

#chrome位置和chrome driver位置
option = webdriver.ChromeOptions()
option.binary_location=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
driver = webdriver.Chrome('D:\Desktop\chromedriver.exe')

#选择商品
def select(buytime):
    while True:
        #当前时间大于购买时间
        if now >= buytime:
            try:
                #理论上只需要在css选择器里面更换商品的编码就可以在购物车中选择商品
                driver.find_element_by_css_selector("J_Item_4750575158586 > ul > li.td.td-chk > div > div > div > label").click()
                #因为脚本没有找到结算按钮，而网页刷新太快会导致脚本报错
                if WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "J_CartSwitch"))):
                    fun()
            except:
                visit()
                select(buytime)
#购买
def buy():
    try:
        if WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "tbToken"))):
            driver.find_element_by_link_text("提交订单").click()
    except:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        visit()
        select(buytime)

def fun():
        try:
            driver.find_element_by_css_selector("#J_Go").click()
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
            buy()
        except:
            time.sleep(0.1)
            fun()

def login():
    time.sleep(10)

def visit():
    driver.get(
        "https://cart.taobao.com/cart.htm?spm=pc_detail.27183998%2Fevo318828b447259.0.0.3fc67dd6EA8M4f&from=btop&app=chrome")


if __name__ == "__main__":
    visit()
    login()
    select(buytime)