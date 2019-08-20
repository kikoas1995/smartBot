# -*- coding: utf-8 -*-
from AccountBots.eldiario import ElDiario
from AccountBots.elpais import ElPais
from AccountBots.elmundo import ElMundo
from threading import Thread

class MyShell:

    def __init__(self): 
        pass

    def eval(self, cmdlist):
        cmd= cmdlist.split()
        if (cmd[0] == "register"):
            if (len(cmd) == 1):
                print("Current services available:")
                print("\teldiario")
                print("\telmundo")
                print("\texpansion")
                print("\tmarca")
            elif (cmd[1] == "eldiario"):

                headless = False
                webdriver = "firefox"

                if (cmd.__contains__("--tor")):
                    webdriver = "firefox-torproxy"
                if (cmd.__contains__("--invisible")):
                    headless = True

                ed = ElDiario(webdriver)
                ed.signup(headless=headless)

            elif (cmd[1] == "elmundo"):

                headless = False
                webdriver = "firefox"

                if (cmd.__contains__("--tor")):
                    webdriver = "firefox-torproxy"
                if (cmd.__contains__("--invisible")):
                    headless = True

                em = ElMundo(webdriver)
                em.signup(headless=headless)

            elif (cmd[1] == "expansion"):

                headless = False
                webdriver = "firefox"

                if (cmd.__contains__("--tor")):
                    webdriver = "firefox-torproxy"
                if (cmd.__contains__("--invisible")):
                    headless = True

                em = ElMundo(webdriver)
                em.signup(headless=headless)

            elif (cmd[1] == "marca"):

                headless = False
                webdriver = "firefox"

                if (cmd.__contains__("--tor")):
                    webdriver = "firefox-torproxy"
                if (cmd.__contains__("--invisible")):
                    headless = True

                em = ElMundo(webdriver)
                em.signup(headless=headless)

        elif (cmd[0] == "comment"):
            if (len(cmd) == 1):
                print("Current services available:")
                print("\teldiario")
                print("\telmundo")
                print("\texpansion")
                print("\tmarca")
            elif (cmd[1] == "eldiario"):

                headless = False
                webdriver = "firefox"
                if (cmd.__contains__("--tor")):
                    webdriver = "firefox-torproxy"
                if (cmd.__contains__("--invisible")):
                    headless = True

                ed = ElDiario(webdriver)
                d = ed.login(headless=headless)
                url = raw_input("URL of the new: ")
                comment = raw_input("Comment to introduce: ")

                ed.post_comment(url, comment, d, headless=headless)

            elif (cmd[1] == "elmundo"):

                headless = False
                webdriver = "firefox"

                if (cmd.__contains__("--tor")):
                    webdriver = "firefox-torproxy"
                if (cmd.__contains__("--invisible")):
                    headless = True

                em = ElMundo(webdriver)
                em.signup(headless=headless)

            elif (cmd[1] == "expansion"):

                headless = False
                webdriver = "firefox"

                if (cmd.__contains__("--tor")):
                    webdriver = "firefox-torproxy"
                if (cmd.__contains__("--invisible")):
                    headless = True

                em = ElMundo(webdriver)
                em.signup(headless=headless)

            elif (cmd[1] == "marca"):

                headless = False
                webdriver = "firefox"

                if (cmd.__contains__("--tor")):
                    webdriver = "firefox-torproxy"
                if (cmd.__contains__("--invisible")):
                    headless = True

                em = ElMundo(webdriver)
                em.signup(headless=headless)

        elif(cmd[0] == "quit"):
            print ("Bye =)bye")
            return 0

        elif (cmd[0] == "hiddenservice"):
            if (len(cmd) == 1):
                print("Current options for the hidden service tweaking:")
                print("\t'start': start hidden service on daemon")
                print("\t'start':")
                print("\texpansion")
                print("\tmarca")
            elif (cmd[1] == "eldiario"):

                headless = False
                webdriver = "firefox"
                if (cmd.__contains__("--tor")):
                    webdriver = "firefox-torproxy"
                if (cmd.__contains__("--invisible")):
                    headless = True

                ed = ElDiario(webdriver)
                d = ed.login(headless=headless)
                url = raw_input("URL of the new: ")
                comment = raw_input("Comment to introduce: ")

                ed.post_comment(url, comment, d, headless=headless)

            elif (cmd[1] == "elmundo"):
        else:
            print("\nUsage:")
            print("\thelp:\tShow this message")
            print("\tregister <name of service>:\t Register an anonymous user in a service and save it into local database")
            print("\tcomment <name of service>:\t post a comment with an anonymous user in a service")
            print("\tquit:\t Exit the program")
            print("\n")
        return 1

    def cmdLoop(self):
        on = 1
        while on:
            cmd = raw_input("smartBot >>> ")
            #try:
            on = self.eval(cmd)
            #except Exception as e:
             #   print("error :", e)

    def printTitle(self):
        print("                           _   ____        _   ")
        print("  ___ _ __ ___   __ _ _ __| |_| __ )  ___ | |_ ")
        print(" / __| '_ ` _ \ / _` | '__| __|  _ \ / _ \| __|")
        print(" \__ \ | | | | | (_| | |  | |_| |_) | (_) | |_ ")
        print(" |___/_| |_| |_|\__,_|_|   \__|____/ \___/ \__|")
        print("                                               ")
        print("\n")


if __name__ == '__main__':

    shell = MyShell()
    shell.printTitle()
    shell.cmdLoop()
