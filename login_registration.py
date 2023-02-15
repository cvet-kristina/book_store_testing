# # Регистрация аккаунта
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_account.click()
# reg_email = driver.find_element_by_id("reg_email")
# reg_email.send_keys("super@mail.com")
# reg_password = driver.find_element_by_id("reg_password")
# reg_password.send_keys("mypassissuper")
# register_btn = driver.find_element_by_css_selector("[value='Register']")
# register_btn.click()
#
# driver.quit()

# Логин в систему
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
my_account.click()
login = driver.find_element_by_id("username")
login.send_keys("super@mail.com")
log_password = driver.find_element_by_id("password")
log_password.send_keys("mypassissuper")
login_btn = driver.find_element_by_css_selector("[value='Login']")
login_btn.click()
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation > ul > li:nth-child(6) > a"))
)

driver.quit()