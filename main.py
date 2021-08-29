from selenium import webdriver
import registration, function, game, traceback, sys, os, time, gui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
driver = ''

def main():
    try:
        global driver
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.set_window_size(1024, 600)
        driver.maximize_window()
        function.log('program started\n')

        if gui.type_of_account == 0:
            driver.get('https://clevver.me/v1/oauth/vk?session=s%3AHYhaOt13MY-z7Uq2Jz4xRB_QibMvn7X6.VENo3IkrsYUKwk%2BLmyJGso2p5ouJH6tyvWkkOajihSI&isMobileApp=false&appInstanceId=1627829225921&v=cBJsn4FPhpthCAQSoDNFd5')
            ch = registration.vk(driver, gui.login_of_account, gui.password_of_account)
            if ch == 1:
                return 1
        elif gui.type_of_account == 1:
            driver.get('https://www.facebook.com/login.php?skip_api_login=1&api_key=1155220181156719&kid_directed_site=0&app_id=1155220181156719&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1155220181156719%26scope%3Demail%252C%2Buser_friends%26display%3Dpopup%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fclevver.me%252Fv1%252Fauth%252Ffb%26state%3D%257B%2522appInstanceId%2522%253A%25221628079273170%2522%252C%2522isMobileApp%2522%253A%2522false%2522%252C%2522encodedSid%2522%253A%2522s%25253AClpsNBJR4-sJAh8ACjVIje16e1lqEcMe.C43ImGJjULTbGlBngujcEikW9ucqA7%25252F9ycMQ9QlR49c%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D3c162cad-1489-43bf-ae77-2691a424a835%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fclevver.me%2Fv1%2Fauth%2Ffb%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522appInstanceId%2522%253A%25221628079273170%2522%252C%2522isMobileApp%2522%253A%2522false%2522%252C%2522encodedSid%2522%253A%2522s%25253AClpsNBJR4-sJAh8ACjVIje16e1lqEcMe.C43ImGJjULTbGlBngujcEikW9ucqA7%25252F9ycMQ9QlR49c%2522%257D%23_%3D_&display=popup&locale=ru_RU&pl_dbl=0')
            ch = registration.facebook(driver, gui.login_of_account, gui.password_of_account)
            if ch == 1:
                driver.quit()
                return 1
        else:
            driver.get('https://clevver.me/#/')
            ch = registration.without_reg(driver, gui.login_of_account)
            if ch == 1:
                driver.quit()
                return 1

        function.check()
        link = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='#/subject/10']")))
        link.click()

        link = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='#/subject/10/topic/37']")))
        link.click()
        link = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='button button_default-border-radius button_default-disabled default-active topic-with-lessons-buttons__button']")))
        link.click()

        function.log('find game\n')
        game.new_game()

    except:
        function.log('Critical error. \nRestarting the program\n\n\n')
        function.crash(traceback.format_exc())
        driver.quit()
        main()

def file_sys():
    log = open('log.txt', 'w')
    log.close()
    crash = open('crash.txt', 'w')
    crash.close()

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


if __name__ == '__main__':
    file_sys()
    gui.gui()

