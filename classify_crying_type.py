import numpy as np
# import pandas as pd
import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import normalize
import warnings
warnings.filterwarnings('ignore')
# from sklearn.model_selection import train_test_split
import tensorflow
# from tensorflow.keras.layers import LSTM, Dense
import pickle
import pyaudio
import wave
import streamlit as st
from keras.preprocessing import image

loaded_model = pickle.load(open('test_model.sav', 'rb'))

def create_spectrogram(audio_file, image_file):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

    y, sr = librosa.load(audio_file)
    ms = librosa.feature.melspectrogram(y=y, sr=sr)
    log_ms = librosa.power_to_db(ms, ref=np.max)
    librosa.display.specshow(log_ms, sr=sr)

    fig.savefig(image_file)
    plt.close(fig)

def create_pngs_from_wavs(input_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    dir = os.listdir(input_path)

    for i, file in enumerate(dir):
        input_file = os.path.join(input_path, file)
        output_file = os.path.join(output_path, file.replace('.wav', '.png'))
        create_spectrogram(input_file, output_file)

# result = loaded_model.score(X_test, Y_test)

def record():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 8
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    create_spectrogram("output.wav", "output.png")

# create_pngs_from_wavs("data/test_belly_pain", "data/test_bp_pngs")

# def get_png_files(directory):
    # folders = ["data/test_bp_pngs"]
    # folders = ['belly_pain', 'burping', 'discomfort', 'tired'] 
    # png_files = []

    # for folder_name in folders:
    #     folder_path = os.path.join(directory, folder_name)
    #     if os.path.exists(folder_path):
    #         png_files.extend(glob.glob(os.path.join(folder_path, '*.png')))
    #     else:
    #         print(f"Folder '{folder_name}' does not exist in '{directory}'.")

    # return png_files
def analyze():
    directory_path = '' 
    # png_files_list = get_png_files(directory_path)
    x = image.load_img("output.png", target_size=(224, 224))

    x = image.img_to_array(x)
    x = np.expand_dims(x, axis=0)/255
        # print(x)
    y = loaded_model.predict(x)

    class_labels = ['belly pain','burping','discomfort','hungry','tired']
    results = ""

    m = 0
    l = ''
    if(y[0][3]>0.9999):
        results = class_labels[3]
    elif (y[0][4]>0.0001):
            # for i, label in enumerate(class_labels):
            #     if(y[0][i]>0 and i != 3):
            #         m = y[0][i]
            #         l = label                                               
            # # print(f'{label}: {y[0][i]}')
        results = class_labels[4]
    else:
        results = class_labels[2]
    return results
    # for i in results:
    #     print(i)
    #     print('\n')

recorded = False
print("AAAAAA")
recordBtn, analyzeBtn = st.columns(2)
if recordBtn.button("record", use_container_width=True):
    # recordBtn.markdown("Recording started")
    record()
    # recordBtn.markdown("Recording ended")
    recorded = True
if analyzeBtn.button("analyze",use_container_width=True):
    print("Analyzing")
    out = analyze()
    analyzeBtn.markdown(out)
    print(out)
    print("DONE")
# st.button("Record", on_click = record())
# st.button("Analyze", on_click = analyze())

# if st.checkbox("record"):
#     record()
#     recorded = True

# if st.checkbox("analyze") and recorded:
#     out = analyze()
#     st.write(out);