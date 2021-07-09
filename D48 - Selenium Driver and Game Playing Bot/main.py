# you have to import selenium first, then reformat to below
from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# there will be a different driver for all browsers
# for mac you have to disable privacy settings for chrome driver

# open a window and go to website
driver.get("https://www.python.org/")

# # find an HTML element in browser
# price = driver.find_element_by_id("priceblock_dealprice")
# print(price.text)

# # this will print out the selenium element
# search_bar = driver.find_element_by_name("q")
# # search_bar.tag_name == "input" tag
# # search_bar.get_attribute that you specify
# # this will also allow you to find out values in HTML
# print(search_bar)

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# # look for a parent class
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# # sometimes it is hard to find a CSS selector, right-click inline HTML tag, copy --> copy xpath
# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# id > name > class

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
    print(events)

# close a window
# driver.close()
# close out browsers entirely
driver.quit()
