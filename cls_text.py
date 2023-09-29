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
            





