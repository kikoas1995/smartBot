# -*- coding: utf-8 -*-
from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.firefox.options import Options
import sys
sys.path.append('../')
class TempAddrMail:

    # Added functionality of https://www.getnada.com.
    # It is a volatile email service that is not banned from most SSNN.
    def __init__(self):
        options = Options()
        options.headless = True
        path = '/root/Utilities/webDrivers/geckodriver'
        self.driver = webdriver.Firefox(options=options, executable_path=path)
        self.driver.get('https://getnada.com/#')
        sleep(2)


    def getEmailAddr(self,):
        mail_xpath = "/html/body/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/h1/span[2]"

        element = self.driver.find_element_by_xpath(mail_xpath)
        return element.text

    def verify(self, ):
        while(1):
                elements = self.driver.find_elements_by_css_selector(".s")
                if (elements.__len__() > 0):
                    break
                sleep(10)


        str = elements[0].text
        self.driver.close()
        return str.partition(" ")[0]

if __name__ == "__main__":

    x = 0