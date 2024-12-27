from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Headless Chrome setup
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
service = Service("C:/Users/Zamin/Videos/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
import time

# Explicit wait
wait = WebDriverWait(driver, 10)

# Test URL
driver.get("http://13.201.23.243:5173/")  # Replace with your app's URL
time.sleep(3)  # Wait for the page to load

# Test case 1: Add person with all valid fields
def test_add_person_all_fields():
    driver.find_element(By.NAME, "name").send_keys("John Doe")
    driver.find_element(By.NAME, "email").send_keys("john.doe@example.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.CLASS_NAME, "form-submit").click()
    time.sleep(1)
    assert "John Doe" in driver.page_source

# Test case 2: Add person with only name and email
def test_add_person_partial_fields():
    driver.find_element(By.NAME, "name").send_keys("Jane Doe")
    driver.find_element(By.NAME, "email").send_keys("jane.doe@example.com")
    driver.find_element(By.CLASS_NAME, "form-submit").click()
    time.sleep(1)
    assert "Error: All fields are required" in driver.page_source

# Test case 3: Add person with empty fields
def test_add_person_empty_fields():
    driver.find_element(By.CLASS_NAME, "form-submit").click()
    time.sleep(1)
    assert "Error: All fields are required" in driver.page_source

# Test case 4: Update person with valid data
def test_update_person_valid():
    update_button = driver.find_element(By.CLASS_NAME, "update-button-john-doe")
    update_button.click()
    name_input = driver.find_element(By.NAME, "name")
    name_input.clear()
    name_input.send_keys("John Updated")
    driver.find_element(By.CLASS_NAME, "form-submit").click()
    time.sleep(1)
    assert "John Updated" in driver.page_source

# Test case 5: Update person with empty fields
def test_update_person_empty_fields():
    update_button = driver.find_element(By.CLASS_NAME, "update-button-jane-doe")
    update_button.click()
    name_input = driver.find_element(By.NAME, "name")
    name_input.clear()
    driver.find_element(By.CLASS_NAME, "form-submit").click()
    time.sleep(1)
    assert "Error: All fields are required" in driver.page_source

# Test case 6: Delete a person
def test_delete_person():
    delete_button = driver.find_element(By.CLASS_NAME, "delete-button-john-updated")
    delete_button.click()
    time.sleep(1)
    assert "John Updated" not in driver.page_source

# Test case 7: Add person with invalid email
def test_add_person_invalid_email():
    driver.find_element(By.NAME, "name").send_keys("Invalid Email")
    driver.find_element(By.NAME, "email").send_keys("invalid-email")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.CLASS_NAME, "form-submit").click()
    time.sleep(1)
    assert "Error: Invalid email format" in driver.page_source

# Test case 8: Delete a non-existent person
def test_delete_non_existent_person():
    try:
        delete_button = driver.find_element(By.CLASS_NAME, "delete-button-non-existent")
        delete_button.click()
    except Exception as e:
        assert "Unable to locate element" in str(e)

# Test case 9: Add person with duplicate email
def test_add_person_duplicate_email():
    driver.find_element(By.NAME, "name").send_keys("Duplicate User")
    driver.find_element(By.NAME, "email").send_keys("john.doe@example.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.CLASS_NAME, "form-submit").click()
    time.sleep(1)
    assert "Error: Email already exists" in driver.page_source


def test_update_person_duplicate_email():
    update_button = driver.find_element(By.CLASS_NAME, "update-button-jane-doe")
    update_button.click()
    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys("john.doe@example.com")
    driver.find_element(By.CLASS_NAME, "form-submit").click()
    time.sleep(1)
    assert "Error: Email already exists" in driver.page_source

# Test case 11: Update person without making changes
def test_update_person_no_changes():
    update_button = driver.find_element(By.CLASS_NAME, "update-button-jane-doe")
    update_button.click()
    driver.find_element(By.CLASS_NAME, "form-submit").click()
    time.sleep(1)
    assert "No changes made" in driver.page_source

# Test case 12: Verify deletion removes buttons
def test_delete_removes_buttons():
    delete_button = driver.find_element(By.CLASS_NAME, "delete-button-jane-doe")
    delete_button.click()
    time.sleep(1)
    assert "update-button-jane-doe" not in driver.page_source


test_add_person_all_fields()
test_add_person_partial_fields()
test_add_person_empty_fields()
test_update_person_valid()
test_update_person_empty_fields()
test_delete_person()
test_add_person_invalid_email()
test_delete_non_existent_person()
test_add_person_duplicate_email()
test_update_person_duplicate_email()
test_update_person_no_changes()
test_delete_removes_buttons()

driver.quit()
