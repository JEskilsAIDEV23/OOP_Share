from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys

class Text:
    def __init__self(self):
        self.__text = ''
        self.__encrypt = ''
        self.__alpha = 0
        self.__symbol = 0

    def set_text(self, value):
        self.__text = value

    def get_text(self):
        return self.__text

    def encrypt_text(self, value):
        kon = "BDFGHJKLMNPQRSTVWXZbdfghjklmnpqrstvwxz"
        tmp_txt = ""
        for i in value:
            if i in kon:
                tmp_txt += i+"o"+i.lower()
            else:
                tmp_txt = tmp_txt+i
        return tmp_txt

    def set_encrypt(self, value):
        self.__encrypt = value
        return self.__encrypt
    
    def get_encrypt(self):
        return self.__encrypt
        
    def n_alpha(self, value):
        n = 0
        nt = 0
        alpha = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ "
        for i in value:
            if i in alpha:
                n += 1
            nt += 1
        self.__alpha = n
        self.__symbol = nt-n

    def get_n_alpha(self):
        return self.__alpha
    
    def get_n_symbol(self):
        return self.__symbol  

enc_txt = Text()

sve_text = 'Välkommen till boken Python från början! Detta är boken för dig som vill lära dig att \
programmera i Python. Du behöver inte ha några tidigare kunskaper i programmering, men \
det är bra om du är van att använda datorer.'

class MyGui(QMainWindow):

    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi('mygui.ui', self)
        self.show()
        self.pushButton.clicked.connect(lambda: self.grab_txt())
        self.plainTextEdit.insertPlainText(sve_text)

    def grab_txt(self):
        text = self.plainTextEdit.toPlainText()
        self.textBrowser.clear()
        enc_txt.set_text(text)
        enc_txt.set_encrypt(enc_txt.encrypt_text(enc_txt.get_text()))
        self.textBrowser.append(enc_txt.get_encrypt())

def main():
    app = QApplication([])
    window = MyGui()
    app.exec_()

if __name__ == '__main__':
    main()