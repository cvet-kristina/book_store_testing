# # Отображение страницы товара
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
# book_html_5_forms = driver.find_element_by_class_name("post-181")
# book_html_5_forms.click()
# book_title = driver.find_element_by_class_name("entry-title")
# assert book_title.text == "HTML5 Forms"
#
# driver.quit()
