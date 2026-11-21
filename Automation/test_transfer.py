
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def test_fund_transfer():

    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    try:
        # Open ParaBank
        driver.get("https://parabank.parasoft.com/parabank/index.htm")

        # Login
        wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        ).send_keys("umaim0@")

        driver.find_element(
            By.NAME, "password"
        ).send_keys("qwert12")

        driver.find_element(
            By.XPATH, "//input[@value='Log In']"
        ).click()

        # Verify login
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[contains(text(),'Account Services')]")
            )
        )

        # Open Transfer Funds
        wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Transfer Funds"))
        ).click()

        # Wait for account dropdowns
        wait.until(
            EC.presence_of_element_located((By.ID, "fromAccountId"))
        )

        wait.until(
            EC.presence_of_element_located((By.ID, "toAccountId"))
        )

        # Wait until source accounts are available
        wait.until(
            lambda d: len(
                Select(d.find_element(By.ID, "fromAccountId")).options
            ) > 0
        )

        from_account = Select(
            driver.find_element(By.ID, "fromAccountId")
        )

        to_account = Select(
            driver.find_element(By.ID, "toAccountId")
        )

        # Debug account options
        print("\n--- SOURCE ACCOUNT OPTIONS ---")

        for option in from_account.options:
            print(option.text, option.get_attribute("value"))

        print("\n--- DESTINATION ACCOUNT OPTIONS ---")

        for option in to_account.options:
            print(option.text, option.get_attribute("value"))

        # Select source account
        source_options = [
            option.get_attribute("value")
            for option in from_account.options
            if option.get_attribute("value")
        ]

        assert source_options, "No source account available"

        from_account.select_by_value(source_options[0])

        # Refresh destination dropdown after source selection
        to_account = Select(
            driver.find_element(By.ID, "toAccountId")
        )

        destination_options = [
            option.get_attribute("value")
            for option in to_account.options
            if option.get_attribute("value")
            and option.get_attribute("value") != source_options[0]
        ]

        assert destination_options, "No second account available"

        to_account.select_by_value(destination_options[0])

        # Enter amount
        driver.find_element(By.ID, "amount").send_keys("10")

        # Click Transfer
        driver.find_element(
            By.XPATH, "//input[@value='Transfer']"
        ).click()

        # Verify transfer
        confirmation = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(),'Transfer Complete!')]")
            )
        )

        assert confirmation.is_displayed()

        print("Fund Transfer Test Passed!")

    except Exception:
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot("screenshots/transfer_failure.png")
        raise

    finally:
        driver.quit()
