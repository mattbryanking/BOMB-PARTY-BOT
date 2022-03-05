import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import Game

BOT_NAME = "EsanBOT"
PATH = 'C:\Program Files\ChromeDriver\chromedriver.exe'
url = "https://jklm.fun/"


def main():
    sg.theme('Default1')
    layout = [
        [sg.Text('BombParty Room Code:')],
        [sg.Text('', size=(0, 0)), sg.InputText()],
        [sg.Text('Select Word Type:')],
        [sg.Radio('All', "RADIO1", default=True)],
        [sg.Radio('Impressive', "RADIO1", default=False)],
        [sg.Radio('Simple', "RADIO1", default=False)],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window('BombParty Bot 1.0', layout, element_justification='c')
    event, values = window.read()
    window.close()

    words_type = None
    room_number = values[0]

    if values[1]:
        words_type = 1
    elif values[2]:
        words_type = 2
    else:
        words_type = 3
    driver = webdriver.Chrome(executable_path=PATH)
    Game.ConnectRoom(driver)
    iframe = 0
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it(iframe))

    while (True):
        # try:
        if (not Game.isGameRunning(driver)):
            Game.JoinGame(driver)
        else:
            sleep(2)
    # except:
    #     print("Something Went Wrong, Restart.")
    #     continue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

