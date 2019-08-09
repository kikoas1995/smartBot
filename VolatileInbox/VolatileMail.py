# -*- coding: utf-8 -*-
from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.firefox.options import Options
import sys
sys.path.append('../')
import re


class TempAddrMail:

    # Added functionality of https://www.getnada.com.
    # It is a volatile email service that is not banned from most websites.
    def __init__(self, headless=False):
        options = Options()
        options.headless = headless
        path = '/root/Utilities/webDrivers/geckodriver'
        self.driver = webdriver.Firefox(options=options, executable_path=path)
        self.driver.get('https://getnada.com/#')
        sleep(2)


    def getEmailAddr(self,):
        mail_xpath = "/html/body/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/h1/span[2]"

        element = self.driver.find_element_by_xpath(mail_xpath)
        return element.text

    def verify(self, page):

        if (page == 'eldiario'):
            sleep(5)
            while(1):
                    elements2 = self.driver.find_elements_by_xpath("//*[contains(text(), 'eldiario')]")
                    elements = self.driver.find_elements_by_xpath("//*[contains(text(), 'diario')]")
                    if (elements2.__len__() > 0):
                        elements2[0].click()
                        sleep(1)
                        self.driver.switch_to.frame("idIframe")
                        while (1):
                            elements = self.driver.find_elements_by_xpath("//a[contains(text(), 'este')]")
                            if (elements.__len__() > 0):
                                href = elements[0].get_attribute("href")
                                return href

        elif (page == 'elmundo'):
            sleep(5)
            while (1):
                elements = self.driver.find_elements_by_xpath("//*[contains(text(), 'elmundo')]")
                if (elements.__len__() > 0):
                    elements[0].click()
                    sleep(1)
                    self.driver.switch_to.frame("idIframe")
                    while (1):
                        elements = self.driver.find_elements_by_xpath("//a[contains(text(), 'seguro.elmundo')]")
                        if (elements.__len__() > 0):
                            href = elements[0].get_attribute("href")
                            return href


        self.driver.close()
        return str.partition(" ")[0]

if __name__ == "__main__":

    x = 0