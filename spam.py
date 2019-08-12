from selenium import webdriver
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import time

"""
Discord Server Messages:

Nia Nation => "Come join Nia Nation a chill server with random conversation and a lot of chill people. Pedos will be exposed, if you think we’re talking about you we probably are. https://discord.gg/6xdf6C4"
Merc's Server => "Growing server, pretty new. for anyone and everyone. theres a wide variety of topics, our sense of humor can be weird/offensive youve been warned https://discord.gg/JKPPpp"
"""

DISC_MODE = True # Discord Mode

if (DISC_MODE):
      interest = "discord"
      msg = "Come join Nia Nation a chill server with random conversation and a lot of chill people. Pedos will be exposed, if you think we’re talking about you we probably are. https://discord.gg/6xdf6C4"
else:
      interest = input("Enter the interests seperate by a comma >> ")
      msg = input("You're message goes here >> ")

driver = webdriver.Firefox()


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def main():
      try:
            driver.get('http://www.omegle.com')
            time.sleep(2)
            driver.find_element_by_xpath('//textarea[@rows="3"]').clear()
            message = driver.find_element_by_xpath('//textarea[@rows="3"]')
            message.send_keys(msg)
            send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
            send.click()

            disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
            disconnect.click()
            disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
            disconnect.click()
            disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
            disconnect.click()
      except (InvalidElementStateException, UnexpectedAlertPresentException):
            main2()


def main2():
      try:
            driver.get('http://www.omegle.com')
            interest1 = driver.find_element_by_xpath('//input[@class="newtopicinput"]')
            interest1.send_keys(interest)
            btn = driver.find_element_by_id("textbtn")
            btn.click()
            time.sleep(2)

            while (check_exists_by_xpath('//div[@class="commonlikescancel"]')):
                  pass

            ### DETECTING CAPTCHA
            if (check_exists_by_xpath('//div[@class="rc-anchor"]')):
                  print("SOLVE THE CAPTCHA!!!")
            else:
                  print("CAPTCHA SOLVED!!!")

            driver.find_element_by_xpath('//textarea[@rows="3"]').clear()
            message = driver.find_element_by_xpath('//textarea[@rows="3"]')
            message.send_keys(msg)

            send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
            send.click()

            disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
            disconnect.click()

      except (InvalidElementStateException, UnexpectedAlertPresentException):
            disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
            disconnect.click()
      else:
            main2()

while True:
      try:
            main2()
      except (InvalidElementStateException, UnexpectedAlertPresentException):
            main()
