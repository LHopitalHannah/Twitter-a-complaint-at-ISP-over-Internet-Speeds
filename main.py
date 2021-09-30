from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_driver_path = YOUR_CHROME_DRIVER_PATH

PROMISED_DOWN = 150
PROMISED_UP = 10
twitter_email = YOUR_TWITTER_EMAIL
twitter_password = YOUR_TWITTER_PASSWORD


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net')
        sleep(7)
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        sleep(20)
        self.down = float(self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        sleep(2)
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        sleep(2)
        return f" My ISP has not followed what they guaranteed. They guaranteed {PROMISED_DOWN} Mbps and {PROMISED_UP} Mbps." \
               f"The current speeds are: down: {self.down}\nup:{self.up}"


    def tweet_at_ISP(self, results):
        self.driver.get('https://twitter.com/home')
        sleep(6)
        username = self.driver.find_element_by_name('username')
        username.send_keys(twitter_email)
        username.send_keys(Keys.ENTER)
        sleep(2)
        password = self.driver.find_element_by_name('password')
        password.send_keys(twitter_password)
        password.send_keys(Keys.ENTER)
        sleep(5)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_button.click()
        sleep(1)
        whats_happening = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div[1]/div')
        whats_happening.send_keys(results)
        sleep(2)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div[3]/div')
        tweet_button.click()


# main code
my_bot = InternetSpeedTwitterBot(chrome_driver_path)
results_from_speed = my_bot.get_internet_speed()
if my_bot.down < PROMISED_DOWN:
    my_bot.tweet_at_ISP(results_from_speed)