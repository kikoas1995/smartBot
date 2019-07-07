import time
from tempMail import tempMail
import re


class TemporaryMail():

    def __init__(self, user=None):
        self.inbox = tempMail.mailer()

    def print_email_addr(self):
        print("Direccion de email:" + self.inbox.getEmail())

    def wait_for_all_mails(self):
        while 1:
            result = self.inbox.mailBox()
            if result:
                print result
            time.sleep(10)

    def mail_matches_regex(self, regex):
        while 1:
            result = self.inbox.mailBox()
            matches = re.search(regex, result)
            if matches:
                print result
                return
            time.sleep(5)

if __name__ == "__main__":
    import time
    from tempMail import tempMail

    m = tempMail.mailer()
    email_address = m.getEmail()
    print 'E-mail: %s' % email_address

    while 1:
        result = m.mailBox()
        if result:
            print result
        time.sleep(2)