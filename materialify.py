# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 03:17:40 2022

@author: Burak Alanyalıoğlu
GitHub: @felsefesinde
Instagram: @felsefesinde
YouTube: Felsefesinde
Twitter: @felsefesinde & @binichburak
MIT License

Copyright (c) 2022 Burak Alanyalıoğlu
"""

import numpy as np


class materialify(object):
    def __init__(self, applied_stress, plane_ind, direction_ind, tensile_stress, crss):
       	self.__applied_stress = applied_stress
       	self.__plane_ind = plane_ind
       	self.__direction_ind = direction_ind
       	self.__tensile_stress = tensile_stress
        self.__crss = crss
    
    def cos_calc(self, arr1, arr2):
        return ((np.dot(arr1, arr2))) / ((((np.linalg.norm(arr1))) * np.linalg.norm(arr2)))
    
    def tau_crss(self, sigma, cos_fi, cos_lambda):
        return sigma * cos_fi * cos_lambda
    
    def yield_strength(self):
        return f"The magnitude of the applied stress to initiate yielding is {self.__crss / ((self.cos_calc(self.__applied_stress, self.__plane_ind)) * (self.cos_calc(self.__applied_stress, self.__direction_ind))):.3f} MPa for a material with a CRSS value of {self.__crss} MPa."
    
    def __repr__(self):
        return f"Resolved Shear Stress is {self.tau_crss(self.__tensile_stress, self.cos_calc(self.__applied_stress, self.__plane_ind), self.cos_calc(self.__applied_stress, self.__direction_ind)):.3f} MPa"
    
    
    
applied_stress = input("Miller indices of applied stress: ").split()
applied_stress = [int(x) for x in applied_stress]

plane_ind = input("Miller indices for shear stress along the plane: ").split()
plane_ind = [int(x) for x in plane_ind]

direction_ind = input("Miller indices for shear stress along the direction: ").split()
direction_ind = [int(x) for x in direction_ind]

tensile_stress = float(input("Please enter the tensile stress (MPa): "))

crss = float(input("Please enter the Critical Resolved Shear Stress [CRSS] (MPa): "))

material = materialify(applied_stress, plane_ind, direction_ind, tensile_stress, crss)

print(material.yield_strength())

