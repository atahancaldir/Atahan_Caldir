# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookDetails.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bookDetailsWindow(object):
    def setupUi(self, bookDetailsWindow):
        bookDetailsWindow.setObjectName("bookDetailsWindow")
        bookDetailsWindow.resize(997, 418)
        bookDetailsWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/Logom2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        bookDetailsWindow.setWindowIcon(icon)
        bookDetailsWindow.setStyleSheet("background:#80c5ed;")
        self.label = QtWidgets.QLabel(bookDetailsWindow)
        self.label.setGeometry(QtCore.QRect(120, 20, 861, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(bookDetailsWindow)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 861, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.edit_but = QtWidgets.QPushButton(bookDetailsWindow)
        self.edit_but.setGeometry(QtCore.QRect(10, 10, 60, 60))
        self.edit_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_but.setStyleSheet("background:#3e8fc9;\n"
"border-radius:10px;")
        self.edit_but.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("media/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_but.setIcon(icon1)
        self.edit_but.setIconSize(QtCore.QSize(45, 45))
        self.edit_but.setObjectName("edit_but")
        self.book_name_label = QtWidgets.QLineEdit(bookDetailsWindow)
        self.book_name_label.setEnabled(True)
        self.book_name_label.setGeometry(QtCore.QRect(120, 60, 861, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setItalic(False)
        self.book_name_label.setFont(font)
        self.book_name_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.book_name_label.setStyleSheet("background:#80c5ed;\n"
"border:0px;")
        self.book_name_label.setText("")
        self.book_name_label.setReadOnly(True)
        self.book_name_label.setClearButtonEnabled(False)
        self.book_name_label.setObjectName("book_name_label")
        self.author_name_label = QtWidgets.QLineEdit(bookDetailsWindow)
        self.author_name_label.setGeometry(QtCore.QRect(120, 160, 861, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setItalic(False)
        self.author_name_label.setFont(font)
        self.author_name_label.setStyleSheet("background:#80c5ed;\n"
"border:0px;")
        self.author_name_label.setText("")
        self.author_name_label.setReadOnly(True)
        self.author_name_label.setObjectName("author_name_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(bookDetailsWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 210, 861, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.page_label = QtWidgets.QLineEdit(bookDetailsWindow)
        self.page_label.setGeometry(QtCore.QRect(560, 270, 421, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setItalic(False)
        self.page_label.setFont(font)
        self.page_label.setStyleSheet("background:#80c5ed;\n"
"border:0px;")
        self.page_label.setText("")
        self.page_label.setReadOnly(True)
        self.page_label.setObjectName("page_label")
        self.owned_check = QtWidgets.QCheckBox(bookDetailsWindow)
        self.owned_check.setGeometry(QtCore.QRect(120, 320, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.owned_check.setFont(font)
        self.owned_check.setObjectName("owned_check")
        self.read_check = QtWidgets.QCheckBox(bookDetailsWindow)
        self.read_check.setGeometry(QtCore.QRect(120, 370, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.read_check.setFont(font)
        self.read_check.setObjectName("read_check")
        self.save_but = QtWidgets.QPushButton(bookDetailsWindow)
        self.save_but.setGeometry(QtCore.QRect(10, 120, 60, 60))
        self.save_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_but.setStyleSheet("background:#3e8fc9;\n"
"border-radius:10px;")
        self.save_but.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("media/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_but.setIcon(icon2)
        self.save_but.setIconSize(QtCore.QSize(40, 40))
        self.save_but.setObjectName("save_but")
        self.delete_but = QtWidgets.QPushButton(bookDetailsWindow)
        self.delete_but.setGeometry(QtCore.QRect(10, 230, 60, 60))
        self.delete_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_but.setStyleSheet("background:#3e8fc9;\n"
"border-radius:10px;")
        self.delete_but.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("media/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_but.setIcon(icon3)
        self.delete_but.setIconSize(QtCore.QSize(45, 45))
        self.delete_but.setObjectName("delete_but")
        self.label_6 = QtWidgets.QLabel(bookDetailsWindow)
        self.label_6.setGeometry(QtCore.QRect(10, 72, 60, 20))
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(bookDetailsWindow)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 60, 20))
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(bookDetailsWindow)
        self.label_8.setGeometry(QtCore.QRect(10, 290, 60, 20))
        self.label_8.setStyleSheet("color:white;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.cat_combo = QtWidgets.QComboBox(bookDetailsWindow)
        self.cat_combo.setEnabled(False)
        self.cat_combo.setGeometry(QtCore.QRect(120, 270, 421, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.cat_combo.setFont(font)
        self.cat_combo.setAutoFillBackground(False)
        self.cat_combo.setStyleSheet("background:#3e8fc9;\n"
"color:white;")
        self.cat_combo.setEditable(False)
        self.cat_combo.setObjectName("cat_combo")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")
        self.cat_combo.addItem("")

        self.retranslateUi(bookDetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(bookDetailsWindow)

    def retranslateUi(self, bookDetailsWindow):
        _translate = QtCore.QCoreApplication.translate
        bookDetailsWindow.setWindowTitle(_translate("bookDetailsWindow", "Book Details"))
        self.label.setText(_translate("bookDetailsWindow", "Book Name"))
        self.label_2.setText(_translate("bookDetailsWindow", "Author Name"))
        self.label_3.setText(_translate("bookDetailsWindow", "Category"))
        self.label_4.setText(_translate("bookDetailsWindow", "Page Number"))
        self.owned_check.setText(_translate("bookDetailsWindow", "Owned"))
        self.read_check.setText(_translate("bookDetailsWindow", "Read"))
        self.label_6.setText(_translate("bookDetailsWindow", "Edit"))
        self.label_7.setText(_translate("bookDetailsWindow", "Save"))
        self.label_8.setText(_translate("bookDetailsWindow", "Delete"))
        self.cat_combo.setItemText(0, _translate("bookDetailsWindow", "Academic"))
        self.cat_combo.setItemText(1, _translate("bookDetailsWindow", "Art"))
        self.cat_combo.setItemText(2, _translate("bookDetailsWindow", "Biography"))
        self.cat_combo.setItemText(3, _translate("bookDetailsWindow", "Business"))
        self.cat_combo.setItemText(4, _translate("bookDetailsWindow", "Economics"))
        self.cat_combo.setItemText(5, _translate("bookDetailsWindow", "History"))
        self.cat_combo.setItemText(6, _translate("bookDetailsWindow", "Law"))
        self.cat_combo.setItemText(7, _translate("bookDetailsWindow", "Novel"))
        self.cat_combo.setItemText(8, _translate("bookDetailsWindow", "Personal Evolution"))
        self.cat_combo.setItemText(9, _translate("bookDetailsWindow", "Philosophy"))
        self.cat_combo.setItemText(10, _translate("bookDetailsWindow", "Poetry"))
        self.cat_combo.setItemText(11, _translate("bookDetailsWindow", "Politics"))
        self.cat_combo.setItemText(12, _translate("bookDetailsWindow", "Religion"))
        self.cat_combo.setItemText(13, _translate("bookDetailsWindow", "Science"))
        self.cat_combo.setItemText(14, _translate("bookDetailsWindow", "Turkish Literature"))
        self.cat_combo.setItemText(15, _translate("bookDetailsWindow", "World Literature"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bookDetailsWindow = QtWidgets.QWidget()
    ui = Ui_bookDetailsWindow()
    ui.setupUi(bookDetailsWindow)
    bookDetailsWindow.show()
    sys.exit(app.exec_())