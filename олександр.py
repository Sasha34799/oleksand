from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('конкурс від Makara')

question = QLabel("в якому році ти отримав <<срібну кнопку>> від Youtube?")
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')

layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment=Qt.AlignCenter)
layout_main.addWidget(btn_answer1, alignment=Qt.AlignCenter)
layout_main.addWidget(btn_answer2, alignment=Qt.AlignCenter)
layout_main.addWidget(btn_answer3, alignment=Qt.AlignCenter)
layout_main.addWidget(btn_answer4, alignment=Qt.AlignCenter)

def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Правильно\nВи виграли гіроскутер')
    victory_win.exec_()

def show_lose():
    lose_win = QMessageBox()
    lose_win.setText('Неправильно\nВи виграли фірмовий плакат')
    lose_win.exec_()

btn_answer3.clicked.connect(show_win)
btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)

main_win.setLayout(layout_main)
main_win.show()

app.exec_()
