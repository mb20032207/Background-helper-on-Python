# -*- coding: utf-8 -
# -*- coding: cp1251 -*-
import sys
import os
import math
from matplotlib import pyplot as plt
import pylab
import numpy as np
import math
import ctypes
import time
import datetime
from datetime import datetime
from multiprocessing import Process
import winsound
from dateutil import parser
import plyer
from os import environ
import urllib.request
import pyzbar
from pyzbar import pyzbar
import cv2
from pyzbar.pyzbar import decode
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow, QTextEdit, QAction, QInputDialog, QMessageBox, QFileDialog
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer
texting = ""
s_weather = "https://www.google.com/search?sxsrf=ALeKk00-GjAmnd_wZ_WgUI60UO49Qmt_ZQ%3A1588265472724&source=hp&ei=AAKrXpOnKeiKmwWj5K-4Bg&q=weather+today+&oq=weather+today+&gs_lcp=CgZwc3ktYWIQAzIHCAAQRhCAAjICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoECCMQJzoFCAAQgwFQ94INWImeDWC4nw1oAHAAeACAAewDiAH8E5IBCTAuMS43LjEuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwiTp7v6zZDpAhVoxaYKHSPyC2cQ4dUDCAc&uact=5"


def make_data(s1, s2, s3):
    s = "2020-"
    for i in months.keys():
        for j in months[i]:
            if j == s2:
                s += i
                break
    print(s3)
    s += "-"
    s += s1
    s += " "
    s += s3[0]
    s += s3[1]
    s += ':'
    s += s3[2]
    s += s3[3]
    s += ':00'
    print(s)
    return s


def transform_string_get_list(s):
    try:
        a = 0
        b = 0
        c = 0
        s = s.replace(' ', '')
        s = s.replace('*', '')
        s = s.replace('х', 'x')
        list1 = s.split('+')
        digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-']
        list_a = []
        list_b = []
        used = []
        for j in range(len(s)):
            if s[j] == '^':
                s_a = ""
                j1 = j - 2
                used.append(j + 1)
                used.append(j)
                used.append(j - 1)
                while s[j1] in digit and j1 >= 0:
                    s_a += s[j1]
                    used.append(j1)
                    if s[j1] == '-':
                        break
                    j1 -= 1
                s_a = s_a[::-1]
                if len(s_a) == 0:
                    list_a.append('1')
                elif s_a == '-':
                    list_a.append('-1')
                else:
                    list_a.append(s_a)
        for j in range(len(s)):
            if s[j] == 'x' and (j + 1 == len(s) or (s[j + 1] != '^')):
                print(s[j + 1])
                used.append(j)
                s_b = ""
                j1 = j - 1
                while s[j1] in digit and j1 >= 0:
                    used.append(j1)
                    s_b += s[j1]
                    if s[j1] == '-':
                        break
                    j1 -= 1
                s_b = s_b[::-1]
                if len(s_b) == 0:
                    list_b.append('1')
                elif s_b == '-':
                    list_b.append('-1')
                else:
                    list_b.append(s_b)
        list_c = []
        for j in range(len(s)):
            if j not in used:
                s_c = ""
                j1 = j
                while s[j1] in digit and j1 < len(s):
                    s_c += s[j1]
                    used.append(j1)
                    j1 += 1
                    if j1 >= len(s):
                        break
                    if s[j1] == '-' or s[j1] == '+':
                        break
                list_c.append(s_c)
        for i in list_a:
            if len(i) != 0:
                a += int(i)
        for i in list_b:
            if len(i) != 0:
                b += int(i)
        for i in list_c:
            if len(i) != 0:
                c += int(i)
        return [a, b, c]
    except:
        return [-1]


def solve(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return ("Решений не существует")
    elif d == 0:
        return ("Корень:" + "\n" + "x = " + str(-b / (2 * a)))
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        if (int(x1) == x1):
            x1 = int(x1)
        print(x1)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        if int(x2) == x2:
            x2 = int(x2)
        print(x1, x2)
        print("x1 = " + str(x1) + "x2 = " + str(x2))
        return ("Корни:" + "\n" + "x1 = " + str(x1) + "\n" + "x2 = " + str(x2))


def clean_str(s):
    s = s.lower()
    s2 = ""
    for i in s:
        if i not in [' ', ':', ';', '.', ',']:
            s2 += i
    return s2


def clean_str_for_site(s):
    s = s.lower()
    s = s.replace(' ', '')
    return s


months = {}
months["Jan"] = ["январь", "январ", "январр", "янв", "я", "01", "1", "january", "jan"]
months["Feb"] = ["февраль", "феврал", "февралл", "фев", "ф", "02", "2", "february", "feb"]
months["Mar"] = ["март", "мар", "03", "3", "march", "mar"]
months["Apr"] = ["апрель", "апр", "апрелл", "04", "4", "april", "apr"]
months["May"] = ["май", "05", "5", "may", "may"]
months["Jun"] = ["июнь", "06", "6", "june", "jun"]
months["Jul"] = ["июль", "июл", "07", "7", "july", "jul"]
months["Aug"] = ["август", "авг", "08", "8", "august", "aug"]
months["Sep"] = ["сентябрь", "сен", "09", "9", "september", "sep"]
months["Oct"] = ["октябрь", "окт", "10", "october", "oct"]
months["Nov"] = ["ноябрь", "нояб", "11", "november", "nov"]
months["Dec"] = ["декабрь", "дек", "12", "december", "dec"]


class show_message_about_solutions(QWidget):
    def __init__(self):
        super().__init__()
        self.UI2()

    def UI2(self):
        print("i am here hello")
        self.setFixedSize(200, 200)
        self.setWindowTitle("Второе окно")
        print("anddd")
        self.mes = QLabel(texting, self)
        self.mes.move(0, 0)
        print("and here")
        self.show()
        print("and gere 2")


def show_message(text):
    print("kokokokokokokokokokokokokokokokokokok")


def show_chart(a, b, c, text_for_chart):
    print("print")
    pr2 = Process(target=show_message(text_for_chart))
    pr2.start()
    print("hello")
    x = np.linspace(-30, 30, 50)
    y = [a * (i ** 2) + b * i + c for i in x]
    print("hello")
    plt.plot(x, y)
    plt.title("График функции")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    pr2.join()


class second_window(QWidget):
    def __init__(self):
        super().__init__()
        self.UI2()

    def UI2(self):
        print("osjdoj")
        self.setFixedSize(1000, 1000)
        self.setWindowTitle("Второе окно")
        self.show()
        print("lol")


class start(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(1000, 1000)
        self.setWindowTitle('Помощник')
        self.hello = QLabel('Привет, Марк!', self)
        self.hello.move(460, 0)
        self.add_event = QPushButton('Добавить напоминание', self)
        self.add_an_alarm = QPushButton('Добавить будильник', self)
        self.add_an_alarm.clicked.connect(self.add_alarm_to_db)
        self.add_an_pair_login_pass = QPushButton('Добавить пароль', self)
        self.solve_square_equation = QPushButton('Решить квадратное уравнение', self)
        self.solve_square_equation.move(0, 150)
        self.solve_square_equation.clicked.connect(self.solve_square_solution)
        self.add_an_pair_login_pass.move(0, 100)
        self.add_an_pair_login_pass.clicked.connect(self.add_an_password_to_base)
        self.add_an_alarm.move(0, 50)
        self.add_event.move(0, 0)
        self.add_event.clicked.connect(self.add_event_button)
        self.go_to_next_window = QPushButton('Построить график', self)
        self.go_to_next_window.move(0, 200)
        self.go_to_next_window.clicked.connect(self.move_to_next_window)
        self.get_pass = QPushButton("Получить пароль", self)
        self.get_pass.move(0, 250)
        self.get_pass.clicked.connect(self.get_password)
        print("check_show")
        self.weather = QPushButton("Узнать погоду", self)
        self.weather.move(0, 300)
        self.weather.clicked.connect(self.show_weather)
        self.get_qr_code = QPushButton("Распознать QR код", self)
        self.get_qr_code.move(0, 350)
        self.get_qr_code.clicked.connect(self.get_qr_code_func)
        self.delete_water = QPushButton("Удалить ватермарку", self)
        self.delete_water.move(0, 400)
        self.delete_water.clicked.connect(self.delete_watermark)
        self.show()
    def get_qr_code_func(self):
        file_path_qr_code = QFileDialog.getOpenFileNames(self, "Выбрать файл", "/apple")
        st1 = str(file_path_qr_code)
        st1 = st1.replace('All Files (*)', '')
        st1 = st1.replace('(', '')
        st1 = st1.replace(')', '')
        st1 = st1.replace('\'', '')
        st1 = st1.replace(',', '')
        st1 = st1.replace('[', '')
        st1 = st1.replace(']', '')
        print("s == ", st1)
        st1 = st1.strip(' ')
        if not st1.endswith('.jpeg') and not st1.endswith('.bmp') and not st1.endswith('.gif') and not st1.endswith('.jpg'):
            print("ok")
            QMessageBox.critical(self, "Error", "Невозможно распознать QR код, так как выбран некорректный формат файла", QMessageBox.Ok)
        else:
            print("we re here congrats")
            im = cv2.imdecode(np.fromfile(st1, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            print(im)
            print("ok")
            try:
                answer = decode(im)[0][0].decode("utf-8")
                print(answer)
                winsound.Beep(2000, 500)
                QMessageBox.about(self, "QR код успешно распознан", answer)
                
            except:
                print("kok")
                QMessageBox.critical(self, "На картинке отсутствует QR код", "Выберите другое изображение и повторите попытку", QMessageBox.Ok)

    def delete_watermark(self):
        file_path_qr_code = QFileDialog.getOpenFileNames(self, "Выбрать файл", "/apple")
        st1 = str(file_path_qr_code)
        st1 = st1.replace('All Files (*)', '')
        st1 = st1.replace('(', '')
        st1 = st1.replace(')', '')
        st1 = st1.replace('\'', '')
        st1 = st1.replace(',', '')
        st1 = st1.replace('[', '')
        st1 = st1.replace(']', '')
        print(st1)
        st1 = st1.strip(' ')
        if not st1.endswith('.jpeg') and not st1.endswith('.bmp') and not st1.endswith('.gif') and not st1.endswith('.jpg'):
            print("ok")
            QMessageBox.critical(self, "Error", "Невозможно удалить ватермарку, так как выбран некорректный формат файла", QMessageBox.Ok)
        else:
            img = cv2.imdecode(np.fromfile(st1, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            print(img)
            alpha = 2.0
            beta = -160
            new = alpha * img + beta
            new = np.clip(new, 0, 255).astype(np.uint8)
            new_path = "C:/Photo_without_watermark"
            print("here")
            try:
                os.mkdir(new_path)
            except:
                print("")
            print("well")
            print(new_path)
            count_of_files = len(os.listdir(new_path))
            print(count_of_files)
            new_path += '/'
            new_path += str(count_of_files)
            new_path += ".jpg"
            print(new_path)
            pr3 = Process(target = start.process2_show_message_without_watermark())
            print("herze")
            pr3.start()
            cv2.imwrite(new_path, new)
            cv2.imshow("Изображение без ватермарки", new)
            cv2.waitKey(0)
            pr3.join()
    def process2_show_message_without_watermark(self):
        print("herze2")
        QMessageBox.about(self, "hello", "hello2")

    def show_weather(self):
        try:
            with urllib.request.urlopen(s_weather) as url:
                s_url = url.read()
                # I'm guessing this would output the html source code ?
                print(s_url)

        except:
            print("Weather is not available! Internet is broken!")

    def add_alarm_to_db(self):
        f = open("data_base_alarm.txt", 'a')
        date, confirm_level_1 = QInputDialog.getText(self, '')
        print("we're here")

    def move_to_next_window(self):
        self.sec_wind = second_window()
        self.sec_wind.show()

    def add_an_password_to_base(self):
        site, confirm_level_1 = QInputDialog.getText(self, 'Сайт', 'Введите сайт')
        if confirm_level_1:
            site = clean_str_for_site(site)
            login, confirm_level_2 = QInputDialog.getText(self, 'Логин', 'Введите логин')
            if confirm_level_2:
                password, confirm_level_3 = QInputDialog.getText(self, 'Пароль', 'Введите пароль')
                if confirm_level_3:
                    file_put = open("data_base_passwords_site.txt", 'a')
                    file_put2 = open("data_base_passwords_login.txt", 'a')
                    file_put3 = open("data_base_passwords_password.txt", 'a')
                    file_put.write(site + "\n")
                    file_put2.write(login + "\n")
                    file_put3.write(password + "\n")
                    file_put.close()
                    file_put2.close()
                    file_put3.close()

    def get_password(self):
        site, confirm_level_1 = QInputDialog.getText(self, 'Сайт', 'Введите сайт')
        if confirm_level_1:
            site = clean_str_for_site(site)
            f = open("data_base_passwords_site.txt", 'r')
            f2 = open("data_base_passwords_login.txt", 'r')
            f3 = open("data_base_passwords_password.txt", 'r')
            index = 0
            need_index = -1
            print("site == ", site)
            site += '\n'
            need_login = ""
            for line in f:
                print("checK", line, "kek", site)
                if line == site:
                    need_index = index
                    break
                index += 1
            if need_index < 0:
                QMessageBox.critical(self, "Ошибка", "Информация о пароле от данного сайта отсутствует в системе")
            index = 0
            for line in f2:
                if index == need_index:
                    need_login = line
                index += 1
            need_pass = ""
            index = 0
            for line in f3:
                if index == need_index:
                    need_pass = line
                index += 1
            if need_index >= 0:
                msg = QMessageBox()
                msg.setWindowTitle("Информация")
                msg.resize(1000, 500)
                msg.setText("Логин:" + need_login + "Пароль:" + need_pass)
                msg.exec()
            print(need_login, need_pass)

    def solve_square_solution(self):
        eq, confirm = QInputDialog.getText(self, 'Решение квадратных уравнений', 'Введите квадратное уравнение')
        if confirm:
            help_list_in_func = transform_string_get_list(eq)
            if len(help_list_in_func) == 1:
                QMessageBox.critical(self, "Ошибка ", "Уравнение некорректно", QMessageBox.Ok)
            else:
                a = help_list_in_func[0]
                b = help_list_in_func[1]
                c = help_list_in_func[2]
                print(a, b, c)
                recieve = str(solve(a, b, c))
                rec2 = ""
                for i in recieve:
                    if i not in ['(', ')', ',', '\'']:
                        rec2 += i
                print(rec2)
                print("here we was")
                show_chart(a, b, c, rec2)

    def add_event_button(self):
        global dict_of_events
        info, confirm_level_1 = QInputDialog.getText(self, 'Название', 'Введите информацию о событии')
        if confirm_level_1:
            date, confirm_level_2 = QInputDialog.getText(self, 'Дата', 'Введите дату события')
            if confirm_level_2:
                month, confirm_level_3 = QInputDialog.getText(self, 'Месяц', 'Введите месяц события')
                if confirm_level_3:
                    time, confirm_level_4 = QInputDialog.getText(self, 'Время', 'Введите время события')
                    if confirm_level_4:
                        date = clean_str(date)
                        month = clean_str(month)
                        time = clean_str(time)
                        add = make_data(date, month, time)
                        file_put = open("data_base_events_info.txt", 'a')
                        file_put2 = open("data_base_events_time.txt", 'a')
                        file_put.write(info + "\n")
                        file_put2.write(add + "\n")
                        file_put.close()
                        file_put2.close()


class start_auth(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        print("hello_world")
        self.show()


def beep():
    while 1 == 1:
        time.sleep(5)
        dt = time.time()
        # print(dt, "== dt")
        dir = os.path.abspath(os.curdir)
        files = os.listdir(dir)
        print(files)
        f = open("data_base_events_time.txt", "r")
        f2 = open("data_base_events_info.txt", "r")
        index = 0
        for line in f:
            datetime_obj = parser.parse(line)
            delta = datetime.now() - datetime_obj
            # print(datetime_obj, datetime.now(), delta.seconds, delta)
            if (abs(delta.seconds) < 60) and str(delta).count("day") == 0:
                winsound.Beep(2500, 1000)
                index2 = 0
                for line2 in f2:
                    if index == index2:
                        plyer.notification.notify(message=line2, app_name="name_cast_later.py", title="Уведомление")
                        break
                    index2 += 1
            index += 1
        f2 = open("data_base_alarm.txt", "r")


if __name__ == '__main__':
    pr = Process(target=beep)
    pr.start()
    print("koooL")
    app = QApplication(sys.argv)
    window = start()
    sys.exit(app.exec_())
    pr.join()
    
