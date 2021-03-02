import time
from webbot import *
import argparse
import sys


def getOptions(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(
        description="This bot helps users to mass report accounts with clickbaits or objectionable material.")
    parser.add_argument("-u", "--username", type=str,
                        default="", help="Username to report.")
    parser.add_argument("-f", "--file", type=str, default="acc.txt",
                        help="Accounts list ( Defaults to acc.txt in program directory ).")
    options = parser.parse_args(args)
    return options


args = getOptions()

username = args.username
acc_file = args.file

if username == "":
    username = input("Username to report: ")

a = open(acc_file, "r").readlines()
file = [s.rstrip()for s in a]
file.reverse()

user = []
passw = []
for lines in file:
    file = lines.split(":")

    un = file[0]
    pw = file[1]
    user.append(un)
    passw.append(pw)


for line in range(len(user)):
    web = Browser()
    print("Reporting with User: "+user[line])
    try:
        web.go_to("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        web.click(text='Phone number, username, or email', tag='span')
        web.type(
            user[line], into="Phone number, username, or email")

        time.sleep(2)
        web.press(web.Key.TAB)
        time.sleep(2)
        web.type(passw[line], into='Password')
        web.press(web.Key.ENTER)

        time.sleep(5)

        web.go_to("https://www.instagram.com/%s/" % username)

        time.sleep(2)

        web.click(
            xpath='//button[contains(@class,\"wpO6b\")]')

        time.sleep(2)

        web.click(text='Report User')

        time.sleep(2)

        web.click(xpath="//button[contains(@class,\"b5k4S\")][1]")

        time.sleep(2)

        web.click(text='Close')

        time.sleep(2)

        web.driver.close()
    except:
        print("Error Encountered")
