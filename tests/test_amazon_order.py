import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PlacingOrderAmazonWebsite.utils.config import Config


@pytest.fixture
def driver():
    config = Config()
    driver = webdriver.Chrome(executable_path=config.chrome_driver_path)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_amazon_order(driver):
    driver.get(Config.base_url)

    # Search for a mobile phone
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("mobile phone")
    search_box.send_keys(Keys.RETURN)

    # Click on the first product
    first_product = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-asin][1]")))
    first_product.click()

    # Add the product to cart
    add_to_cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart-button")))
    add_to_cart_button.click()

    # Proceed to checkout
    driver.get("https://www.amazon.com/gp/cart/view.html")
    proceed_to_checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "proceedToCheckout")))
    proceed_to_checkout_button.click()

    # Continue to the next steps of the checkout process
    # (Add code here to fill in shipping and payment details, etc.)

    # Place the order
    place_order_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "placeYourOrder1")))
    place_order_button.click()

    # Optionally, add assertions to verify the order placement success