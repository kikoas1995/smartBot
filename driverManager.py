# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.firefox.options import Options
import subprocess


class driverManager(object):

    def __init__(self, driver='geckodriver'):
        self.engine = driver
        self.driver = None

    def run(self, headless=False):
        options = Options()
        options.headless = headless
        # Point the path to the geckodriver bin in your system
        execgeckopath = '/root/Utilities/webDrivers/geckodriver'
        if (self.engine == 'geckodriver'):
            self.driver = webdriver.Firefox(options=options, executable_path=execgeckopath)
        elif (self.engine == 'firefox-torproxy'):
            fp = webdriver.FirefoxProfile()
            fp.set_preference("network.proxy.type", 1)

            fp.set_preference("network.proxy.socks", "127.0.0.1")
            fp.set_preference("network.proxy.socks_port", 9050)

            fp.set_preference("network.proxy.socks_remote_dns", True)

            options = Options()
            options.headless = self.headless

            # Point the path to the geckodriver bin in your system
            execgeckopath = '/root/Utilities/webDrivers/geckodriver'
            self.driver = webdriver.Firefox(options=options, executable_path=execgeckopath, firefox_profile=fp)

        #
        # TODO: Add compatibility for more webdrivers
        #

    def stop(self):
        self.driver.close()
        if (self.engine == 'firefox-torproxy'):
            subprocess.call(["service", "tor", "stop"])

if __name__ == "__main__":

    d = driverManager(driver='firefox-torproxy')
    subprocess.call(["service", "tor", "start"])
    d.run()
    d.driver.get('https://check.torproject.org/')