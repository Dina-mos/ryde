from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

# Setup Chrome options (optional)
options = Options()
options.add_argument("--start-maximized")  # Start maximized

# Set path to your chromedriver
service = Service("C:\\chrome-driver\\chromedriver.exe")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the login page
    driver.get("http://dashboard.rydeapp.net/admin/login")

    # Wait for the page to load (replace with WebDriverWait for production)
    time.sleep(2)

    # Locate and interact with the login form
    username = driver.find_element(By.ID, "data.email")
    password = driver.find_element(By.ID, "data.password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")



    # Fill in the login credentials
    username.send_keys("tcf@rydeapp.net")
    password.send_keys("just4Test")

    # Click the login button
    login_button.click()

    time.sleep(2)

    # Add Location
    btn_add_location = driver.find_element(By.XPATH, "//a[@href='/admin/locations/create']")
    btn_add_location.click()

    time.sleep(3)  # Wait for the map and controls to load

    # 1. Click the "Draw Polygons" button
    try:
        draw_btn = driver.find_element(By.CSS_SELECTOR, ".leaflet-pm-icon-polygon")
        draw_btn.click()
    except Exception as e:
        print("Draw button not found or not clickable:", e)

    time.sleep(1)

    # 2. Find the map div and get its location and size
    try:
        map_div = driver.find_element(By.CSS_SELECTOR, '[x-ref="map"]')
        loc = map_div.location
        size = map_div.size
    except Exception as e:
        print("Draw button not found or not clickable:", e)


    try:
        actions = ActionChains(driver)

        # 3. Generate 4 random points within the map div and click them
        for _ in range(4):
            x = size['width'] - 20
            y = size['height'] - 20
            print(f"Map x: {x}, y: {y}")
            x_offset = random.randint(20, size['width'] - 20)
            y_offset = random.randint(20, size['height'] - 20)
            actions.move_to_element_with_offset(map_div, x_offset, y_offset).click()
            time.sleep(2)

        actions.perform()
        time.sleep(1)
    except Exception as e:
        print("Error while clicking on the map:", e)

    # 4. Click the "Finish" button
    # finish_btn = driver.find_element(By.CSS_SELECTOR, ".action-finish")
    # finish_btn.click()

    # Wait to see the result
    time.sleep(60)

finally:
    # Close the browser
    driver.quit()
