
import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Open ParaBank homepage
        driver.get("https://parabank.parasoft.com/parabank/index.htm")

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        ).send_keys("areeb22")

       
        driver.find_element(
            By.NAME, "password"
        ).send_keys("qwerty!2")

        
        driver.find_element(
            By.XPATH, "//input[@value='Log In']"
        ).click()

        # Verify Account Services page
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[contains(text(),'Account Services')]")
            )
        )

        assert "overview.htm" in driver.current_url

        print("Login Test Passed!")

    except Exception:
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot("screenshots/login_failure.png")
        raise

    finally:
        driver.quit()
