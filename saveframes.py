import os

import cv2


def extract_frames_from_videos(input_folder):
    # Ottieni tutte le sottocartelle e file nella cartella di input
    entries = os.listdir(input_folder)

    # Trova tutte le lettere presenti basate sui nomi dei file
    letters_present = set(
        entry.split("_")[0].upper() for entry in entries if entry.endswith(".mp4")
    )

    # Percorsi delle cartelle Train e No_train
    train_root_folder = os.path.join(input_folder, "Train")
    no_train_root_folder = os.path.join(input_folder, "No_train")

    # Creare le cartelle Train e No_train, se non esistono
    os.makedirs(train_root_folder, exist_ok=True)
    os.makedirs(no_train_root_folder, exist_ok=True)

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

        # Creare le cartelle per la lettera dentro Train e No_train, se non esistono
        train_folder = os.path.join(train_root_folder, letter)
        no_train_folder = os.path.join(no_train_root_folder, letter)
        os.makedirs(train_folder, exist_ok=True)
        os.makedirs(no_train_folder, exist_ok=True)

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
                        no_train_folder, f"{letter}{frame_count}.jpg"
                    )
                else:
                    save_path = os.path.join(train_folder, f"{letter}{frame_count}.jpg")

                cv2.imwrite(save_path, frame)

            cap.release()


if __name__ == "__main__":
    alphabet = "asl"
    input_path = f"/home/giuseppe/lm_18/ProjectML_ASLvsBSL/dataset/{alphabet}"
    extract_frames_from_videos(input_path)
