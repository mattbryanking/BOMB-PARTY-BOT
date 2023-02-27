import PySimpleGUI as sg
from selenium import webdriver
from time import sleep
import Game as Game


class Controller:

    def __init__(self):
        self.PATH = ''

    def main(self):
        sg.theme('Default1')
        layout = [
            [sg.Text('Desired Username:')],
            [sg.Text('', size=(0, 0)), sg.InputText(default_text="Esan BOT")],
            [sg.Text('BombParty Room Code:')],
            [sg.Text('', size=(0, 0)), sg.InputText()],
            [sg.Text('ChromeDriver Location:')],
            [sg.Text('', size=(0, 0)), sg.InputText(), sg.FileBrowse()],
            [sg.Text('Select Language:')],
            [sg.Radio('English', "RADIO1", default=True), sg.Radio('French', "RADIO1", default=False)],
            [sg.Text('Select Word Type:')],
            [sg.Radio('All', "RADIO2", default=True), sg.Radio('Impressive', "RADIO2", default=False),
                sg.Radio('Simple', "RADIO2", default=False)],
            [sg.Text('Select Mode:')],
            [sg.Radio('Cheater Mode', "RADIO3", default=True), sg.Radio('Fake Player Mode', "RADIO3", default=False)],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('BombParty Bot 1.0', layout, element_justification='c')
        event, values = window.read()
        window.close()
        botName = values[0]
        code = values[1].lower()
        self.PATH = values[2]

        if values[3]:
            lang = 1
        else:
            lang = 2

        if values[5]:
            wordType = 1
        elif values[6]:
            wordType = 2
        else:
            wordType = 3

        cheater = values[8] == True

        driver = webdriver.Chrome(executable_path=self.PATH)
        game = Game.Game(driver, botName, code, wordType, lang, cheater)
        game.connectRoom()

        while True:
            try:
                if not game.isGameRunning():
                    # if the game is in the lobby join
                    game.joinGame()
                else:
                    # Wait for game to start
                    sleep(2)
            except:
                print("Something Went Wrong, Restart.")
                game.playGame()
                continue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Controller().main()
