# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.firefox.options import Options
import subprocess
from random import  randint
from fake_useragent import UserAgent

class driverManager(object):

    def __init__(self, driver='firefox'):
        self.engine = driver
        self.driver = None

    def run(self, headless=False):
        options = Options()
        options.headless = headless
        # Point the path to the geckodriver bin in your system
        execgeckopath = '/root/Utilities/webDrivers/geckodriver'
        if (self.engine == 'firefox'):
            fp = webdriver.FirefoxProfile()
            fp.set_preference("network.proxy.type", 0)

            fp.set_preference("network.proxy.socks", "")
            fp.set_preference("network.proxy.socks_port", 0)

            fp.set_preference("network.proxy.socks_remote_dns", False)
            self.driver = webdriver.Firefox(options=options, executable_path=execgeckopath)
        elif (self.engine == 'firefox-torproxy'):
            generic_useragent = UserAgent()
            subprocess.call(["service", "tor", "start"])
            fp = webdriver.FirefoxProfile()
            fp.set_preference("general.useragent.override", generic_useragent.random)
            fp.set_preference("network.proxy.type", 1)

            fp.set_preference("network.proxy.socks", "127.0.0.1")
            fp.set_preference("network.proxy.socks_port", 9050)

            fp.set_preference("network.proxy.socks_remote_dns", True)

            options = Options()
            options.headless = headless

            # Point the path to the geckodriver bin in your system
            execgeckopath = '/root/Utilities/webDrivers/geckodriver'
            self.driver = webdriver.Firefox(options=options, executable_path=execgeckopath, firefox_profile=fp)

        self.driver.set_window_size(1024 + randint(0,256), 718 + randint(0,256))
        self.driver.set_window_position(randint(0,128), randint(0,128))


    def stop(self):
        self.driver.close()
        if (self.engine == 'firefox-torproxy'):
            subprocess.call(["service", "tor", "stop"])

if __name__ == "__main__":

    d = driverManager(driver='firefox-torproxy')
    d.run()
    d.driver.get('https://check.torproject.org/')