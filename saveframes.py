import os

import cv2


def extract_frames_from_videos(input_folder):
    # Ottieni tutte le sottocartelle e file nella cartella di input
    entries = os.listdir(input_folder)

    # Trova tutte le lettere presenti basate sui nomi dei file
    letters_present = set(
        entry.split("_")[0].upper() for entry in entries if entry.endswith(".mp4")
    )

    # Scorrere ogni lettera presente
    for letter in sorted(letters_present):
        # Percorsi ai video specifici per la lettera corrente
        video_files = [
            os.path.join(input_folder, f"{letter.lower()}_{i}.mp4") for i in range(1, 4)
        ]

        # Controlla se i file video esistono
        video_files = [file for file in video_files if os.path.exists(file)]

        if not video_files:
            continue

        # Creare la cartella per la lettera, se non esiste
        letter_folder = os.path.join(input_folder, letter)
        os.makedirs(letter_folder, exist_ok=True)

        frame_count = 0

        # Scorrere ogni video
        for i, video_file in enumerate(video_files):
            cap = cv2.VideoCapture(video_file)
            frame_rate = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            frames_to_capture = 40
            frame_interval = int(frame_rate // 2)  # Ogni 0.5 secondi

            for j in range(frames_to_capture):
                frame_number = j * frame_interval
                if frame_number >= total_frames:
                    break
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
                ret, frame = cap.read()
                if not ret:
                    break

                frame_count += 1
                if i == 2:  # Se è il terzo video
                    save_path = os.path.join(
                        letter_folder, letter, f"{letter}{frame_count}.jpg"
                    )
                    os.makedirs(os.path.join(letter_folder, letter), exist_ok=True)
                else:
                    save_path = os.path.join(
                        letter_folder, f"{letter}{frame_count}.jpg"
                    )

                cv2.imwrite(save_path, frame)

            cap.release()


if __name__ == "__main__":
    input_path = "/home/giuseppe/lm_18/ProjectML_ASLvsBSL/ml/bsl"
    extract_frames_from_videos(input_path)
