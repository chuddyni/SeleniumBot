from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import datetime

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument('--headless')
# to open chrome webbrowser and maximize the window
driver = webdriver.Chrome(chrome_options=options)
# Implicit Wait when element is taking time to load
driver.implicitly_wait(2)
# connect to the specific ip address


def connect(login, password):

    driver.get("http://www.facebook.com")
    a = driver.find_element_by_id('email')

    a.send_keys(login)
    b = driver.find_element_by_id('pass')

    b.send_keys(password)
    c = driver.find_element_by_id('loginbutton')
    c.click()


def reply_messages(command):
    if command == "!BOT":
        return "Wiadomosc na !BOT"
    if command == "!BTC":
        return "Aktualny kurs BTC to " + "X $"


def crypto_course(waluta):
    return


def dzien_tygodnia():
    dzien_tygodnia = datetime.datetime.now().strftime("%A")
    return dzien_tygodnia


def numer_tygodnia():
    numer_tygodnia = datetime.datetime.now().strftime("%U")
    return int(numer_tygodnia)


def iseven(week_number):
    if week_number % 2 == 0:
        return "2/4"
    else:
        return "1/3"

# print(iseven(numer_tygodnia()))

planzajec = [
    {
        "przedmiot": "Programowanie",
        "sala": "208 B4",
        "rozpoczecie": "8:00",
        "zakonczenie": "9:30",
        "tydzien": "1/3",
        "dzien_tyg": "Tuesday",
    },
    {
        "przedmiot": "Metodyka",
        "sala": "243 B1",
        "rozpoczecie": "9:45",
        "zakonczenie": "11:15",
        "tydzien": "2/4",
        "dzien_tyg": "Tuesday"
    },
    {
        "przedmiot": "Metodyka",
        "sala": "243 B1",
        "rozpoczecie": "9:45",
        "zakonczenie": "11:15",
        "tydzien": "2/4",
        "dzien_tyg": "Tuesday"
    }
]
# print(dzien_tygodnia())
wiadomosc_bota = ["Zajęcia dziś \n "]

# Dodawanie planu zajec do wiadomosci_bota

for zajecia in planzajec:
    if zajecia["dzien_tyg"] == dzien_tygodnia() and zajecia["tydzien"] == iseven(numer_tygodnia()):
        print(zajecia["przedmiot"])
        print(zajecia["rozpoczecie"])
        print(zajecia["sala"])
        # print(iseven
        wiadomosc_bota += zajecia["przedmiot"] + " " + zajecia["rozpoczecie"] + " " + zajecia["sala"] + " "

# sleep(20)
connect("login", "password")

driver.get("https://www.facebook.com/messages/t/1974449535911266")
sleep(2)


# driver.find_element_by_xpath("//*[@data-editor]").click()
# actions = ActionChains(driver)
# actions.send_keys(wiadomosc_bota)
# actions.send_keys(Keys.RETURN)
# actions.perform()
# profilePicList = driver.find_elements_by_xpath('//*[@id="js_1"][@type="text"]')

while True:
    wiadomosci=driver.find_element_by_xpath('//*[@id="js_1"]')
    dane_text=wiadomosci.text
    dane_lista=dane_text.split('\n')
    print(dane_lista)

    if dane_lista[-1] == "!BOT":
        # print("Pasuje odpisac na wiadomosc: " + dane_lista[-1])

        driver.find_element_by_xpath("//*[@data-editor]").click()
        actions=ActionChains(driver)

        # actions.send_keys(reply_messages(dane_lista[-1]))
        actions.send_keys(wiadomosc_bota)
        actions.send_keys(Keys.RETURN)
        actions.perform()

    sleep(10)

# wiadomosc=driver.find_element_by_xpath('//*[@id="js_1"]')
# print(wiadomosc.text)
