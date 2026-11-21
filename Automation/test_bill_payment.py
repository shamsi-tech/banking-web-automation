
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def test_bill_payment():

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

        # Open Bill Payment
        wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Bill Pay")
            )
        ).click()

        # Enter payee details
        driver.find_element(
            By.NAME, "payee.name"
        ).send_keys("Test Electricity Company")

        driver.find_element(
            By.NAME, "payee.address.street"
        ).send_keys("Main Road")

        driver.find_element(
            By.NAME, "payee.address.city"
        ).send_keys("Karachi")

        driver.find_element(
            By.NAME, "payee.address.state"
        ).send_keys("Sindh")

        driver.find_element(
            By.NAME, "payee.address.zipCode"
        ).send_keys("75300")

        driver.find_element(
            By.NAME, "payee.phoneNumber"
        ).send_keys("03001234567")

        driver.find_element(
            By.NAME, "payee.accountNumber"
        ).send_keys("123456789")

        driver.find_element(
            By.NAME, "verifyAccount"
        ).send_keys("123456789")

        # Select account
        account_dropdown = Select(
            driver.find_element(By.NAME, "fromAccountId")
        )

        wait.until(
            lambda d: len(
                Select(d.find_element(By.NAME, "fromAccountId")).options
            ) > 0
        )

        account_dropdown = Select(
            driver.find_element(By.NAME, "fromAccountId")
        )

        available_accounts = [
            option.get_attribute("value")
            for option in account_dropdown.options
            if option.get_attribute("value")
        ]

        assert available_accounts, "No account available"

        account_dropdown.select_by_value(available_accounts[0])

        # Enter payment amount
        driver.find_element(
            By.NAME, "amount"
        ).send_keys("10")

        # Send Payment
        driver.find_element(
            By.XPATH, "//input[@value='Send Payment']"
        ).click()

        # Verify payment confirmation
        confirmation = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(),'Bill Payment Complete')]")
            )
        )

        assert confirmation.is_displayed()

        print("Bill Payment Test Passed!")

    except Exception:
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot("screenshots/bill_payment_failure.png")
        raise

    finally:
        driver.quit()
