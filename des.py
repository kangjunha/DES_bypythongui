#-*- coding: utf8 -*-

initialPermutation = [58, 50, 42, 34, 26, 18, 10, 2,
                      60, 52, 44, 36, 28, 20, 12, 4,
                      62, 54, 46, 38, 30, 22, 14, 6,
                      64, 56, 48, 40, 32, 24, 16, 8,
                      57, 49, 41, 33, 25, 17,  9, 1,
                      59, 51, 43, 35, 27, 19, 11, 3,
                      61, 53, 45, 37, 29, 21, 13, 5,
                      63, 55, 47, 39, 31, 23, 15, 7]

removeParity = [57, 49, 41, 33, 25, 17,  9,
                 1, 58, 50, 42, 34, 26, 18,
                10,  2, 59, 51, 43, 35, 27,
                19, 11,  3, 60, 52, 44, 36,
                63, 55, 47, 39, 31, 23, 15,
                 7, 62, 54, 46, 38, 30, 22,
                14,  6, 61, 53, 45, 37, 29,
                21, 13,  5, 28, 20, 12,  4]

keyCompression = [14, 17, 11, 24,  1,  5,  3, 28,
                  15,  6, 21, 10, 23, 19, 12,  4,
                  26,  8, 16,  7, 27, 20, 13,  2,
                  41, 52, 31, 37, 47, 55, 30, 40,
                  51, 45, 33, 48, 44, 49, 39, 56,
                  34, 53, 46, 42, 50, 36, 29, 32]

shiftLeft = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

expandPermutation = [32,  1,  2,  3,  4,  5,
                      4,  5,  6,  7,  8,  9,
                      8,  9, 10, 11, 12, 13,
                     12, 13, 14, 15, 16, 17,
                     16, 17, 18, 19, 20, 21,
                     20, 21, 22, 23, 24, 25,
                     24, 25, 26, 27, 28, 29,
                     28, 29, 30, 31, 32,  1]

sBox = [

[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
],

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
],

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],

[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

roundPermutation = [16,  7, 20, 21, 29, 12, 28, 17,
                     1, 15, 23, 26,  5, 18, 31, 10,
                     2,  8, 24, 14, 32, 27,  3,  9,
                    19, 13, 30,  6, 22, 11,  4, 25]

finalPermutation = [40,  8, 48, 16, 56, 24, 64, 32,
                    39,  7, 47, 15, 55, 23, 63, 31,
                    38,  6, 46, 14, 54, 22, 62, 30,
                    37,  5, 45, 13, 53, 21, 61, 29,
                    36,  4, 44, 12, 52, 20, 60, 28,
                    35,  3, 43, 11, 51, 19, 59, 27,
                    34,  2, 42, 10, 50, 18, 58, 26,
                    33,  1, 41,  9, 49, 17, 57, 25]

def stringToBit(text):
    bitArray = list();
    for char in text:
        binVal = binaryValue(char, 4)
        bitArray.extend([int(x) for x in list(binVal)])
    return bitArray

def bitToString(array):
    s = nsplit(array, 4)
    res = ''
    for bytes in nsplit(array, 4):
        integer = bytes[3] + bytes[2] * 2 + bytes[1] * 4 + bytes[0] * 8
        if integer < 10:
            res += str(integer)
        else:
            res += chr(integer + 55)
    return res

def binaryValue(val, bitSize):
    intVal = 0
    flag = True
    if isinstance(val, int):
        intVal = val
        flag = False
    else:
        if ord(val) < 58 and ord(val) > 47:
            intVal = ord(val) - 48
        elif ord(val) < 71 and ord(val) > 64:
            intVal = ord(val) - 55
        else:
            raise "wrong input"

    binVal = bin(intVal)[2:]

    if len(binVal) > bitSize:
        raise "binary value larger than the expected size"
    while len(binVal) < bitSize:
        binVal = "0" + binVal
    return binVal

def nsplit(s, n):
    return [s[k:k+n] for k in range(0, len(s), n)]

ENCRYPT = 1
DECRYPT = 0

class des():
    def __init__(self):
        self.password = None
        self.text = None
        self.keys = list()

    def run(self, key, text, action = ENCRYPT, padding = False):
        if len(key) != 16:
            raise "Key Should be 16 bytes long"

        self.password = key
        self.text = text

        if padding and action == ENCRYPT:
            self.addPadding()
        elif len(self.text) % 16 != 0:
            raise "Data size should be multiple of 16"

        self.generateKeys() #Generate all the keys
        text_blocks = nsplit(self.text, 16) #Split the text in blocks of 8 bytes so 64 bits
        result = list()
        for block in text_blocks: #Loop over all the blocks of data
            block = stringToBit(block) #Convert the block in bit array
            block = self.permutation(block, initialPermutation) #Apply the initial permutation
            g, d = nsplit(block, 32) #g(LEFT), d(RIGHT)
            tmp = None
            for i in range(16): #Do the 16 rounds
                d_e = self.expand(d, expandPermutation) #Expand d to match Ki size (48bits)
                if action == ENCRYPT:
                    tmp = self.xor(self.keys[i], d_e)#If encrypt use Ki
                else:
                    tmp = self.xor(self.keys[15 - i], d_e)#If decrypt start by the last key
                tmp = self.substitute(tmp) #Method that will apply the SBOXes
                tmp = self.permutation(tmp, roundPermutation)
                tmp = self.xor(g, tmp)
                g = d
                d = tmp
            result += self.permutation(d + g, finalPermutation) #Do the last permut and append the result to result
        final_res = bitToString(result)
        if padding and action == DECRYPT:
            return self.removePadding(final_res) #Remove the padding if decrypt and padding is true
        else:
            return final_res #Return the final string of data ciphered/deciphered

    def substitute(self, d_e): #Substitute bytes using SBOX
        subblocks = nsplit(d_e, 6)#Split bit array into sublist of 6 bits
        result = list()
        for i in range(len(subblocks)): #For all the sublists
            block = subblocks[i]
            row = int(str(block[0]) + str(block[5]),2) #Get the row with the first and last bit
            column = int(''.join([str(x) for x in block[1:][:-1]]),2) #Column is the 2,3,4,5th bits
            val = sBox[i][row][column] #Take the value in the SBOX appropriated for the round (i)
            bin = binaryValue(val, 4) #Convert the value to binary
            result += [int(x) for x in bin] #And append it to the resulting list
        return result

    def permutation(self, block, table):#Permut the given block using the given table (so generic method)
        return [block[x - 1] for x in table]

    def expand(self, block, table):#Do the exact same thing than permut but for more clarity has been renamed
        return [block[x - 1] for x in table]

    def xor(self, t1, t2):#Apply a xor and return the resulting list
        return [x ^ y for x, y in zip(t1, t2)]

    def generateKeys(self): #Algorithm that generates all the keys
        self.keys = []
        key = stringToBit(self.password)
        key = self.permutation(key, removeParity) #Apply the initial permut on the key
        g, d = nsplit(key, 28) #Split it in to (g->LEFT),(d->RIGHT)
        for i in range(16): #Apply the 16 rounds
            g, d = self.shift(g, d, shiftLeft[i]) #Apply the shift associated with the round (not always 1)
            tmp = g + d #Merge them
            self.keys.append(self.permutation(tmp, keyCompression)) #Apply the permut to get the Ki

    def shift(self, g, d, n): #Shift a list of the given value
        return g[n:] + g[:n], d[n:] + d[:n]

    def addPadding(self): #Add padding to the datas using PKCS5 spec.
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)

    def removePadding(self, data): #Remove the padding of the plain text (it assume there is padding)
        pad_len = ord(data[-1])
        return data[:-pad_len]

    def encrypt(self, key, text, padding=False):
        return self.run(key, text, ENCRYPT, padding)

    def decrypt(self, key, text, padding=False):
        return self.run(key, text, DECRYPT, padding)

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 259)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 191, 16))
        self.label.setObjectName("label")
        self.plainEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainEdit.setGeometry(QtCore.QRect(40, 30, 321, 21))
        self.plainEdit.setObjectName("plainEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 121, 16))
        self.label_2.setObjectName("label_2")
        self.keyEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.keyEdit.setGeometry(QtCore.QRect(40, 80, 321, 21))
        self.keyEdit.setObjectName("keyEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 161, 16))
        self.label_3.setObjectName("label_3")
        self.resultEdit = QtWidgets.QLineEdit(Dialog)
        self.resultEdit.setGeometry(QtCore.QRect(40, 160, 321, 21))
        self.resultEdit.setObjectName("resultEdit")
        self.runButton = QtWidgets.QPushButton(Dialog)
        self.runButton.setGeometry(QtCore.QRect(140, 110, 113, 32))
        self.runButton.setObjectName("runButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 321, 51))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.runButton.clicked.connect(self.buttonSlot)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Input Plaintext"))
        self.label_2.setText(_translate("Dialog", "Input Key"))
        self.label_3.setText(_translate("Dialog", "Result (Cypertext)"))
        self.runButton.setText(_translate("Dialog", "Run DES"))
        self.label_4.setText(_translate("Dialog", "ERRORLIST"))
        self.plainEdit.setPlainText("123456ABCD132536")
        self.keyEdit.setPlainText("AABB09182736CCDD")

    def buttonSlot(self):
        _translate = QtCore.QCoreApplication.translate
        text = self.plainEdit.toPlainText() #initialized value: "123456ABCD132536"
        key = self.keyEdit.toPlainText() #initialized value: "AABB09182736CCDD"
        d = des()
        r = d.encrypt(key, text)
        r2 = d.decrypt(key, r)
        self.resultEdit.setText(_translate("Dialog", r))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
