# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1039, 914)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(794, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_25 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setScaledContents(False)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_39.addWidget(self.label_25)
        self.Comb_1 = QtWidgets.QComboBox(self.frame_3)
        self.Comb_1.setObjectName("Comb_1")
        self.Comb_1.addItem("")
        self.Comb_1.addItem("")
        self.Comb_1.addItem("")
        self.Comb_1.addItem("")
        self.horizontalLayout_39.addWidget(self.Comb_1)
        self.gridLayout_2.addLayout(self.horizontalLayout_39, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.frame_15 = QtWidgets.QFrame(self.frame_2)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.label_2 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_45.addWidget(self.label_2)
        self.Comb_2 = QtWidgets.QComboBox(self.frame_15)
        self.Comb_2.setObjectName("Comb_2")
        self.Comb_2.addItem("")
        self.Comb_2.addItem("")
        self.Comb_2.addItem("")
        self.Comb_2.addItem("")
        self.horizontalLayout_45.addWidget(self.Comb_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_45, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_15)
        self.gridLayout_18.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_14 = QtWidgets.QFrame(self.frame)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 320))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_14)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_14)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_1 = ImageView(self.frame_4)
        self.widget_1.setObjectName("widget_1")
        self.gridLayout_4.addWidget(self.widget_1, 0, 0, 1, 1)
        self.widget_mod1 = ImageView(self.frame_4)
        self.widget_mod1.setObjectName("widget_mod1")
        self.gridLayout_4.addWidget(self.widget_mod1, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_14)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_2 = ImageView(self.frame_5)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5.addWidget(self.widget_2, 0, 0, 1, 1)
        self.widget_mod2 = ImageView(self.frame_5)
        self.widget_mod2.setObjectName("widget_mod2")
        self.gridLayout_5.addWidget(self.widget_mod2, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.gridLayout_17.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_14)
        self.frame_17 = QtWidgets.QFrame(self.frame)
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_16 = QtWidgets.QFrame(self.frame_17)
        self.frame_16.setMaximumSize(QtCore.QSize(700, 16777215))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_7 = QtWidgets.QFrame(self.frame_16)
        self.frame_7.setMaximumSize(QtCore.QSize(600, 50))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_7 = QtWidgets.QLabel(self.frame_7)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_9.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame_16)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.wid_output1 = ImageView(self.frame_6)
        self.wid_output1.setObjectName("wid_output1")
        self.horizontalLayout_38.addWidget(self.wid_output1)
        self.wid_output2 = ImageView(self.frame_6)
        self.wid_output2.setObjectName("wid_output2")
        self.horizontalLayout_38.addWidget(self.wid_output2)
        self.gridLayout_8.addLayout(self.horizontalLayout_38, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_6)
        self.gridLayout_19.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_16)
        self.frame_8 = QtWidgets.QFrame(self.frame_17)
        self.frame_8.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setMaximumSize(QtCore.QSize(4050, 65))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.label_26 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setScaledContents(False)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_40.addWidget(self.label_26)
        self.radio_out1 = QtWidgets.QRadioButton(self.frame_9)
        self.radio_out1.setObjectName("radio_out1")
        self.horizontalLayout_40.addWidget(self.radio_out1)
        self.radio_out2 = QtWidgets.QRadioButton(self.frame_9)
        self.radio_out2.setObjectName("radio_out2")
        self.horizontalLayout_40.addWidget(self.radio_out2)
        self.gridLayout_10.addLayout(self.horizontalLayout_40, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.label_27 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setScaledContents(False)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_41.addWidget(self.label_27)
        self.label = QtWidgets.QLabel(self.frame_10)
        self.label.setObjectName("label")
        self.horizontalLayout_41.addWidget(self.label)
        self.horizontalSlider_17 = QtWidgets.QSlider(self.frame_10)
        self.horizontalSlider_17.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_17.setObjectName("horizontalSlider_17")
        self.horizontalLayout_41.addWidget(self.horizontalSlider_17)
        self.gridLayout_11.addLayout(self.horizontalLayout_41, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.Combo_com1 = QtWidgets.QComboBox(self.frame_11)
        self.Combo_com1.setObjectName("Combo_com1")
        self.Combo_com1.addItem("")
        self.Combo_com1.addItem("")
        self.Combo_com1.addItem("")
        self.Combo_com1.addItem("")
        self.Combo_com1.addItem("")
        self.Combo_com1.addItem("")
        self.horizontalLayout_42.addWidget(self.Combo_com1)
        self.radio_com11 = QtWidgets.QRadioButton(self.frame_11)
        self.radio_com11.setObjectName("radio_com11")
        self.horizontalLayout_42.addWidget(self.radio_com11)
        self.radio_com12 = QtWidgets.QRadioButton(self.frame_11)
        self.radio_com12.setObjectName("radio_com12")
        self.horizontalLayout_42.addWidget(self.radio_com12)
        self.gridLayout_12.addLayout(self.horizontalLayout_42, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_8)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_28 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setScaledContents(False)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_5.addWidget(self.label_28)
        self.label_3 = QtWidgets.QLabel(self.frame_12)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.horizontalSlider_18 = QtWidgets.QSlider(self.frame_12)
        self.horizontalSlider_18.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_18.setObjectName("horizontalSlider_18")
        self.horizontalLayout_5.addWidget(self.horizontalSlider_18)
        self.gridLayout_14.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_8)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.Combo_com2 = QtWidgets.QComboBox(self.frame_13)
        self.Combo_com2.setObjectName("Combo_com2")
        self.Combo_com2.addItem("")
        self.Combo_com2.addItem("")
        self.horizontalLayout_44.addWidget(self.Combo_com2)
        self.r = QtWidgets.QRadioButton(self.frame_13)
        self.r.setObjectName("r")
        self.horizontalLayout_44.addWidget(self.r)
        self.radioButton_24 = QtWidgets.QRadioButton(self.frame_13)
        self.radioButton_24.setObjectName("radioButton_24")
        self.horizontalLayout_44.addWidget(self.radioButton_24)
        self.gridLayout_15.addLayout(self.horizontalLayout_44, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_13)
        self.gridLayout_16.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_8)
        self.gridLayout_20.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_17)
        self.gridLayout_21.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1039, 26))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        self.menuSave = QtWidgets.QMenu(self.menubar)
        self.menuSave.setObjectName("menuSave")
        self.menuOther = QtWidgets.QMenu(self.menubar)
        self.menuOther.setObjectName("menuOther")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Image = QtWidgets.QAction(MainWindow)
        self.actionOpen_Image.setObjectName("actionOpen_Image")
        self.actionImage_2 = QtWidgets.QAction(MainWindow)
        self.actionImage_2.setObjectName("actionImage_2")
        self.actionSave_1 = QtWidgets.QAction(MainWindow)
        self.actionSave_1.setObjectName("actionSave_1")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.menuOpen.addAction(self.actionOpen_Image)
        self.menuOpen.addAction(self.actionImage_2)
        self.menuSave.addAction(self.actionSave_1)
        self.menuSave.addAction(self.actionSave_2)
        self.menuOther.addAction(self.actionReset)
        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menuSave.menuAction())
        self.menubar.addAction(self.menuOther.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_25.setText(_translate("MainWindow", "  Image 1 Display   "))
        self.Comb_1.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.Comb_1.setItemText(1, _translate("MainWindow", "Phase"))
        self.Comb_1.setItemText(2, _translate("MainWindow", "Real"))
        self.Comb_1.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.label_2.setText(_translate("MainWindow", "  Image 2 Display   "))
        self.Comb_2.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.Comb_2.setItemText(1, _translate("MainWindow", "Phase"))
        self.Comb_2.setItemText(2, _translate("MainWindow", "Real"))
        self.Comb_2.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.label_6.setText(_translate("MainWindow", " Output 1"))
        self.label_7.setText(_translate("MainWindow", "Output 2"))
        self.label_26.setText(_translate("MainWindow", "  Mixer Options:      "))
        self.radio_out1.setText(_translate("MainWindow", "Output 1"))
        self.radio_out2.setText(_translate("MainWindow", "Output 2"))
        self.label_27.setText(_translate("MainWindow", "  Component 1:"))
        self.label.setText(_translate("MainWindow", "0%"))
        self.Combo_com1.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.Combo_com1.setItemText(1, _translate("MainWindow", "Uniform Magnitude"))
        self.Combo_com1.setItemText(2, _translate("MainWindow", "Phase"))
        self.Combo_com1.setItemText(3, _translate("MainWindow", "Uniform Phase"))
        self.Combo_com1.setItemText(4, _translate("MainWindow", "Real"))
        self.Combo_com1.setItemText(5, _translate("MainWindow", "Imaginary"))
        self.radio_com11.setText(_translate("MainWindow", "Image 1"))
        self.radio_com12.setText(_translate("MainWindow", "Image 2"))
        self.label_28.setText(_translate("MainWindow", "  Component 2:"))
        self.label_3.setText(_translate("MainWindow", "0%"))
        self.Combo_com2.setItemText(0, _translate("MainWindow", "Phase"))
        self.Combo_com2.setItemText(1, _translate("MainWindow", "Uniform Phase"))
        self.r.setText(_translate("MainWindow", "Image 1"))
        self.radioButton_24.setText(_translate("MainWindow", "Image 2"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuOther.setTitle(_translate("MainWindow", "Other"))
        self.actionOpen_Image.setText(_translate("MainWindow", "Image 1"))
        self.actionOpen_Image.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionImage_2.setText(_translate("MainWindow", "Image 2"))
        self.actionImage_2.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionSave_1.setText(_translate("MainWindow", "Save 1"))
        self.actionSave_1.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_2.setText(_translate("MainWindow", "Save 2"))
        self.actionSave_2.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
from pyqtgraph import ImageView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
