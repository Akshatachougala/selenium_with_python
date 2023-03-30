print("hello world")
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(5)
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.quit()