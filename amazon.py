import time
from selenium import webdriver

# For using Chrome
browser = webdriver.Chrome('/Users/km/alchemy/chromedriver')

# BestBuy RTX 3060 page
browser.get('https://www.amazon.com/PlayStation-Marvels-Iron-Man-Bundle-4/dp/B08NRGF2DL/ref=sr_1_4?brr=1&dchild=1&qid=1628481134&rd=1&s=videogames&sr=1-4')

# BestBuy purchaseable page
# browser.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-nvlink-bridge-for-3090-cards-space-gray/6441554.p?skuId=6441554')

buyButton = False

while not buyButton:

    try:
        # If this works then the button is not open
        addToCartBtn = addButton = browser.find_element_by_class_name("")

        # Button isn't open restart the script
        print("Button isnt ready yet")

        # Refresh page after a delay
        time.sleep(1)
        browser.refresh()

    except:

        addToCartBtn = addButton = browser.find_element_by_class_name("a-button-input")

        # Click the button and end the script
        print("Button was clicked")
        addToCartBtn.click()
        buyButton = True
