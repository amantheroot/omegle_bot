from selenium import webdriver
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import UnexpectedAlertPresentException
import time


# interest = input("Enter the interests seperate by a comma ")
# msg1 = input("Enter your first message (1/4) >> ")
# msg2 = input("Enter your second message (2/4) >> ")
# msg3 = input("Enter your third message (3/4) >> ")
# msg4 = input("Enter your fourth message (4/4) >> ")
interest = "discord"
msg = "LMAO EPIC LOL LMFAO"
driver = webdriver.Firefox()


def main():
      try:
            driver.get('http://www.omegle.com')
            time.sleep(2)
            driver.find_element_by_xpath('//textarea[@rows="3"]').clear()
            message = driver.find_element_by_xpath('//textarea[@rows="3"]')
            message.send_keys(msg)
            send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
            send.click()
            # message.send_keys(msg2)
            # send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
            # send.click()
            # message.send_keys(msg3)
            # send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
            # send.click()
            # message.send_keys(msg4)
            # send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
            # send.click()
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
            time.sleep(5)
            driver.find_element_by_xpath('//textarea[@rows="3"]').clear()
            message = driver.find_element_by_xpath('//textarea[@rows="3"]')
            message.send_keys(msg)
            send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
            send.click()
            # message.send_keys(msg2)
            # send.click()
            # message.send_keys(msg3)
            # send.click()
            # message.send_keys(msg4)
            # send.click()
            # send.click()
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
