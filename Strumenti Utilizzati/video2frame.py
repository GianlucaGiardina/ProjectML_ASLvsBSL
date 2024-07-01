import glob
import os

import cv2


def estrai_frame(video_path, output_path):
    # Apre il video
    video = cv2.VideoCapture(video_path)
    # Contatore per i frame
    frame_count = 0

    # Legge i frame finché ce ne sono
    while True:
        # Legge un frame
        success, frame = video.read()

        # Se il frame non può essere letto, esce dal ciclo
        if not success:
            break

        # Ruota il frame di 90 gradi
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

        # Salva il frame come immagine
        frame_name = f"{output_path[-1]}_{frame_count:04d}.jpg"
        cv2.imwrite(os.path.join(output_path, frame_name), frame)

        # Incrementa il contatore dei frame
        frame_count += 1

    # Chiude il video
    video.release()


# Funzione per estrarre frame da tutti i video nella cartella specificata
def estrai_frame_da_cartella(cartella_video, cartelle_output):
    # Itera attraverso ogni video nella cartella
    for video_path in glob.glob(os.path.join(cartella_video, "*.mp4")):
        # Estrae il prefisso (ASL o BSL) dal nome del video
        prefisso = video_path.split("/")[-1][:3]
        # Estrae la lettera dal nome del video
        lettera = video_path.split("/")[-1][4]
        # Verifica se la cartella per il prefisso esiste, altrimenti la crea
        output_folder = os.path.join(cartelle_output, prefisso, lettera)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        # Estrae i frame dal video e li salva nella cartella di output corrispondente
        estrai_frame(video_path, output_folder)


# Cartella contenente i video da elaborare
cartella_video = "VideoASL&BSL"
# Cartella contenente le cartelle ASL e BSL
cartelle_output = "DatasetImmagini"

# Estrae i frame da tutti i video nella cartella
estrai_frame_da_cartella(cartella_video, cartelle_output)
