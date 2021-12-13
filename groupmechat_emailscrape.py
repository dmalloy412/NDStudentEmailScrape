from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#two scrapes: One with all names, one with the people with comments in the past 3 months

driver = webdriver.Firefox()
driver.get("https://web.groupme.com/chats")
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="signinUserNameInput"]')))
username = driver.find_element_by_xpath('//input[@id="signinUserNameInput"]')
username.send_keys("dmalloy412@gmail.com")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="signinPasswordInput"]')))
username = driver.find_element_by_xpath('//input[@id="signinPasswordInput"]')
username.send_keys("8Dttf,ft.")

log_in = driver.find_element_by_xpath('//button[@type="submit"]')
ActionChains(driver).click(log_in).perform()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label,'Sales & Giveaways')]")))
sales_and_giveaways = driver.find_element_by_xpath("//button[contains(@aria-label,'Sales & Giveaways')]")
ActionChains(driver).click(sales_and_giveaways).perform()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'dropdown-toggle') and .//h2[text()='Sales & Giveaways']]")))
s_g_dropdown = driver.find_element_by_xpath("//button[contains(@class,'dropdown-toggle') and .//h2[text()='Sales & Giveaways']]")
ActionChains(driver).click(s_g_dropdown).perform()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@ng-click='showMembers()']")))
s_g_dropdown = driver.find_element_by_xpath("//button[@ng-click='showMembers()']")
ActionChains(driver).click(s_g_dropdown).perform()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='modal-content' and .//div[@class='members row']]")))

name_list = []
name_blocks = driver.find_elements_by_xpath("//div[@class='col-sm-3']//div[@class='member accessible-focus']")
for i in range(1,1+len(name_blocks)):
    current_block = driver.find_element_by_xpath("(//div[@class='col-sm-3']//div[@class='member accessible-focus'])[" + str(i) + "]")
    name = current_block.get_attribute("aria-label")
    name_list.append(name)
print(name_list)
