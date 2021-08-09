import time
from selenium import webdriver

# For using Chrome
browser = webdriver.Chrome('/Users/km/alchemy/chromedriver')

# D.O.L.L.A. D$ Dad Hat page
browser.get('https://www.bigdollamerch.com/product/5QCHDA002/d-dad-hat?cp=null')

# purchaseable page
# browser.get('https://www.bigdollamerch.com/product/5QAMDA002/dolla-sign-mask?cp=null')

buyButton = False

while not buyButton:

    try:
        # If this works then the button is not open
        addToCartBtn = addButton = browser.find_element_by_class_name("OutOfStockMsg")

        # Button isn't open restart the script
        print("Button isnt ready yet")

        # Refresh page after a delay
        time.sleep(5)
        browser.refresh()

    except:

        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")

        # Click the button and end the script
        print("Button was clicked")
        addToCartBtn.click()
        buyButton = True
