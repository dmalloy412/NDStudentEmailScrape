from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# open nd student directory
driver = webdriver.Firefox()
driver.get("https://nd.joinhandshake.com/")
driver.maximize_window()
time.sleep(3)
login_button = "//div[text()='University of Notre Dame Login']"
# click the button
login = driver.find_element_by_xpath(login_button)
ActionChains(driver).click(login).perform()
time.sleep(3)

username = driver.find_element_by_xpath('//input[@id="okta-signin-username"]')
username.send_keys("dmalloy1@nd.edu")

password = driver.find_element_by_id('okta-signin-password')
password.send_keys("8Dttf,ft.")

submit = driver.find_element_by_id("okta-signin-submit")
ActionChains(driver).click(submit).perform()

time.sleep(3)
send_push = driver.find_element_by_xpath('//input[@value="Send Push"]')
ActionChains(driver).click(send_push).perform()
time.sleep(13)

student_tab = driver.find_element_by_xpath("//nav//a//span[text()='Students']")
ActionChains(driver).click(student_tab).perform()
time.sleep(5)

checkbox = driver.find_element_by_xpath("//input[@id='own_institution_only' and @type='checkbox']")
ActionChains(driver).click(checkbox).perform()
time.sleep(2)

for class_year in ['Freshman','Sophomore','Junior','Senior']:
    year_input = driver.find_element_by_xpath('//input[@id="autosuggest-facet-school_years"]')
    year_input.send_keys(class_year)
    time.sleep(3)
    option = driver.find_element_by_xpath("//div[@id='react-select-2--option-0']")
    ActionChains(driver).click(option).perform()
    time.sleep(3)

name_list = []
frac = 0
num_pages = 309
for pnum in range(1, 1+num_pages):
    next_page = driver.find_element_by_xpath("//button[@aria-label='next page']")
    driver.execute_script("arguments[0].scrollIntoView();", next_page)
    for i in range(1,1+len(driver.find_elements_by_xpath("//div[@data-hook='search-results']//h2[contains(@class,'heading')]//a"))):
        name_path = "(//div[@data-hook='search-results']//h2[contains(@class,'heading')]//a)[" + str(i) + "]"
        name = driver.find_element_by_xpath(name_path).text
        parts = name.split()
        if len(parts) >= 2:
            first_two = parts[0] + " " + parts[1]
        name_list.append(first_two)
    frac = float(pnum)/float(num_pages)
    if frac < 1:
        ActionChains(driver).click(next_page).perform()
        time.sleep(3)
    if frac*num_pages == 150:
        print(name_list)
        print("********BREAK!!!!!!!!!!!!!!!!!!!!!!!!")

print(name_list)
