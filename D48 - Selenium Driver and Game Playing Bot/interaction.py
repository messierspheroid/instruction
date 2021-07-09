from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

# # use "#" to target ids if a parent class is not available
# article_count = driver.find_element_by_css_selector("#articlecount a")
# article_count.click()

# # find method that is specific to links
# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# # typing in an input, need "name"
# search = driver.find_element_by_name("search")
# # type into a field
# search.send_keys("Python")
# # import "from selenium.webdriver.common.keys import Keys" to use use commands
# search.send_keys(Keys.ENTER)

f_name_input = driver.find_element_by_name("fName")
f_name_input.send_keys("Chad")

l_name_input = driver.find_element_by_name("lName")
l_name_input.send_keys("Bjornberg")

email_input = driver.find_element_by_name("email")
email_input.send_keys("bjornbergchad@gmail.com")

signup = driver.find_element_by_class_name("btn")
signup.click()
