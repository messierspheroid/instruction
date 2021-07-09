from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
insta_login = "https://www.instagram.com/accounts/login/"
follower_mine = "https://www.instagram.com/aliabdaal/"

user = "messier.spheroid@gmail.com"
pass_ = "*Applepass93*"


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.user = user
        self.pass_ = pass_
        self.insta_login = insta_login

    def login(self):
        self.driver.get(self.insta_login)
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        username.send_keys(self.user)
        password = self.driver.find_element_by_name("password")
        password.send_keys(self.pass_)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        # user account interested in
        time.sleep(5)
        self.driver.get(follower_mine)

        # popup follower list
        time.sleep(3)
        followers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        followers.click()

        # for loop follower list
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for click in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_element_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
                cancel_button.click()
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()


