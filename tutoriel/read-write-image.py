# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:29:21 2025

@author: HP
"""

import cv2 as cv

img = cv.imread("../images/cochon.jpg")

# Récupérer les dimensions de l'image
hauteur, largeur = img.shape[:2]

# Créer une fenêtre redimensionnable
cv.namedWindow('Cochon', cv.WINDOW_NORMAL)

# Ajuster la taille de la fenêtre à celle de l'image
cv.resizeWindow('Cochon', largeur, hauteur)

cv.imshow('Cochon', img)
cv.waitKey(0)
cv.destroyAllWindows()