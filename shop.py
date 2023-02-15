# # Отображение страницы товара
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_account.click()
# login = driver.find_element_by_id("username")
# login.send_keys("super@mail.com")
# log_password = driver.find_element_by_id("password")
# log_password.send_keys("mypassissuper")
# menu_shop = driver.find_element_by_id("menu-item-40")
# menu_shop.click()
# book_html_5_forms = driver.find_element_by_class_name("post-181")
# book_html_5_forms.click()
# book_title = driver.find_element_by_class_name("entry-title")
# assert book_title.text == "HTML5 Forms"
#
# driver.quit()

# # Количество товаров в категории
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_account.click()
# login = driver.find_element_by_id("username")
# login.send_keys("super@mail.com")
# log_password = driver.find_element_by_id("password")
# log_password.send_keys("mypassissuper")
# menu_shop = driver.find_element_by_id("menu-item-40")
# menu_shop.click()
# cat_html = driver.find_element_by_css_selector(".cat-item-19 > a")
# cat_html.click()
# cat_html_items = driver.find_elements_by_css_selector(".masonry-done > li")
# assert len(cat_html_items) == 3
#
# driver.quit()

# # Сортировка товаров
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_account.click()
# login = driver.find_element_by_id("username")
# login.send_keys("super@mail.com")
# log_password = driver.find_element_by_id("password")
# log_password.send_keys("mypassissuper")
# menu_shop = driver.find_element_by_id("menu-item-40")
# menu_shop.click()
# selector_element = driver.find_element_by_class_name("orderby")
# selector_element_default = selector_element.get_attribute("value")
# assert selector_element_default == "menu_order"
# select = Select(selector_element)
# select.select_by_value("price-desc")
# selector_element = driver.find_element_by_class_name("orderby")
# selector_element_high_to_law = selector_element.get_attribute("value")
# assert selector_element_high_to_law == "price-desc"
#
# driver.quit()

# # Отображение, скидка товара
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_account.click()
# login = driver.find_element_by_id("username")
# login.send_keys("super@mail.com")
# log_password = driver.find_element_by_id("password")
# log_password.send_keys("mypassissuper")
# menu_shop = driver.find_element_by_id("menu-item-40")
# menu_shop.click()
# book_android = driver.find_element_by_class_name("post-169")
# book_android.click()
# old_price = driver.find_element_by_tag_name("del")
# assert old_price.text == "₹600.00"
# new_price = driver.find_element_by_css_selector("ins .amount")
# assert new_price.text == "₹450.00"
# book_cover = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "images"))
# )
# book_cover.click()
# close_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))
# )
# close_btn.click()
#
# driver.quit()

# # Проверка цены в корзине (для теста использовала книгу "Mastering JavaScript)
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# menu_shop = driver.find_element_by_id("menu-item-40")
# menu_shop.click()
# add_btn = driver.find_element_by_css_selector(".post-165  > a:nth-child(2)")
# add_btn.click()
# time.sleep(3)
# item_basket = driver.find_element_by_class_name("cartcontents")
# assert item_basket.text == "1 Item"
# price_basket = driver.find_element_by_css_selector(".wpmenucart-contents > .amount")
# assert price_basket.text == "₹350.00"
# basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
# basket_btn.click()
# WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal > td > span"), "₹")
# )
# WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total > td > strong"), "₹")
# )
#
# driver.quit()

# # Работа в корзине (для теста использовала книгу "Mastering JavaScript")
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
#
# menu_shop = driver.find_element_by_id("menu-item-40")
# menu_shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# add_btn = driver.find_element_by_css_selector(".post-165  > a:nth-child(2)")
# add_btn.click()
# time.sleep(3)
# basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
# basket_btn.click()
# time.sleep(3)
# product_remove = driver.find_element_by_css_selector("td.product-remove > a")
# product_remove.click()
# time.sleep(3)
# undo = driver.find_element_by_css_selector(".woocommerce-message > a")
# undo.click()
# time.sleep(3)
# quantity = driver.find_element_by_css_selector(" .quantity > input")
# quantity.clear()
# quantity.send_keys("3")
# basket_update = driver.find_element_by_css_selector("[name='update_cart']")
# basket_update.click()
# time.sleep(3)
# quantity = driver.find_element_by_css_selector(" .quantity > input")
# quantity_value = quantity.get_attribute("value")
# assert quantity_value == "3"
# # пункт 11 не делала, так как в моём интерфейсе не возникает сообщение "Please enter a coupon code."
#
# driver.quit()

# Покупка товаров
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

menu_shop = driver.find_element_by_id("menu-item-40")
menu_shop.click()
driver.execute_script("window.scrollBy(0, 300);")
add_btn = driver.find_element_by_css_selector(".post-165  > a:nth-child(2)")
add_btn.click()
time.sleep(3)
basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
basket_btn.click()
checkout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button"))
)
checkout.click()

first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("Kristina")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Cvet")
email = driver.find_element_by_id("billing_email")
email.send_keys("super@mail.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("88887778888")
country_select_btn = driver.find_element_by_id("select2-chosen-1")
country_select_btn.click()
country_select_field = driver.find_element_by_id("s2id_autogen1_search")
country_select_field.send_keys("Russia")
time.sleep(3)
country_select_russia = driver.find_element_by_class_name("select2-match")
country_select_russia.click()
adress = driver.find_element_by_css_selector("p #billing_address_1")
adress.send_keys("Big Street")
city = driver.find_element_by_css_selector("p #billing_city")
city.send_keys("Saint-Petersburg")
state = driver.find_element_by_id("billing_state")
state.send_keys("Russia")
postcode = driver.find_element_by_css_selector("p #billing_postcode")
postcode.send_keys("197095")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
check_pay = driver.find_element_by_css_selector("li.payment_method_cheque > input")
check_pay.click()
driver.execute_script("window.scrollBy(0, 100);")
place_order = driver.find_element_by_id("place_order")
place_order.click()

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element
    ((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received.")
)
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element
    ((By.CSS_SELECTOR, "ul.order_details .method"), "Check Payments")
)

driver.quit()
