import cv2
import os
def estrai_frame(video_path, letter, output_path):
    # Apre il video
    video = cv2.VideoCapture(video_path)
    # Contatore per i frame
    frame_count = 0

    # Verifica se la cartella di output per la lettera esiste, altrimenti la crea
    output_path_letter = os.path.join(output_path, letter)
    if not os.path.exists(output_path_letter):
        os.makedirs(output_path_letter)

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
        frame_name = f"{letter}{frame_count + 1}.jpg"
        cv2.imwrite(os.path.join(output_path_letter, frame_name), frame)
        
        # Incrementa il contatore dei frame
        frame_count += 1

    # Chiude il video
    video.release()


import os

# Percorso della cartella contenente i video
video_dataset_path = "/home/gian/projectml/ProjectML_ASLvsBSL/videodataset"
# Cartella di output per le immagini
image_dataset_path = "/home/gian/projectml/ProjectML_ASLvsBSL/imagedataset"

# Ciclo su tutte le lettere dell'alfabeto
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    # Costruisci il percorso completo del video per la lettera corrente
    video_input_path = os.path.join(video_dataset_path, f"{letter}.mp4")
    
    # Estrai i frame solo se il file video esiste
    if os.path.exists(video_input_path):
        # Estrai i frame ruotati dal video e salvali nella cartella delle immagini
        estrai_frame(video_input_path, letter, image_dataset_path)
    else:
        print(f"Il video per la lettera {letter} non esiste.")

# Percorso del video di input
video_input = "videoprova.mp4"
# Cartella di output per le immagini
output_folder = "A"

# Estrae i frame ruotati dal video
estrai_frame(video_input, output_folder)