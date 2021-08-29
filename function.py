import time, traceback
from selenium.common.exceptions import NoSuchElementException
import main, gui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

total_score__ = 0
game_count__ = 0
def check():
    try:
        element = WebDriverWait(main.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME,'premium-subject-congratulations__inner')))
        element.click()
    except:
        crash(traceback.format_exc())
        pass

def achievment():
    try:
        link = WebDriverWait(main.driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='achievement-description__title']")))
        if not link:
            pass
        else:
            ### Временно ###
            main.driver.quit()
            main.main()

    except:
        pass
        #crash(traceback.format_exc())
        #main.driver.quit()
        #main.main()

def new_level():
    try:
        link = WebDriverWait(main.driver, 3).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'b-achievement-description__title-wrap i-utils_adventure__vertical-centering-content')))
        if not link:
            pass
        else:
            ### Временно ###
            main.driver.quit()
            main.main()
    except:
        pass
        #main.driver.quit()
        #main.main()


def log(text):
    try:
        log = open('log.txt', 'a')
        log.write(text)
        log.close()
    except:
        pass

def crash(text):
    try:
        crash_ = open('crash.txt', 'a')
        crash_.write(text + '\n')
        crash_.close()
    except:
        pass

def game_score():
    try:
        score_for_game = WebDriverWait(main.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='b-modal-content__score-value']")))
        tmp = score_for_game.text
        global total_score__
        global game_count__
        total_score__ += int(tmp)
        game_count__ += 1
        gui.Main_menu.stat()
        time.sleep(1)
    except:
        log('Game_score error')
        crash(traceback.format_exc())
