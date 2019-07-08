# -*- coding: utf-8 -*-
from samba.dcerpc.smb_acl import user
from selenium import webdriver
import os
from time import sleep
import names
from random import randrange,randint
from random import choice
from random import uniform
from random import shuffle
from string import ascii_lowercase, digits
from VolatileInbox import VolatileMail
from bot import Bot
from driverManager import driverManager
import obfuscate

class Instagram(Bot):

    def __init__(self, driver):
        self.driver = driver
        self.user = None
        self.pwd = None
        self.email = None
        self.name = None
        self.last_name = None

    def signup(self, driver='firefox-torproxy'):

        m = VolatileMail.TempAddrMail()

        self.email = m.getEmailAddr()
        self.name = names.get_first_name().lower()
        self.last_name = names.get_last_name().lower()

        username_list = [self.last_name, '_' , randint(80, 99)]
        shuffle(username_list)

        stringlist= ''
        for element in username_list:
            stringlist += str(element)

        self.user = self.name + stringlist

        # IG maximum username length
        if self.user.__len__() > 12:
            self.user = self.user[:11]

        self.pwd = obfuscate.rot47(self.user)

        print ("User e-mail is: " + self.email)

        d = driverManager(driver)

        d.run(headless=False)

        d.driver.get('https://www.instagram.com/accounts/emailsignup/')
        sleep(float(randint(3,5)) + uniform(0,1))
        mail = d.driver.find_element_by_name('emailOrPhone')
        name = d.driver.find_element_by_name('fullName')
        user = d.driver.find_element_by_name('username')
        pwd = d.driver.find_element_by_name('password')
        button = d.driver.find_elements_by_tag_name("button")[1]

        sleep(float(randint(2,3)) + uniform(0,1))
        name.send_keys(self.name + ' ' + self.last_name)
        sleep(float(randint(2,3)) + uniform(0,1))
        user.send_keys(self.user)
        sleep(float(randint(2,3)) + uniform(0,1))
        mail.send_keys(self.email)
        sleep(float(randint(2,3)) + uniform(0,1))
        pwd.send_keys(self.pwd)
        sleep(float(randint(2,3)) + uniform(0,1))

        len = 1
        while (len > 0):
            try:
                button.click()
                sleep(randrange(1,5))
                e = driver.find_elements_by_xpath("//*[contains(text(), 'Sorry, ')]")
                len = e.__len__()
                if (len > 0):
                    user.clear()
                    sleep(randrange(1, 3))
                    user.send_keys(reg_user + ''.join(choice(ascii_lowercase + digits) for _ in range(3)))
            except:
                break
        sleep(2)
        elements = driver.find_elements_by_xpath("//*[contains(text(), 'Skip')]")

        for element in elements:
            try:
                element.click()
                sleep(randrange(3,6))
            except:
                continue

        insert_user("instagram", reg_user, reg_pwd, reg_mail)
        driver.close()

        return

    def login(self):
        script_dir = os.path.dirname(__file__)
        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        driver = webdriver.Firefox(executable_path=path)
        random_user = get_random_user("instagram")
        driver.get('https://www.instagram.com/accounts/login/?hl=es')
        sleep(3)
        user = driver.find_element_by_name('username')
        pwd = driver.find_element_by_name('password')

        reg_user = random_user[3]
        reg_pwd = random_user[2]

        user.send_keys(reg_user)
        sleep(randrange(1, 3))
        pwd.send_keys(reg_pwd)
        sleep(randrange(1, 3))

        elements = driver.find_elements_by_xpath("//*[contains(text(), 'Iniciar ')]")

        for ele in elements:
            if ele.is_displayed():
                ele.click()
                sleep(randrange(3,5))

        return driver

    def stalk(self, user):

        driver = self.login()

        driver.get('https://www.instagram.com/' + user)

        elements = driver.find_elements_by_xpath("//*[contains(text(), 'Follow')]")
        for ele in elements:
            if ele.is_displayed():
                ele.click()
                sleep(randrange(3,5))
        driver.get('https://www.instagram.com/')
        sleep(randrange(5,7))

        """x = driver.find_elements_by_xpath("//*[text()='x']")
        for ele in x:
            if ele.is_displayed():
                ele.click()
                sleep(randrange(3, 5))"""

        elements = driver.find_elements_by_xpath("//*[contains(text(), 'Like')]")
        fr = 0
        to = 500

        while(1):
            for e in elements:
                if e.is_displayed():
                    sleep(1)
                    e.click()
                    sleep(randrange(1,2))

            if elements.__len__() == 0:
                break

            for _ in range(0, 2):
                driver.execute_script("window.scrollTo(" + str(fr) + ", " + str(to) + ")")
                sleep(randrange(1,3))
                fr += 500
                to += 500
            sleep(randrange(1,3))
            elements = driver.find_elements_by_xpath("//*[contains(text(), 'Like')]")
            sleep(randrange(1, 3))

    def getConfirmation(self, email):

        tm = TempMail()
        # print email
        while (1):
            box = tm.get_mailbox(email)  # list of emails
            if type(box) is dict:
                # print "Waiting for mails"
                sleep(10)
            elif type(box) is list:
                # print box[0]['mail_text']
                m = re.findall('\n\d+\n', box[0]['mail_text'])
                return m[0][1:-1]



if __name__ == "__main__":

    instagram = Instagram()
    instagram.signup()
    instagram.stalk("natgeo")