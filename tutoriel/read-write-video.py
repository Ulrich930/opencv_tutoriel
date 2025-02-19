# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:49:27 2025

@author: HP
"""

import cv2 as cv
import sys  # Ajouter cette ligne pour utiliser sys.exit()

# Ouvrir la vidéo
cap = cv.VideoCapture("../videos/mavideo.mp4")

print(cap)

# Vérifier si la vidéo est bien ouverte
if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la vidéo.")
    sys.exit()  # Utiliser sys.exit() au lieu de exit()

# Lire la première frame pour obtenir les dimensions
ret, frame = cap.read()
if not ret:
    print("Erreur : Impossible de lire la vidéo.")
    sys.exit()  # Utiliser sys.exit() au lieu de exit()

hauteur, largeur = frame.shape[:2]

# Créer une fenêtre redimensionnable
cv.namedWindow('Vidéo', cv.WINDOW_NORMAL)

# Ajuster la taille de la fenêtre aux dimensions de la première frame
cv.resizeWindow('Vidéo', largeur, hauteur)

while True:
    # Lire la frame suivante
    ret, frame = cap.read()
    if not ret:
        break  # Sortir de la boucle si la vidéo est terminée

    # Afficher la frame dans la fenêtre
    cv.imshow('Vidéo', frame)

    # Attendre 25 ms et vérifier si l'utilisateur appuie sur la touche 'q' pour quitter
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

# Libérer les ressources et fermer les fenêtres
cap.release()
cv.destroyAllWindows()