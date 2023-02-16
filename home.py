# Добавление комментария
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0, 600);")
book_selenium_ruby = driver.find_element_by_css_selector(".post-160 > a > h3")
book_selenium_ruby.click()
book_selenium_ruby_reviews = driver.find_element_by_css_selector("[href='#tab-reviews']")
book_selenium_ruby_reviews.click()
five_stars = driver.find_element_by_css_selector(".stars > span > a:nth-child(5)")
five_stars.click()
comment_field = driver.find_element_by_id("comment")
comment_field.send_keys("Nice book!")
name_field = driver.find_element_by_id("author")
name_field.send_keys("Kristina")
email_field = driver.find_element_by_id("email")
email_field.send_keys("mail@mail.com")
submit_btn = driver.find_element_by_css_selector(".form-submit input")
submit_btn.click()

driver.quit()