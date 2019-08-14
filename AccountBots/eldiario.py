# -*- coding: utf-8 -*-

from time import sleep
import names
from random import randrange,randint
from random import uniform
from random import shuffle
from VolatileInbox import VolatileMail
from bot import Bot
from driverManager import driverManager
import obfuscate
from termcolor import colored
from db import cryptoDB


class ElDiario(Bot):

    def __init__(self, driver):
        self.driver = driver
        self.user = None
        self.pwd = None
        self.email = None
        self.name = None
        self.last_name = None

    def signup(self, headless=False):

        m = VolatileMail.TempAddrMail(headless=headless)

        self.email = m.getEmailAddr()
        self.name = names.get_first_name().lower()
        self.last_name = names.get_last_name().lower()

        username_list = [self.last_name, '_' , randint(80, 99)]
        shuffle(username_list)

        stringlist= ''

        for element in username_list:
            stringlist += str(element)

        self.user = self.name + stringlist

        # ELDIARIO maximum username length
        if self.user.__len__() > 12:
            self.user = self.user[:11]

        self.pwd = obfuscate.rot47(self.user)

        print (" User e-mail is: " + self.email)

        d = driverManager(self.driver)

        d.run(headless=headless)
        d.driver.get('https://usuarios.eldiario.es/registro#!/registro')
        sleep(float(randint(3,5)) + uniform(0,1))
        mail = d.driver.find_element_by_name('email')
        button = d.driver.find_element_by_id("btnSubmit")
        agree = d.driver.find_element_by_name('userAgree')

        mail.send_keys(self.email)
        #sleep(float(randint(2,3)) + uniform(0,1))
        agree.click()
        #sleep(float(randint(0, 3)) + uniform(0, 1))

        button.click()

        # Fill-in information
        sleep(float(randint(1, 2)) + uniform(0, 1))
        elements  = 0

        while (elements == 0):
            nick = d.driver.find_elements_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[1]/div[1]/input')
            elements = nick.__len__()
            sleep(1)

        nombre = d.driver.find_element_by_name("name")
        apellidos = d.driver.find_element_by_name('surname')
        pw = d.driver.find_element_by_name('pw')
        button = d.driver.find_element_by_id("btnSubmit")

        nick[0].send_keys(self.user)
        #sleep(float(randint(0, 1)) + uniform(0, 1))
        nombre.send_keys(self.name)
        #sleep(float(randint(0, 1)) + uniform(0, 1))
        apellidos.send_keys(self.last_name)
        #sleep(float(randint(0, 1)) + uniform(0, 1))
        pw.send_keys(self.pwd)
        #sleep(float(randint(0, 1)) + uniform(0, 1))

        button.click()

        # VERIFY

        href = m.verify(page='eldiario')
        print (colored("[+]", "green") + (" Account confirmation link is: " + href))
        d.driver.get(href)

        print (colored("[+]", "green") + (" Account confirmed. :). Putting the new user into DB..."))

        cryptoDB.insert_user("eldiario", self.user, self.pwd, self.email)

        print (colored("[+]", "green") + (" User added successfully into DB"))

        d.stop()

        return

    def login(self, headless=False):

        d = driverManager(self.driver)

        d.run(headless=headless)
        d.driver.get('https://usuarios.eldiario.es/?#!/iniciar-sesion')
        sleep(float(randint(3,5)) + uniform(0,1))
        mail = d.driver.find_element_by_name('email')
        pw = d.driver.find_element_by_name('password')
        button = d.driver.find_element_by_id("btnSubmit")

        print (colored("[+]", "green") + (" Selecting a random user from the DB to log in..."))

        user = cryptoDB.get_random_user("eldiario")

        reg_pwd = user[2]
        reg_mail = user[3]

        mail.send_keys(reg_mail)
        sleep(float(randint(0, 1)) + uniform(0, 1))
        pw.send_keys(reg_pwd)

        button.click()

        sleep(1)

        print (colored("[+]", "green") + (" User logged successfully."))

        return d

    def post_comment(self, url, comment, d, headless=False):

        d.driver.get(url)

        print (colored("[+]", "green") + (" Posting the comment in the newspaper..."))

        text = d.driver.find_element_by_id('edi_comment-text')
        button = d.driver.find_element_by_id('edi-comment-button')
        text.send_keys(comment)
        cookies = d.driver.find_elements_by_xpath("/html/body/div[11]/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/button")
        cookies2 = d.driver.find_elements_by_xpath("//*[text()='Aceptar']")
        if (cookies.__len__() > 0):
            cookies[0].click()

        button.click()

        print (colored("[+]", "green") + (" Comment posted successfully."))


if __name__ == "__main__":

    ed = ElDiario('firefox')
    ed.signup(headless=False)
    driver = ed.login(headless=False)

    url = raw_input("Introduce la URL de la noticia: ")
    comment = raw_input("Introduce tu comentario en la noticia: ")

    ed.post_comment(url, comment, driver, headless=False)

