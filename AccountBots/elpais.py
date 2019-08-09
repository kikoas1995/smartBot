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


class ElPais(Bot):

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

        d.driver.get('https://plus.elpais.com/registro/')

        name = d.driver.find_element_by_name('Name')
        name.send_keys(self.name)
        sleep(float(randint(0, 1)) + uniform(0, 1))
        lastn = d.driver.find_element_by_name('LastName1')
        lastn.send_keys(self.last_name)
        sleep(float(randint(0, 1)) + uniform(0, 1))
        mail= d.driver.find_element_by_name('Email1')
        mail.send_keys(self.email)
        sleep(float(randint(0, 1)) + uniform(0, 1))
        pwd = d.driver.find_element_by_name('Password')
        pwd.send_keys(self.pwd)
        sleep(float(randint(0, 1)) + uniform(0, 1))
        pwd = d.driver.find_element_by_name('Password2')
        pwd.send_keys(self.pwd)
        sleep(float(randint(0, 1)) + uniform(0, 1))
        dia = d.driver.find_element_by_id('dia')
        dia.send_keys(randint(1,26))
        sleep(float(randint(0, 1)) + uniform(0, 1))
        mes = d.driver.find_element_by_id('mes')
        mes.send_keys(randint(1,12))
        sleep(float(randint(0, 1)) + uniform(0, 1))
        agno = d.driver.find_element_by_id('agno')
        agno.send_keys(randint(1975,1999))
        sleep(float(randint(0, 1)) + uniform(0, 1))
        checkbox = d.driver.find_element_by_id('Privacity')
        checkbox.click()
        sleep(float(randint(0, 1)) + uniform(0, 1))
        regButton = d.driver.find_element_by_name('submit1')
        regButton.click()

        link = m.verify(page='elpais')

        d.driver.get(link)


        return

    def login(self, headless=False):

        d = driverManager(self.driver)

        d.run(headless=headless)
        d.driver.get('https://usuarios.eldiario.es/?#!/iniciar-sesion')
        sleep(float(randint(3,5)) + uniform(0,1))
        mail = d.driver.find_element_by_name('email')
        pw = d.driver.find_element_by_name('password')
        button = d.driver.find_element_by_id("btnSubmit")

        print (colored("[+]", "green") + (" Seleccionando un usuario aleatorio de la base de datos para logarse..."))

        user = cryptoDB.get_random_user("eldiario")

        reg_pwd = user[2]
        reg_mail = user[3]

        mail.send_keys(reg_mail)
        sleep(float(randint(0, 1)) + uniform(0, 1))
        pw.send_keys(reg_pwd)

        button.click()

        sleep(1)

        print (colored("[+]", "green") + (" Usuario logueado correctamente."))

        return d

    def post_comment(self, url, comment, d, headless=False):

        d.driver.get(url)

        print (colored("[+]", "green") + (" Posteando comentario en la noticia..."))

        text = d.driver.find_element_by_id('edi_comment-text')
        button = d.driver.find_element_by_id('edi-comment-button')
        text.send_keys(comment)
        cookies = d.driver.find_element_by_xpath("/html/body/div[12]/div[1]/div/div[2]/div/button")

        cookies.click()
        button.click()

        print (colored("[+]", "green") + (" Comentario posteado con éxito."))


if __name__ == "__main__":

    em = ElPais('firefox-torproxy')
    em.signup(headless=False)

    #driver = em.login(headless=False)

    #url = raw_input("Introduce la URL de la noticia: ")
    #comment = raw_input("Introduce tu comentario en la noticia: ")

    #ed.post_comment(url, comment, driver, headless=False)

