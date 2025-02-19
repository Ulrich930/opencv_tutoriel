# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:46:23 2025

@author: HP
"""

import cv2
import numpy as np
import os
import sys
import threading
from pynput import keyboard

# Dossier de sauvegarde des scans
SAVE_FOLDER = "scans"
os.makedirs(SAVE_FOLDER, exist_ok=True)

# Détection automatique de la caméra
def detect_camera():
    for i in range(5):  # Tester plusieurs indices
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)  # Utiliser DSHOW pour réduire la latence
        if cap.isOpened():
            print(f"✅ Caméra détectée sur l’index {i}")
            return cap
    print("❌ Aucune caméra détectée.")
    return None

# Ajuster les propriétés de la caméra
def set_camera_properties(cap):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3072)  # Résolution large
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1728)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)  # Luminosité
    cap.set(cv2.CAP_PROP_CONTRAST, 0.5)    # Contraste
    cap.set(cv2.CAP_PROP_SATURATION, 0.5)  # Saturation

# Traitement d’image (mise au propre)
def process_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Niveaux de gris
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # Réduction du bruit
    sharpened = cv2.addWeighted(gray, 1.5, blurred, -0.5, 0)  # Amélioration de la netteté
    edged = cv2.Canny(sharpened, 50, 150)  # Détection des contours
    return edged

# Capture et enregistrement
def capture_and_process(cap):
    ret, frame = cap.read()
    if ret:
        #processed_image = process_image(frame)
        filename = os.path.join(SAVE_FOLDER, f"scan_{cv2.getTickCount()}.jpg")
        cv2.imwrite(filename, frame)
        print(f"✅ Image enregistrée : {filename}")

# Gestion de la capture à la pression d'une touche
def on_press(key, cap):
    if key == keyboard.Key.space:  # Modifier si la pédale envoie une autre touche
        print("📸 Capture en cours...")
        capture_and_process(cap)

# Fonction de prévisualisation
def preview_camera(cap):
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Preview', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    sys.exit()
    

# Détection de la caméra
cap = detect_camera()
if cap is None:
    sys.exit()
 
# Ajuster les propriétés de la caméra
set_camera_properties(cap)

# Lancer la prévisualisation dans un thread séparé
preview_thread = threading.Thread(target=preview_camera, args=(cap,))
preview_thread.daemon = True
preview_thread.start()

# Lancement de l'écouteur de touche
print("🚀 Prêt ! Appuie sur la pédale (ou espace) pour capturer un scan.")
listener = keyboard.Listener(on_press=lambda key: on_press(key, cap))
listener.start()
listener.join()
  