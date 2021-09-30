# Twitter-a-complaint-at-ISP-over-Internet-Speeds
The code in the main.py file uses OOP to create a class for a twitter complaint bot. The purpose of the code was to use Selenium Webdriver in order to automate the code that is run, and for web scraping to obtain data needed for the project.
# Project Steps
Using Chrome Driver and Selenium Webdriver, I was able to create a twitter complaint bot via the class of InternetSpeedTwitterBot. This class has several functions, the first being to obtain our current internet speed using the tools provided by speedtest.net. The second function is used to compose and post a tweet, containing the internet upload and download speeds, through your own personal twitter account, if called.
The main portion of the code is quite concise. All that is needed is to create your own object from InternetSpeedTwitterBot, gather the internet speed, and if the download speed is below the speed guaranteed by your ISP, your bot will call the function to compose and post a tweet.
