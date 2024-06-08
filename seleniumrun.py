from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def search(search_query):
    options = webdriver.ChromeOptions()
    options=Options()
    #options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://www.myntra.com")
    

    # Close the login popup if it appears
    try:
        close_button = driver.find_element(By.XPATH, '//button[contains(text(), "✕")]')
        close_button.click()
    except:
        pass

    # Enter the search query
    search_box = driver.find_element(By.XPATH, ".//input[@class='desktop-searchBar']")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.ENTER)
    #search_box.submit()

    # Wait for the results to load and display the titles
    driver.implicitly_wait(5)  # You can increase this if your internet is slow

    products = driver.find_elements(By.XPATH, ".//h3[@class='product-brand']")
    product_names = [product.text for product in products[:1]]  # Get top 5 results
 
    driver.quit()
    results = [b for b in zip(product_names)] 
    for result in results:
        return result