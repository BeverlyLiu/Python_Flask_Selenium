from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
preferences = {"download.default_directory": "/Users/beverlyliu/PycharmProjects/Flask_Blog/yahoo_finance"}
options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://finance.yahoo.com/')
search_input = driver.find_element_by_id('yfin-usr-qry')
search_input.send_keys('aapl')
search_input.send_keys(Keys.ENTER)

WebDriverWait(driver, 100).until(
    expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="quote-nav"]/ul/li[5]/a')))
driver.find_element_by_xpath('//*[@id="quote-nav"]/ul/li[5]/a').send_keys(Keys.ENTER)

WebDriverWait(driver,100).until(
    expected_conditions.visibility_of_element_located((By.XPATH ,'//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a')))
driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a').click()



