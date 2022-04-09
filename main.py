# DSP Task 3
#libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication)
import numpy as np
import pandas as pd
import pyqtgraph as pg
import cv2 as cv
import math
import logging
from modesEnum import Modes
from imageModel import ImageModel
from design import *



logging.basicConfig(filename="loging_data.Log",level=logging.INFO)
log_file = logging.getLogger()

class Image_Mixer(Ui_MainWindow):
    def __init__ (self, MainWindow):
        super(Image_Mixer, self).setupUi(MainWindow)

        self.Widgets = [self.widget_mod1, self.widget_mod2, self.widget_2, self.widget_1, self.wid_output1, self.wid_output2]
        for wid in self.Widgets:
            wid.ui.histogram.hide()
            wid.ui.roiBtn.hide()
            wid.ui.menuBtn.hide()
            wid.ui.roiPlot.hide()
        self.widget_in = [self.widget_1, self.widget_2] 
        self.widget_mod = [self.widget_mod1, self.widget_mod2]
        self.wid_output = [self.wid_output1, self.wid_output2]
        self.Comb = [self.Comb_1, self.Comb_2] 
        self.images = [0,0]
        self.out_flag = [False, False]
        self.open_flag = [False, False]
        self.Mags = ["Magnitude", "Uniform Magnitude"]
        self.which_image = {0:1, 1:0}
        self.img_mixed_data = [0,0]
        self.radio_out1.setChecked(True)
        self.radio_com11.setChecked(True)
        self.radioButton_24.setChecked(True)
        self.Combo_com1.currentTextChanged.connect(self.component_select)
        self.actionOpen_Image.triggered.connect(lambda:self.open_Image(0))
        self.actionImage_2.triggered.connect(lambda: self.open_Image(1))
        self.Comb_1.currentTextChanged.connect(lambda:self.comp_construct(0))
        self.Comb_2.currentTextChanged.connect(lambda: self.comp_construct(1))
        self.Combo_com1.currentTextChanged.connect(self.mixer_input)
        self.Combo_com2.currentTextChanged.connect(self.mixer_input)
        self.horizontalSlider_17.valueChanged.connect(self.mixer_input)
        self.horizontalSlider_18.valueChanged.connect(self.mixer_input)
        self.radio_out1.toggled.connect(self.mixer_input)
        self.radio_com11.toggled.connect(self.mixer_input)
        self.r.toggled.connect(self.mixer_input)
        self.actionSave_1.triggered.connect(lambda: self.save_out(0))
        self.actionSave_2.triggered.connect(lambda : self.save_out(1))
        self.actionReset.triggered.connect(self.reset_data)
        log_file.info("Intializing and setting attributes")
        log_file.info("Assigning Fucntions to the window elements")


    def component_select(self):
        self.Combo_com2.clear()
        if (str(self.Combo_com1.currentText())) == "Magnitude":
            self.Combo_com2.addItem("Phase")
            self.Combo_com2.addItem("Uniform Phase")  
        elif (str(self.Combo_com1.currentText())) == "Uniform Magnitude":
            self.Combo_com2.addItem("Phase")
            self.Combo_com2.addItem("Uniform Phase")
        elif (str(self.Combo_com1.currentText())) == "Phase":
            self.Combo_com2.addItem("Magnitude")
            self.Combo_com2.addItem("Uniform Magnitude")   
        elif (str(self.Combo_com1.currentText())) == "Uniform Phase":
            self.Combo_com2.addItem("Magnitude")
            self.Combo_com2.addItem("Uniform Magnitude") 
        elif (str(self.Combo_com1.currentText())) == "Imaginary":
            self.Combo_com2.addItem("Real")
        elif (str(self.Combo_com1.currentText())) == "Real":
            self.Combo_com2.addItem("Imaginary")
        log_file.info("setting the options the user can select from")
        

    def open_Image(self,image_index):
        
        other_image = self.which_image[image_index]
        fname = QFileDialog.getOpenFileName(None, 'Open file','C:/Users/Al-Motasem/OneDrive/Desktop/Dsp 3', "Images (*.png *.xpm *.jpg)")
        if fname[0]:
            image = ImageModel(fname[0])
            if self.open_flag[other_image]:
                if (self.images[other_image].dim == (image.imgByte.shape[0], image.imgByte.shape[1])):
                    self.images[image_index] = image
                    self.plot_input(image_index)
                    log_file.info("opening and plotting an inmage")
                else: 
                    self.pop_up_error()
                    log_file.info("popping an error for selection a wrong size photo")
            else:   
                self.images[image_index] = image
                self.plot_input(image_index)
                log_file.info("opening and plotting an inmage")

    def plot_input(self, image_index):
        self.open_flag[image_index] = True
        self.widget_in[image_index].setImage(self.images[image_index].imgByte.T)
        self.widget_in[image_index].show()
        self.comp_construct(image_index)      

    def save_out(self,index):
        if all(self.open_flag):
            if self.out_flag[index]:
                fname = QFileDialog.getSaveFileName(None, 'Save file','/home', ".jpg")
                if fname[0]:
                    name = fname[0] + '.jpg'
                    cv.imwrite(name, self.img_mixed_data[index])
                    log_file.info("saving an image")



    def comp_construct(self,index):
        if self.open_flag[index]:
            if (str(self.Comb[index].currentText())) == "Magnitude":
                img_abs = np.abs(self.images[index].dft)
                img_shift = np.fft.fftshift(img_abs)
                img_final = np.log(img_shift + 1)
            elif (str(self.Comb[index].currentText())) == "Phase":
                img_final = self.images[index].phase
            elif (str(self.Comb[index].currentText())) == "Imaginary":
                img_imaginary = np.imag(self.images[index].dft)
                img_final = np.log(img_imaginary+1)
            elif(str(self.Comb[index].currentText())) == "Real":
                img_real = np.real(self.images[index].dft)
                img_final = np.log(img_real+1)
            log_file.info("plotting a component of the selected image")
            self.widget_mod[index].show()
            self.widget_mod[index].setImage(img_final.T)
        else:
            pass

    def mixer_input(self):
        if all(self.open_flag):
            self.label.setText(str(self.horizontalSlider_17.value()) +' %')
            self.label_3.setText(str(self.horizontalSlider_18.value())+ ' %')
            if self.radio_com11.isChecked():
                ind1 = 0
            else:
                ind1 = 1
            if self.r.isChecked():
                ind2 = 0
            else:
                ind2 = 1
            if self.radio_out1.isChecked():
                ind3 = 0
            else:
                ind3 = 1
            select_img1 = self.images[ind1]
            select_img2 = self.images[ind2]
            if(str(self.Combo_com1.currentText())) == "Magnitude":
                if(str(self.Combo_com2.currentText())) == "Phase":
                    self.img_mixed_data[ind3] = select_img1.mix(select_img2, self.horizontalSlider_17.value()/100, self.horizontalSlider_18.value()/100,Modes.magnitudeAndPhase)
                else:
                    self.img_mixed_data[ind3] = select_img1.mix(select_img2, self.horizontalSlider_17.value()/100, self.horizontalSlider_18.value()/100, Modes.uniformPhase)
            elif(str(self.Combo_com1.currentText())) == "Phase":
                if(str(self.Combo_com2.currentText())) == "Magnitude":
                    self.img_mixed_data[ind3] = select_img2.mix(select_img1, self.horizontalSlider_18.value()/100, self.horizontalSlider_17.value()/100,Modes.magnitudeAndPhase)
                else:
                    self.img_mixed_data[ind3] = select_img2.mix(select_img1, self.horizontalSlider_18.value(), self.horizontalSlider_17.value()/100, Modes.uniformMagnitude)
            elif(str(self.Combo_com1.currentText())) == "Imaginary":
                self.img_mixed_data[ind3] = select_img2.mix(select_img1, self.horizontalSlider_18.value()/100, self.horizontalSlider_17.value()/100,Modes.realAndImaginary)
            elif(str(self.Combo_com1.currentText())) == "Real":
                self.img_mixed_data[ind3] = select_img1.mix(select_img2, self.horizontalSlider_17.value()/100, self.horizontalSlider_18.value()/100,Modes.realAndImaginary)
            elif(str(self.Combo_com1.currentText())) == "Uniform Magnitude":
                if(str(self.Combo_com2.currentText())) == "Phase":
                    self.img_mixed_data[ind3] = select_img1.mix(select_img2, self.horizontalSlider_17.value()/100, self.horizontalSlider_18.value()/100,Modes.uniformMagnitude)
                else:
                    self.img_mixed_data[ind3] = select_img1.mix(select_img2, self.horizontalSlider_17.value()/100, self.horizontalSlider_18.value()/100, Modes.uniMagnitudePhase)
            elif(str(self.Combo_com1.currentText())) == "Uniform Phase":
                if(str(self.Combo_com2.currentText())) == "Magnitude":
                    self.img_mixed_data[ind3] = select_img2.mix(select_img1, self.horizontalSlider_18.value()/100, self.horizontalSlider_17.value()/100, Modes.uniformPhase)
                else:
                    self.img_mixed_data[ind3] = select_img2.mix(select_img1, self.horizontalSlider_18.value()/100, self.horizontalSlider_18.value()/100, Modes.uniMagnitudePhase)
            log_file.info("plotting mixed image")
            self.out_flag[ind3] = True
            self.wid_output[ind3].show()
            self.wid_output[ind3].setImage(self.img_mixed_data[ind3].T)


    def pop_up_error(self):
        error = QtWidgets.QMessageBox()
        error.setText("Please, select a photo that is consistant with previous one")
        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.exec()

    def reset_data(self):
        self.images = [0,0]
        self.out_flag = [False, False]
        self.open_flag = [False, False]
        self.radio_out1.setChecked(True)
        self.radio_com11.setChecked(True)
        self.radioButton_24.setChecked(True)
        self.horizontalSlider_17.setValue(0)
        self.horizontalSlider_18.setValue(0)
        self.label.setText("0 %")
        self.label_3.setText("0 %")
        self.Combo_com1.setCurrentText("Magnitude")
        self.Comb_1.setCurrentText("Magnitude")
        self.Comb_2.setCurrentText("Magnitude")
        self.component_select()
        log_file.info("resettting the program")
        for ele in self.Widgets:
            ele.clear()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Image_Mixer(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())