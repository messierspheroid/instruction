from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
speedtest_url = "https://www.speedtest.net/"

twitter_login_url = "https://twitter.com/login"
twitter_user = "messierspheroid"
twitter_pass = "*Applepass91*"

account_dl = 600
account_ul = 15

class InternetSpeedTwitterBot():

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.download_result_text = 0
        self.upload_result_text = 0

    def get_internet_speed(self):
        self.driver.get(speedtest_url)
        self.driver.set_window_size(700, 500)

        time.sleep(3)
        start_speedtest_button = self.driver.find_element_by_xpath(
            "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        start_speedtest_button.click()

        time.sleep(50)
        self.download_result_text = self.driver.find_element_by_xpath(
            "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        print(self.download_result_text)
        self.upload_result_text = self.driver.find_element_by_xpath(
            "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text
        print(self.upload_result_text)

    def tweet_at_provider(self):
        if float(self.download_result_text) < account_dl or float(self.upload_result_text) < account_ul:
            with open("C:/Users/chade/Google Drive/xfinity_speeds.txt", mode="a") as data_file:
                data_file.write(f"{self.download_result_text}, {self.upload_result_text}\n")

        self.driver.get(twitter_login_url)
        time.sleep(3)
        t_user_input = self.driver.find_element_by_name("session[username_or_email]")
        t_user_input.send_keys(twitter_user)
        t_user_pass = self.driver.find_element_by_name("session[password]")
        t_user_pass.send_keys(twitter_pass)
        t_user_pass.send_keys(Keys.ENTER)

        time.sleep(3)
        t_text_field = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div")
        t_text_field.send_keys(f"Hey @Xfinity, why is my internet speed "
                               f"{self.download_result_text}down/{self.upload_result_text}up when I pay for {account_dl}down/{account_ul}up?")

        time.sleep(2)
        t_button_post = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]").click()


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()
