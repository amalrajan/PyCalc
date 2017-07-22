# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class UserInterface(object):
    def __init__(self):
        # Initializing the instance attributes.
        self.gridLayout = None
        self.gridLayout_2 = None

        self.button_c = None
        self.button_squareroot = None
        self.button_minus = None
        self.button_one = None
        self.button_two = None
        self.button_three = None
        self.button_four = None
        self.button_five = None
        self.button_six = None
        self.button_seven = None
        self.button_eight = None
        self.button_nine = None
        self.button_plus = None
        self.button_reciprocal = None
        self.button_square = None
        self.button_ce = None
        self.button_divide = None
        self.button_multiply = None
        self.button_backspace = None
        self.button_plusminus = None
        self.button_zero = None
        self.button_decimal = None
        self.button_equals = None

        self.label = None
        self.horizontalLayout = None
        self.pushButton_26 = None
        self.pushButton_25 = None
        self.pushButton_27 = None
        self.pushButton_28 = None
        self.pushButton_29 = None

        self.line_result = None




    def initialize_ui(self, Form):
        Form.setObjectName("PyCalcs")
        Form.resize(340, 595)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setAutoFillBackground(False)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_c = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_c.sizePolicy().hasHeightForWidth())
        self.button_c.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_c.setFont(font)
        self.button_c.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(255, 39, 39);\n"
            "    border: 0;\n"
            "    border-radius: 6px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_c.setObjectName("button_c")
        self.gridLayout.addWidget(self.button_c, 1, 1, 1, 1)
        self.button_squareroot = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_squareroot.sizePolicy().hasHeightForWidth())
        self.button_squareroot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_squareroot.setFont(font)
        self.button_squareroot.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_squareroot.setIconSize(QtCore.QSize(16, 16))
        self.button_squareroot.setFlat(False)
        self.button_squareroot.setObjectName("button_squareroot")
        self.gridLayout.addWidget(self.button_squareroot, 0, 1, 1, 1)
        self.button_minus = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_minus.sizePolicy().hasHeightForWidth())
        self.button_minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_minus.setFont(font)
        self.button_minus.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(209, 209, 209);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_minus.setObjectName("button_minus")
        self.gridLayout.addWidget(self.button_minus, 3, 3, 1, 1)
        self.button_one = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_one.sizePolicy().hasHeightForWidth())
        self.button_one.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_one.setFont(font)
        self.button_one.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_one.setObjectName("button_one")
        self.gridLayout.addWidget(self.button_one, 4, 0, 1, 1)
        self.button_two = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_two.sizePolicy().hasHeightForWidth())
        self.button_two.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_two.setFont(font)
        self.button_two.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_two.setObjectName("button_two")
        self.gridLayout.addWidget(self.button_two, 4, 1, 1, 1)
        self.button_three = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_three.sizePolicy().hasHeightForWidth())
        self.button_three.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_three.setFont(font)
        self.button_three.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_three.setObjectName("button_three")
        self.gridLayout.addWidget(self.button_three, 4, 2, 1, 1)
        self.button_plus = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_plus.sizePolicy().hasHeightForWidth())
        self.button_plus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_plus.setFont(font)
        self.button_plus.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(209, 209, 209);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_plus.setObjectName("button_plus")
        self.gridLayout.addWidget(self.button_plus, 4, 3, 1, 1)
        self.button_reciprocal = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_reciprocal.sizePolicy().hasHeightForWidth())
        self.button_reciprocal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_reciprocal.setFont(font)
        self.button_reciprocal.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_reciprocal.setIconSize(QtCore.QSize(16, 16))
        self.button_reciprocal.setFlat(False)
        self.button_reciprocal.setObjectName("button_reciprocal")
        self.gridLayout.addWidget(self.button_reciprocal, 0, 3, 1, 1)
        self.button_square = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_square.sizePolicy().hasHeightForWidth())
        self.button_square.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_square.setFont(font)
        self.button_square.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_square.setIconSize(QtCore.QSize(16, 16))
        self.button_square.setFlat(False)
        self.button_square.setObjectName("button_square")
        self.gridLayout.addWidget(self.button_square, 0, 2, 1, 1)
        self.button_ce = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_ce.sizePolicy().hasHeightForWidth())
        self.button_ce.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_ce.setFont(font)
        self.button_ce.setStyleSheet(
            "QPushButton {\n"
            "    background-color:rgb(255, 98, 87);\n"
            "    border: 0;\n"
            "    border-radius: 6px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_ce.setObjectName("button_ce")
        self.gridLayout.addWidget(self.button_ce, 1, 0, 1, 1)
        self.button_seven = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_seven.sizePolicy().hasHeightForWidth())
        self.button_seven.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_seven.setFont(font)
        self.button_seven.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_seven.setObjectName("button_seven")
        self.gridLayout.addWidget(self.button_seven, 2, 0, 1, 1)
        self.button_divide = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_divide.sizePolicy().hasHeightForWidth())
        self.button_divide.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_divide.setFont(font)
        self.button_divide.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(209, 209, 209);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_divide.setObjectName("button_divide")
        self.gridLayout.addWidget(self.button_divide, 1, 3, 1, 1)
        self.button_eight = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_eight.sizePolicy().hasHeightForWidth())
        self.button_eight.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_eight.setFont(font)
        self.button_eight.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_eight.setObjectName("button_eight")
        self.gridLayout.addWidget(self.button_eight, 2, 1, 1, 1)
        self.button_nine = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_nine.sizePolicy().hasHeightForWidth())
        self.button_nine.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_nine.setFont(font)
        self.button_nine.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_nine.setObjectName("button_nine")
        self.gridLayout.addWidget(self.button_nine, 2, 2, 1, 1)
        self.button_multiply = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_multiply.sizePolicy().hasHeightForWidth())
        self.button_multiply.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_multiply.setFont(font)
        self.button_multiply.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(209, 209, 209);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_multiply.setObjectName("button_multiply")
        self.gridLayout.addWidget(self.button_multiply, 2, 3, 1, 1)
        self.button_five = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_five.sizePolicy().hasHeightForWidth())
        self.button_five.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_five.setFont(font)
        self.button_five.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_five.setObjectName("button_five")
        self.gridLayout.addWidget(self.button_five, 3, 1, 1, 1)
        self.button_modulus = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_modulus.sizePolicy().hasHeightForWidth())
        self.button_modulus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_modulus.setFont(font)
        self.button_modulus.setMouseTracking(False)
        self.button_modulus.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_modulus.setIconSize(QtCore.QSize(16, 16))
        self.button_modulus.setFlat(False)
        self.button_modulus.setObjectName("button_modulus")
        self.gridLayout.addWidget(self.button_modulus, 0, 0, 1, 1)
        self.button_backspace = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_backspace.sizePolicy().hasHeightForWidth())
        self.button_backspace.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_backspace.setFont(font)
        self.button_backspace.setStyleSheet(
            "QPushButton {\n"
            "    background-color:rgb(255, 98, 87);\n"
            "    border: 0;\n"
            "    border-radius: 6px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_backspace.setObjectName("button_backspace")
        self.gridLayout.addWidget(self.button_backspace, 1, 2, 1, 1)
        self.button_four = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_four.sizePolicy().hasHeightForWidth())
        self.button_four.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_four.setFont(font)
        self.button_four.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_four.setObjectName("button_four")
        self.gridLayout.addWidget(self.button_four, 3, 0, 1, 1)
        self.button_six = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_six.sizePolicy().hasHeightForWidth())
        self.button_six.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_six.setFont(font)
        self.button_six.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_six.setObjectName("button_six")
        self.gridLayout.addWidget(self.button_six, 3, 2, 1, 1)
        self.button_plusminus = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_plusminus.sizePolicy().hasHeightForWidth())
        self.button_plusminus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_plusminus.setFont(font)
        self.button_plusminus.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_plusminus.setObjectName("button_plusminus")
        self.gridLayout.addWidget(self.button_plusminus, 5, 0, 1, 1)
        self.button_zero = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_zero.sizePolicy().hasHeightForWidth())
        self.button_zero.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_zero.setFont(font)
        self.button_zero.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_zero.setObjectName("button_zero")
        self.gridLayout.addWidget(self.button_zero, 5, 1, 1, 1)
        self.button_decimal = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_decimal.sizePolicy().hasHeightForWidth())
        self.button_decimal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_decimal.setFont(font)
        self.button_decimal.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_decimal.setObjectName("button_decimal")
        self.gridLayout.addWidget(self.button_decimal, 5, 2, 1, 1)
        self.button_equals = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_equals.sizePolicy().hasHeightForWidth())
        self.button_equals.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.button_equals.setFont(font)
        self.button_equals.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(28, 213, 0) ;\n"
            "    border: 0;\n"
            "    border-radius: 6px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(0, 191, 0) ;\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    border: 0;\n"
            "    color: white;\n"
            " }")
        self.button_equals.setObjectName("button_equals")
        self.gridLayout.addWidget(self.button_equals, 5, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_26 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    color: white;\n"
            "    border: 0;\n"
            " }")
        self.pushButton_26.setObjectName("pushButton_26")
        self.horizontalLayout.addWidget(self.pushButton_26)
        self.pushButton_25 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    color: white;\n"
            "    border: 0;\n"
            " }")
        self.pushButton_25.setObjectName("pushButton_25")
        self.horizontalLayout.addWidget(self.pushButton_25)
        self.pushButton_27 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    color: white;\n"
            "    border: 0;\n"
            " }")
        self.pushButton_27.setObjectName("pushButton_27")
        self.horizontalLayout.addWidget(self.pushButton_27)
        self.pushButton_28 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    color: white;\n"
            "    border: 0;\n"
            " }")
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout.addWidget(self.pushButton_28)
        self.pushButton_29 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(182, 182, 182);\n"
            "    border: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed { \n"
            "    background-color: rgb(0, 0, 0);\n"
            "    color: white;\n"
            "    border: 0;\n"
            " }")
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout.addWidget(self.pushButton_29)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text_expression = QtWidgets.QTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.text_expression.sizePolicy().hasHeightForWidth())
        self.text_expression.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(13)
        self.text_expression.setFont(font)
        self.text_expression.setToolTip("")
        self.text_expression.setToolTipDuration(3)
        self.text_expression.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_expression.setStyleSheet(
            "QTextEdit{\n"
            "    border: 0;\n"
            "}")
        self.text_expression.setUndoRedoEnabled(False)
        self.text_expression.setAcceptRichText(False)
        self.text_expression.setCursorWidth(10)
        self.text_expression.setObjectName("text_expression")
        self.verticalLayout_2.addWidget(self.text_expression)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.line_result = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(13)
        self.line_result.setFont(font)
        self.line_result.setReadOnly(True)
        self.line_result.setObjectName("line_result")
        self.gridLayout_2.addWidget(self.line_result, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("PyCalc", "PyCalc"))
        self.button_c.setText(_translate("PyCalc", "C"))
        self.button_squareroot.setText(_translate("PyCalc", "√"))
        self.button_minus.setText(_translate("PyCalc", "-"))
        self.button_one.setText(_translate("PyCalc", "1"))
        self.button_two.setText(_translate("PyCalc", "2"))
        self.button_three.setText(_translate("PyCalc", "3"))
        self.button_plus.setText(_translate("PyCalc", "+"))
        self.button_reciprocal.setText(_translate("PyCalc", "1/x"))
        self.button_square.setText(_translate("PyCalc", "x²"))
        self.button_ce.setText(_translate("PyCalc", "CE"))
        self.button_seven.setText(_translate("PyCalc", "7"))
        self.button_divide.setText(_translate("PyCalc", "÷"))
        self.button_eight.setText(_translate("PyCalc", "8"))
        self.button_nine.setText(_translate("PyCalc", "9"))
        self.button_multiply.setText(_translate("PyCalc", "x"))
        self.button_five.setText(_translate("PyCalc", "5"))
        self.button_modulus.setText(_translate("PyCalc", "%"))
        self.button_backspace.setText(_translate("PyCalc", "<<"))
        self.button_four.setText(_translate("PyCalc", "4"))
        self.button_six.setText(_translate("PyCalc", "6"))
        self.button_plusminus.setText(_translate("PyCalc", "±"))
        self.button_zero.setText(_translate("PyCalc", "0"))
        self.button_decimal.setText(_translate("PyCalc", "."))
        self.button_equals.setText(_translate("PyCalc", "="))
        self.label.setText(_translate("PyCalc", "Standard Mode"))
        self.pushButton_26.setText(_translate("PyCalc", "MC"))
        self.pushButton_25.setText(_translate("PyCalc", "MR"))
        self.pushButton_27.setText(_translate("PyCalc", "M+"))
        self.pushButton_28.setText(_translate("PyCalc", "M-"))
        self.pushButton_29.setText(_translate("PyCalc", "MS"))
        self.text_expression.setPlaceholderText(_translate("PyCalc", "expression or command here."))
        self.line_result.setPlaceholderText(_translate("PyCalc", "result."))