
import time

from selenium import webdriver

driver=webdriver.Chrome("C:\SeleniumDrivers\chromedriver.exe")

time.sleep(3)
driver.maximize_window()
driver.get("https://www.amazon.com/")

element=driver.find_element_by_id("twotabsearchtextbox")
element.send_keys("oppo Mobiles")
time.sleep(3)

element=driver.find_element_by_id("nav-search-submit-button")
element.click()

element=driver.find_element_by_class_name("s-image")
element.click()

element=driver.find_element_by_id("buy-now-button")
element.click()

element=driver.find_element_by_name("email")
element.send_keys("malikzain909192@gmail.com")

element=driver.find_element_by_id("continue")
element.click()

element=driver.find_element_by_id("ap_password")
element.send_keys("Zain90Ali909192")

element=driver.find_element_by_id("signInSubmit")
element.click()

element=driver.find_element_by_class_name("address-ui-widgets-desktop-button-text")
element.click()

element=driver.find_element_by_class_name("a-button-input")
element.click()


# testing gmail

# driver.get("https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&dsh=S118178798%3A1660535577201350&biz=false")
#
# element=driver.find_element_by_class_name("whsOnd")
# element.send_keys("Zain")
# time.sleep(2)
#
# element=driver.find_element_by_name("lastName")
# element.send_keys("Ali")
# time.sleep(2)
#
# element=driver.find_element_by_id("username")
# element.send_keys("Zain31Ali32")
# time.sleep(2)
#
#
# element=driver.find_element_by_name("Passwd")
# element.send_keys("Gmailpassword123*")
# time.sleep(2)
#
# element=driver.find_element_by_name("ConfirmPasswd")
# element.send_keys("Gmailpassword123*")
# time.sleep(2)
#
# # check box clicking
# element=driver.find_element_by_class_name("VfPpkd-muHVFf-bMcfAe")
# element.click()
# time.sleep(2)
#
# # next button clicking
# element=driver.find_element_by_class_name("VfPpkd-vQzf8d")
# element.click()
#
#
#
# element=driver.find_element_by_id("phoneNumberId")
# element.send_keys("03123345678")
# time.sleep(2)
#
# # clicking next button
# element=driver.find_element_by_class_name("VfPpkd-RLmnJb")
# element.click()
#






