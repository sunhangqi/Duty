# -*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QTextEdit, QPushButton
import time
import sys


class Duty(QWidget):
    def __init__(self):
        super(Duty, self).__init__()
        self.timer = QTimer()
        self.time_text = time.strftime("%m-%d-%a\n%H:%M:%S %p")
        self.label_text = "今日任务"
        self.time_label = QLabel(self)
        self.text_label = QLabel(self)
        self.text_edit = QTextEdit(self)
        self.reset_btn = QPushButton(self)
        self.save_btn = QPushButton(self)
        self.exit_btn = QPushButton(self)
        self.box_layout = QVBoxLayout()
        self.init_ui()
        self.init_timer()

    def init_ui(self):
        self.resize(400, 450)
        self.setWindowTitle("今日任务")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.85)

        self.time_label.setGeometry(QRect(100, 10, 200, 50))
        self.time_label.setText(self.time_text)
        self.time_label.setFont(QFont("monaco", 24))
        self.time_label.setAutoFillBackground(True)
        self.time_label.setAlignment(Qt.AlignCenter)
        ###############

        self.text_label.setGeometry(100, 60, 200, 50)
        self.text_label.setText(self.label_text)
        self.text_label.setStyleSheet("color:red")
        self.text_label.setFont(QFont("monaco", 20))
        self.text_label.setAlignment(Qt.AlignCenter)
        ###############
        self.text_edit.setGeometry(QRect(0, 100, 400, 300))
        # self.text_edit.setTextColor(Qt.green) 该方法删除字后颜色设置无效？
        self.text_edit.setStyleSheet("color:yellow")
        self.text_edit.setFont(QFont("monaco", 25))
        self.text_edit.setEnabled(True)

        ################
        self.reset_btn.setGeometry(QRect(20, 410, 80, 30))
        self.reset_btn.setText("重置")
        self.reset_btn.clicked.connect(self.reset)

        ################
        self.save_btn.setGeometry(QRect(160, 410, 80, 30))
        self.save_btn.setText("保存")
        self.save_btn.clicked.connect(self.write_file)

        self.exit_btn.setGeometry(QRect(300, 410, 80, 30))
        self.exit_btn.setText("退出")
        self.exit_btn.clicked.connect(self.exit)

        ################

        self.box_layout.addWidget(self.time_label)
        self.box_layout.addWidget(self.text_label)
        self.box_layout.addWidget(self.text_edit)
        self.box_layout.addWidget(self.save_btn)
        self.box_layout.addWidget(self.reset_btn)
        self.box_layout.addWidget(self.exit_btn)
        self.show()

    def init_timer(self):
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.update_text)

    def update_text(self):
        self.time_text = time.strftime("%m-%d-%a\n%H:%M:%S %p")
        self.time_label.setText(self.time_text)
        self.time_label.setWordWrap(True)

    def write_file(self):
        with open("task.txt", 'a+') as f:
            # lines = f.readlines()
            # if lines is not None:
                #f.write("\n")
            f.write("\n")
            f.write(self.text_edit.toPlainText())
            f.write("\n")
            f.write(self.time_text)
        self.text_edit.setEnabled(False)

    def reset(self):
        self.text_edit.setEnabled(True)
        self.text_edit.clear()

    def exit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    duty = Duty()
    app.exec_()
