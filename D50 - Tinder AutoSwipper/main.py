from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

fb_user = 'messier.spheroid@gmail.com'
fb_password = '*Applepass91*'

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://tinder.com/')

time.sleep(2)
base_window = driver.current_window_handle
assert len(driver.window_handles) == 1
login_button = driver.find_element_by_xpath('//*[@id="s1107296492"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

time.sleep(2)
fb_login = driver.find_element_by_xpath('//*[@id="s-621084584"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

time.sleep(2)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(5)
username_input = driver.find_element_by_id('email')
username_input.send_keys(fb_user)
userpass_input = driver.find_element_by_id('pass')
userpass_input.send_keys(fb_password)
userpass_input.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)

time.sleep(2)
repress_fblogin = driver.find_element_by_xpath('//*[@id="s-621084584"]/div/div/div[1]/div/div[3]/span/div[2]/button')
repress_fblogin.click()

time.sleep(5)
share_loc_button = driver.find_element_by_xpath('//*[@id="s-621084584"]/div/div/div/div/div[3]/button[1]')
share_loc_button.click()

time.sleep(2)
dont_enable_notifications_button = driver.find_element_by_xpath('//*[@id="s-621084584"]/div/div/div/div/div[3]/button[2]')
dont_enable_notifications_button.click()

time.sleep(2)
set_location = driver.find_element_by_xpath('//*[@id="s-621084584"]/div/div/div[1]/a')
set_location.click()

time.sleep(2)
like_recieved = driver.find_element_by_xpath('//*[@id="s-621084584"]/div/div/div/div[3]/button[2]')
like_recieved.click()

time.sleep(2)
select_current_city = driver.find_element_by_xpath('//*[@id="s1107296492"]/div/div[1]/div/main/div[1]/div/div/div[2]/button')
select_current_city.click()

time.sleep(2)
i_accept_cookies = driver.find_element_by_xpath('//*[@id="s1107296492"]/div/div[2]/div/div/div[1]/button')
i_accept_cookies.click()

for n in range(100):
    time.sleep(2)

    try:
        print('called')
        like_button = driver.find_element_by_xpath('//*[@id="s1107296492"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_button.click()

    # catches the case where there is a 'Matched' pop-up in from of the 'like' button
    except ElementClickInterceptedException:
        try:

            match_popup = driver.find_element_by_xpath('//*[@id="t-880314588"]/div/div/div[1]/div/div[4]/button')
            match_popup.click()

            add_to_homescreen = driver.find_element_by_xpath('//*[@id="t--1349883856"]/div/div/div[2]/button[2]')
            match_popup.click()

            send_superlike = driver.find_element_by_xpath('//*[@id="t--1349883856"]/div/div/button[1]')
            send_superlike.click()

        # catches the cases where the 'like' button has not yet loaded, so wait 2 seconds before retrying
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
