import data, time, traceback, function, main, re, threading
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread

tread_killer = 0

def check_end_game():
    try:
        flag = WebDriverWait(main.driver, 1000).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='flag flag_clickable flag_mistakes-review']")))
        if flag:
            try:
                function.log('end game\n')
                global tread_killer
                tread_killer = ''
                flag.click()
                function.achievment()
                function.new_level()
                function.check()
                tap = WebDriverWait(main.driver, 30).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//span[@class='g-button__label']")))
                function.game_score()
                tap.click()
                function.log('\nfind game\n')
                new_game()

            except:
                function.log('end game error\n\n')
                function.crash(traceback.format_exc())
                main.driver.quit()
                main.main()

    except:
        function.log('end game error\n\n')
        function.crash(traceback.format_exc())
        main.driver.quit()
        main.main()

def check_network():
    try:
        global tread_killer
        tread_killer += 1
        try:
            tap = WebDriverWait(main.driver, 1000).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='b-modal-content__description']")))
            if tap.text == 'У соперника проблемы со связью... Ждем':
                main.driver.quit()
                main.main()
            else:
                check_network()
        except:
            function.log('check_network error\n\n')
            function.crash(traceback.format_exc())
            check_network()
    except:
        pass


def check_game_quit():
    try:
        global tread_killer
        tread_killer += 1
        try:
            tap = WebDriverWait(main.driver, 1000).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='b-modal-content__description']")))
            if tap.text == 'Игра прервана. \nСоперник покинул игру.':
                main.driver.quit()
                main.main()
            else:
                check_game_quit()
        except:
            function.log('check_game_quit error\n\n')
            function.crash(traceback.format_exc())
            check_game_quit()
    except:
        pass

def check_my_network():
    try:
        global tread_killer
        tread_killer += 1
        try:
            tap = WebDriverWait(main.driver, 1000).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='b-modal-content__description']")))
            if tap.text == 'Игра прервана. \nСоперник покинул игру.':
                main.driver.quit()
                main.main()
            else:
                check_game_quit()
        except:
            function.log('check_game_quit error\n\n')
            function.crash(traceback.format_exc())
            check_game_quit()
    except:
        pass

def stroke():
    try:
        # i-control b-battle-cell b-battle-cell_adventure b-battle-cell_available  Этот класс определяет доступные для хода клетки!!!
        global tread_killer
        tread_killer += 1
        try:
            b_stroke = WebDriverWait(main.driver, 120).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='b-page__timer b-page__timer_footer']")))
            field = main.driver.find_elements_by_xpath("//div[@class='b-battle-cell__tap-zone']")
            own = main.driver.find_elements_by_xpath("//div[@class='i-control g-icon g-icon_adventure b-battle-cell__background-icon g-icon_img_resizable_cell-owned-blue']")
            k = len(own)
            if k == 0:
                try:
                    field[9].click()
                except NoSuchElementException:
                    pass
            elif k == 1:
                try:
                    field[6].click()
                except NoSuchElementException:
                    pass
            elif k == 2:
                try:
                    field[3].click()
                except NoSuchElementException:
                    pass
            elif k >= 3:
                try:
                    field[0].click()
                except NoSuchElementException:
                    pass
            stroke()
        except:
            function.log('stroke error\n\n')
            function.crash(traceback.format_exc())
            stroke()

    except:
        pass

def question_():
    try:
        global tread_killer
        tread_killer += 1
        try:
            type_ = WebDriverWait(main.driver, 120).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     ".//div[@class='b-modal-content__info' and text()='Ваш вопрос' or @class='b-modal-content__info' and text()='Вопрос-дуэль']")))

            question = WebDriverWait(main.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='b-modal-content__title']")))

            question_text = question.text
            try:
                question_text_str = str(data.data_for[question_text])
            except:
                print('except', question_text)
                for i in data.data_for.keys():
                    result = re.findall(i, question_text)
                    if len(result) > 0:
                        question_text_str = str(data.data_for[i])
            print('answer', question_text_str)
            answer = WebDriverWait(main.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[text()="{0}"]'.format(question_text_str))))
            print(answer)
            time.sleep(1)
            answer.click()
            time.sleep(5)
            question_()

        except:
            question_()

    except:
        pass

def play():
    try:
        function.log('game started\n')
        global tread_killer
        tread_killer = 0
        pc_stroke = Thread(target=stroke, args=(), daemon=True)
        pc_question = Thread(target=question_, args=(), daemon=True)
        pc_network = Thread(target=check_network, args=(), daemon=True)
        pc_ch_game = Thread(target=check_game_quit, args=(), daemon=True)
        pc_stroke.start()
        pc_network.start()
        pc_question.start()
        pc_ch_game.start()
        check_end_game()
    except:
        main.driver.quit()
        main.main()

def new_game():
    try:
        link = WebDriverWait(main.driver, 80).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='i-control b-hexagon-map b-hexagon-map_adventure b-hexagon-map_battle']")))
        play()
    except:
        pass

