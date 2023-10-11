import sys
from PyQt5 import QtWidgets, uic, QtGui, QtDesigner, QtCore, QtQuickWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from MainWindow import Ui_MainWindow
from cls_Arbitary_dice import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        pixmap6 = QPixmap('X.png') 
        self.label.setPixmap(QPixmap(pixmap6))
        self.label.resize(pixmap6.width(),pixmap6.height())
        self.label_2.setPixmap(QPixmap(pixmap6))
        self.label_2.resize(pixmap6.width(),pixmap6.height())
        self.label_3.setPixmap(QPixmap(pixmap6))
        self.label_3.resize(pixmap6.width(),pixmap6.height())
        self.label_4.setPixmap(QPixmap(pixmap6))
        self.label_4.resize(pixmap6.width(),pixmap6.height())
        self.label_5.setPixmap(QPixmap(pixmap6))
        self.label_5.resize(pixmap6.width(),pixmap6.height())
        self.label_6.setPixmap(QPixmap(pixmap6))
        self.counter_winp1 = 0
        self.counter_winp2 = 0
        self.counter_push = 0
        self.pushButton.clicked.connect(lambda: roll_em())

        def roll_em():
        
            pd_label_1, pd_label_2, pd_label_3, sum_d = roll_it()
            self.label.setPixmap(QPixmap(pd_label_1))
            self.label_2.setPixmap(QPixmap(pd_label_2))
            self.label_3.setPixmap(QPixmap(pd_label_3))
            self.labelP1_sum.setText(str(sum_d))

            pd_label_4, pd_label_5, pd_label_6, sum_d2 = roll_it_2()
            self.label_4.setPixmap(QPixmap(pd_label_4))
            self.label_5.setPixmap(QPixmap(pd_label_5))
            self.label_6.setPixmap(QPixmap(pd_label_6))
            self.labelP2_sum.setText(str(sum_d2))

            if sum_d > sum_d2:
                self.counter_winp1 +=1
            if sum_d < sum_d2:
                self.counter_winp2 +=1
            if sum_d == sum_d2:
                self.counter_push +=1

            self.labelP1_wins.setText(str(self.counter_winp1))
            self.labelP2_wins.setText(str(self.counter_winp2))
            self.label_None.setText(str(self.counter_push))

def roll_it():
    Dice.set_Dice_type(6)
 #   wm = p_calc(6)
 #   Dice.set_Dice_w(wm)
    d1 = Dn1()
    pd_label_1 = d1.pd1
    d2 = Dn1()
    pd_label_2 = d2.pd1
    d3 = Dn1()
    pd_label_3 = d3.pd1
    sum_d = d1.dice_1+d2.dice_1+d3.dice_1
    return pd_label_1, pd_label_2, pd_label_3, sum_d

def roll_it_2():
    Dice.set_Dice_type(6)
 #   wm = p_calc2(6)
 #   Dice.set_Dice_w(wm)
    d1_2 = Dn1()
    pd_label_4 = d1_2.pd1
    d2_2 = Dn1()
    pd_label_5 = d2_2.pd1
    d3_2 = Dn1()
    pd_label_6 = d3_2.pd1
    sum_d_2 = d1_2.dice_1+d2_2.dice_1+d3_2.dice_1
    return pd_label_4, pd_label_5, pd_label_6, sum_d_2

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()