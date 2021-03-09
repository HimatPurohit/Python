from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome('./chromedriver')
driver.maximize_window()

# # Text box
# driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
# print(driver.title)

# driver.implicitly_wait(5)
# pop_up=driver.find_element_by_css_selector('.at-cv-button.at-cv-lightbox-yesno.at-cm-no-button')
# pop_up.click()

# # Form 1 - Show Message
# message_input= driver.find_element_by_id('user-message')
# message_input.clear()
# message_input.send_keys("Test Message 1")
# form_1=driver.find_element_by_css_selector('#get-input')
# show_message=form_1.find_element_by_css_selector('.btn.btn-default')
# show_message.click()

# # Form 2 - Get Total
# a_value=driver.find_element_by_css_selector('#sum1')
# b_value=driver.find_element_by_css_selector('#sum2')
# a_value.send_keys(5)
# b_value.send_keys(10)
# get_total=driver.find_element_by_css_selector('#gettotal > .btn.btn-default')
# get_total.click()


# Check Box
driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
print(driver.title)

checkbox_1=driver.find_element_by_css_selector('#isAgeSelected')
checkbox_1.click()
print(checkbox_1.is_selected())