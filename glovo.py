# packages imported
from selenium import webdriver
import pandas as pd

# headless mode set up
options = webdriver.ChromeOptions()
options.headless = True
# webdriver set up and url
PATH = "C:\Program Files (x86)\chromedriver.exe"  # align this with your webdrivers' directory path
url = "https://glovoapp.com/ke/en/nairobi/chicken-inn-nbo/?content=menu-c.702212460"
driver = webdriver.Chrome(
    PATH, options=options
)  # note the added info after the coma ,,,aaah hiii kizungu imeniboo sasa wee ona kuna options hapo nimeeka

driver.get(url)
# array to collect info
info = []
# all items containers
items = driver.find_elements_by_xpath("//div[contains(@type,'PRODUCT_ROW')]")
print(len(items))
# looping all items at a go
for item in items:

    # try:

    name = item.find_element_by_xpath(
        ".//span[contains(@data-test-id,'product-row-name__highlighter')]/span"
    ).text
    # except:
    #   name = "null"
    # try:

    price = item.find_element_by_xpath(
        ".//span[contains(@class,'product-price__effective product-price__effective--new-card')]"
    ).text
    # except:
    #   price = "nulll"
    datast = {"name": name, "price": price}
    info.append(datast)
# data aragement into rows and columns and storing into csv and json
data = pd.DataFrame(info)
# data.to_csv("glovo.csv", index=False)
# data.to_json("glovo.json")
print(data)

driver.close()
