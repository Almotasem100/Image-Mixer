## This is the abstract class that the students should implement  

from modesEnum import Modes
import cv2 as cv
import numpy as np

class ImageModel():

    """
    A class that represents the ImageModel"
    """
    '''
    def __init__(self):
        pass
    '''
    def __init__(self, imgPath: str):
        
        self.imgPath = imgPath
        self.imgByte = cv.imread(self.imgPath)
        self.imgByte = cv.cvtColor(self.imgByte, cv.COLOR_BGR2GRAY)
        self.dft = np.fft.fftn(self.imgByte)
        self.real = np.real(self.dft)
        self.imaginary = np.imag(self.dft)
        self.magnitude = np.abs(self.dft)
        self.phase = np.angle(self.dft)
        self.dim = (self.imgByte.shape[0], self.imgByte.shape[1])


   
    def mix(self, imageToBeMixed: 'ImageModel', magnitudeOrRealRatio: float, phaesOrImaginaryRatio: float, mode: 'Modes') -> np.ndarray:
        if mode == Modes.magnitudeAndPhase:
            new_magnitude = self.magnitude * magnitudeOrRealRatio + imageToBeMixed.magnitude * (1-magnitudeOrRealRatio)
            new_phase = self.phase * (1-phaesOrImaginaryRatio) + imageToBeMixed.phase * phaesOrImaginaryRatio
            new_data = new_magnitude * np.exp(new_phase*1j)
            
        elif mode == Modes.realAndImaginary:
            new_real = self.real * magnitudeOrRealRatio + imageToBeMixed.real * (1-magnitudeOrRealRatio)
            new_imaginary = self.imaginary * (1-phaesOrImaginaryRatio) + imageToBeMixed.imaginary * phaesOrImaginaryRatio
            new_data = new_real + new_imaginary*1j
        
        elif mode == Modes.uniformMagnitude:
            new_magnitude = np.ones(self.magnitude.shape)
            new_phase = self.phase * (1-phaesOrImaginaryRatio) + imageToBeMixed.phase * phaesOrImaginaryRatio
            new_data = new_magnitude * np.exp(new_phase*1j)

        elif mode == Modes.uniformPhase:
            new_magnitude = self.magnitude * magnitudeOrRealRatio + imageToBeMixed.magnitude * (1-magnitudeOrRealRatio)
            new_phase = np.zeros(self.phase.shape)
            new_data = new_magnitude * np.exp(new_phase*1j)
        elif mode == Modes.uniMagnitudePhase:
            new_magnitude = np.ones(self.magnitude.shape)
            new_phase = np.zeros(self.phase.shape)
            new_data = new_magnitude * np.exp(new_phase*1j)
            
        new_data = np.fft.ifftn(new_data)
        return np.real(new_data)
