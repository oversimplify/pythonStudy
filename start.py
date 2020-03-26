from selenium import webdriver

import pickle

# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=C:\\Users\\vibe\\AppData\\Local\\Google\\Chrome\\User Data")

# options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])

driver = webdriver.Chrome()
# driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
# driver.maximize_window()

driver.get('http://www.fakenamegenerator.com/')

# print(driver.get_cookies())

# cookies = driver.get_cookies()
# with open('D:/develop/cookies/generateInfor_cookie.txt','wb') as f:
#     pickle.dump(cookies,f)

sex = driver.find_element_by_css_selector('.bcs .content img').get_attribute('alt')
name = driver.find_element_by_css_selector('.info .address h3').get_attribute('textContent')
address = driver.find_element_by_css_selector('.info .address .adr').get_attribute('textContent')
ssn = driver.find_element_by_css_selector('.info .extra>dl:nth-child(2)').get_attribute('textContent')
phone = driver.find_element_by_css_selector('.info .extra>dl:nth-child(4)').get_attribute('textContent')
# sex_js = '$(\".bcs .content img\")[0]'
# sex_0 = driver.execute_script(sex_js)
print (sex)
print(name)
print(address)
print(ssn)
print(phone)