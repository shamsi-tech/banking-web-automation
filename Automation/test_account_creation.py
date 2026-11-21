
import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


def test_account_creation():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Open ParaBank homepage
        driver.get("https://parabank.parasoft.com/parabank/index.htm")

        wait = WebDriverWait(driver, 15)

        # Click Register
        wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        ).click()

        # Generate unique username
        username = "uzair" + datetime.now().strftime("%Y%m%d%H%M%S")

        # Enter registration details
        driver.find_element(By.ID, "customer.firstName").send_keys("Uzair")
        driver.find_element(By.ID, "customer.lastName").send_keys("Shamsi")
        driver.find_element(By.ID, "customer.address.street").send_keys("Gulshan Karachi")
        driver.find_element(By.ID, "customer.address.city").send_keys("Karachi")
        driver.find_element(By.ID, "customer.address.state").send_keys("Sindh")
        driver.find_element(By.ID, "customer.address.zipCode").send_keys("75300")
        driver.find_element(By.ID, "customer.phoneNumber").send_keys("03001234567")
        driver.find_element(By.ID, "customer.ssn").send_keys("123456789")

        driver.find_element(By.ID, "customer.username").send_keys(username)
        driver.find_element(By.ID, "customer.password").send_keys("Uzair@12345")
        driver.find_element(By.ID, "repeatedPassword").send_keys("Uzair@12345")

        # Click Register button
        driver.find_element(
            By.XPATH, "//input[@value='Register']"
        ).click()

        # Verify successful registration
        success_message = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(),'Your account was created successfully')]")
            )
        )

        assert success_message.is_displayed()

        print("Account Creation Test Passed!")
        print("Generated Username:", username)

    except Exception:
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot("screenshots/account_creation_failure.png")
        raise

    finally:
        driver.quit()
