
import os
import re
from typing import List
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

# URL validation regex expression from Django framework source code
urlRegex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
isValidUrl = False

while not isValidUrl:
    urlToScan = input("Please, input  URL to scan: ")
    isValidUrl = re.match(urlRegex, urlToScan) is not None
    if not isValidUrl:
        print("The give input is not a valid URL, try again.")

chromeDriverPath = os.path.join(os.getcwd(), "resources", "chromedriver.exe")
driver = webdriver.Chrome(chromeDriverPath)
driver.get(urlToScan)

countOfFormElementsWithMethodGet = 0
countOfImageElements = 0

formElements: List[WebElement] = driver.find_elements_by_xpath(".//form") #could be: driver.find_elements_by_tag_name("form")
for element in formElements:
    if element.get_attribute("method") == "get":
        countOfFormElementsWithMethodGet += 1

imageElements: List[WebElement] = driver.find_elements_by_xpath(".//img") #could be: driver.find_elements_by_tag_name("img")
countOfImageElements = len(imageElements)

driver.quit()

print("Number of HTM: form elements with method get: ", countOfFormElementsWithMethodGet)
print("Number of HTML image tags: ", countOfImageElements)