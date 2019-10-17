from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
# elem = driver.find_element_by_name("email")
# elem.clear()
# elem.send_keys("akash.nath1")
# elemp = driver.find_element_by_name("pass")
# elemp.clear()
# elemp.send_keys("akash.NATH9811036534")
# elemp.send_keys(Keys.RETURN)
# WebDriverWait(driver, 200)
# driver.scroll()
driver.quit()
