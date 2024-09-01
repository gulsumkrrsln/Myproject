from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()

driver.get("https://www.akakce.com/")
driver.maximize_window()
time.sleep(5)

Giris_yap = driver.find_element(By.CSS_SELECTOR,"#H_rl_v8 a:nth-child(2)")
Giris_yap.click()
time.sleep(5)

username= driver.find_element(By.ID, "life")
username.click()
time.sleep(2)

username.send_keys("gulsum329778@gmail.com")

password= driver.find_element(By.ID, "lifp")
password.click()
time.sleep(2)

password.send_keys("Akakçe123456")

tıkla=driver.find_element(By.ID,"lfb")
tıkla.click()
time.sleep(5)

arama= driver.find_element(By.ID,"q")
arama.click()
time.sleep(2)

arama.send_keys("Iphone")
time.sleep(2)

arama_butonu=driver.find_element(By.CSS_SELECTOR, "#H_s_v8 button i")
arama_butonu.click()
time.sleep(10)


ürüne_git =driver.find_element(By.XPATH, '//*[@id="CPL"]/li[1]/a/span/span[5]/b')
ürüne_git.click()
time.sleep(5)

takip_listesine_ekle=driver.find_element(By.CSS_SELECTOR,"#pf_w_v8 span")
takip_listesine_ekle.click()
time.sleep(10)




