from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class InstaBot():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def close(self):
        self.driver.close()
        self.driver.quit()

    def loginIG(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        elem = driver.find_element_by_name('username')
        elem.send_keys(self.username)
        elem = driver.find_element_by_name('password')
        elem.send_keys(self.password)
        elem.send_keys(Keys.RETURN)

    def searchUsername(self, usernameIG):
        driver = self.driver
        notNowButton = WebDriverWait(driver, 15).until(
            lambda d: d.find_element_by_xpath('//button[text()="Not Now"]')
        )

        notNowButton.click()
        searchIg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Search']")
            )
        )
        searchIg.send_keys(usernameIG)
        time.sleep(2)
        searchIg.send_keys(Keys.RETURN)
        time.sleep(1)
        searchIg.send_keys(Keys.RETURN)
        time.sleep(3)

    def likepostT(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        pic_hrefs = []

        hrefs = driver.find_elements_by_tag_name('a')
        all_hrefs = [elem.get_attribute('href') for elem in hrefs]
        for href in all_hrefs:
            if 'https://www.instagram.com/p/' in href:
                pic_hrefs.append(href)

        print(len(pic_hrefs))
        print(pic_hrefs)
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



if __name__ == '__main__':
    username = "an10ig"
    password = "9431269821"
    igbot = InstaBot(username, password)
    igbot.loginIG()
    try:
        username = "fcbarcelona"
        igbot.searchUsername(username)
        igbot.likepostT()
    except Exception:
        igbot.close()

    igbot.close()
    # igbot.likepost('veronicagalecka', 3)
