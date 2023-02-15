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