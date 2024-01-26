from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Launch browser
driver = webdriver.Chrome()  # veya başka bir tarayıcı seçeneği

#  Navigate to url 'http://automationexercise.com'
driver.get("http://automationexercise.com")

# Verify that home page is visible successfully
try:
    WebDriverWait(driver, 10).until(EC.title_contains("Automation Exercise"))
    print("Home page is successfully visible.")
except Exception as e:
    print("Error: Home page is not visible.")
    print(e)

# Click 'Products' button
products_button =driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(2) > a > i")
products_button.click()

  # Hover over first product and click 'Add to cart'
first_product = driver.find_element(By.CLASS_NAME, "overlay-content")
ActionChains(driver).move_to_element(first_product).perform()
view_product_button = first_product.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/ul")
view_product_button.click()
time.sleep(5)
add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "body > section > div > div > div.col-sm-9.padding-right > div.product-details > div.col-sm-7 > div > span > button > i")
add_to_cart_button.click()

time.sleep(5)

  # Click 'Continue Shopping' button
continue_shopping_button = driver.find_element(By.CSS_SELECTOR, "#cartModal > div > div > div.modal-footer")
continue_shopping_button.click()
time.sleep(5)

products_button =driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(2) > a > i")
products_button.click()

#Hover over second product and click 'Add to cart'
second_product = driver.find_element(By.CLASS_NAME, "product-overlay")
ActionChains(driver).move_to_element(second_product).perform()
view_product_button = second_product.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[2]/ul/li/a")
view_product_button.click()
time.sleep(5)
add_to_cart_button = driver.find_element(By.XPATH, "/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button")
add_to_cart_button.click()
time.sleep(5)

 # Click 'View Cart' button
view_cart=driver.find_element(By.CSS_SELECTOR, "#cartModal > div > div > div.modal-body > p:nth-child(2) > a > u")
view_cart.click()

    # Verify both products are added to Cart
try:
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#cart_items > div")))
    print("Both products are added to the Cart.")
except Exception as e:
    print("Error: Products are not added to the Cart.")


try:
    # Verify product for first product
    price_element = driver.find_element(By.CSS_SELECTOR, "#product-1 > td.cart_price").text
    assert price_element == "Rs. 500", "Price verification failed for the first product."
    print("Price verification successful for the first product.")
except Exception as e:
    print("Error: Price verification failed for the first product.")
    
try:
        # Verify price for second product
    price_element2 = driver.find_element(By.CSS_SELECTOR, "#product-2 > td.cart_price").text
    assert price_element2 == "Rs. 400", "Price verification failed for the second product."
    print("Price verification successful for the second product.")
except Exception as e:
    print("Error: Price verification failed for the second product.")


try:
    
    # Verify quantity for first product
    quantity_element_1 = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/table/tbody/tr[1]/td[4]").text
    assert quantity_element_1 == "1", "Quantity verification failed for the first product."
    print("Quantity verification successful for the first product.")
except Exception as e:
    print("Error: Verification failed for the first product.")

    
try: 
    # Verify quantity for second product
    quantity_element_2 = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/table/tbody/tr[2]/td[4]").text
    assert quantity_element_2 == "1", "Quantity verification failed for the second product."
    print("Quantity verification successful for the second product.")
except Exception as e:
    print("Error: Verification failed for the second product.")


try:
   # Verify total price for first product 
    total_price_element_1 = driver.find_element(By.XPATH, '/html/body/section/div/div[2]/table/tbody/tr[1]/td[5]').text
    assert total_price_element_1 == "RS. 500", "Total price verification failed for the first product."
    print("Total price verification successful for the first product.")
except Exception as e:
    print("Error:Total price verification failed for the first product")


try:
    # Verify total price for second product 
    total_price_element_2 = driver.find_element(By.CSS_SELECTOR, '#product-2 > td.cart_total').text
    assert total_price_element_2 == "RS. 400", "Total price verification failed for the second product."
    print("Total price verification successful for the second product.")
except Exception as e:
    print("Error:Total price verification failed for the second product")










