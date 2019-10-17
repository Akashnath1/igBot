from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
time.sleep(2)
login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
login_button.click()
time.sleep(2)
# usernameIG = 'veronicagalecka'
# link = "https://www.instagram.com/" + usernameIG + "/"
# driver.get(link)
# login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=private_profile']")
# driver.implicitly_wait(3)
        # driver.find_element_by_xpath("//a[@href='accounts/login/?source=private_profile']")
# time.sleep(3)
# login_button.click()
# time.sleep(3)
elem = driver.find_element_by_name('username')
elem.clear()
elem.send_keys('fcbakash')
elem = driver.find_element_by_name('password')
elem.clear()
elem.send_keys("")
# elem = driver.find_element_by_name('Search')
elem.send_keys(Keys.RETURN)
notNowButton = WebDriverWait(driver, 15).until(
    lambda d: d.find_element_by_xpath('//button[text()="Not Now"]')
)
notNowButton .click()
searchIg = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Search']")
    )
)#driver.find_element_by_xpath("//span[@class='TqC_a']")
# searchIg.click()
# driver.implicitly_wait(3)
# searchIg.send_keys(Keys.RETURN)
# driver.implicitly_wait(3)
# driver.get("https://www.instagram.com/" + usernameIG + "/")
searchIg.send_keys('shivam.p.singh1')
time.sleep(2)
searchIg.send_keys(Keys.RETURN)
time.sleep(1)
searchIg.send_keys(Keys.RETURN)
time.sleep(3)
# for i in range(5):
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
pic_hrefs =[]
hrefs = driver.find_elements_by_tag_name('a')
all_hrefs = [elem.get_attribute('href') for elem in hrefs]
for href in all_hrefs:
    if 'https://www.instagram.com/p/' in href:
        pic_hrefs.append(href)
# elements = driver.find_elements_by_class_name("v1Nh3 kIKUG  _bz0w")
# for elem in elements:
#     href = elements.get_attribute("href")

print(len(pic_hrefs))
print (pic_hrefs)
for pic_href in pic_hrefs:
    driver.get(pic_href)
    try:
        like = driver.find_element_by_xpath(
            "//span [@class=\'glyphsSpriteHeart__outline__24__grey_9 u-__7' and @aria-label=\'Like\']")
        like.click()

    except NoSuchElementException:
        # unlike = driver.find_element_by_xpath(
        #     "//span [@class=\'glyphsSpriteHeart__filled__24__red_5 u-__7' and @aria-label=\'Unlike\']")
        # unlike.click()
        continue

driver.quit()