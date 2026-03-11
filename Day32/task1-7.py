# TASK 1: Loading audio and playing 
import librosa as lb 
 
y,sr=lb.load("D:\\Internship\\Day32\\game_over.wav", sr=None) 
print("Audio duration: ",lb.get_duration(y=y, sr=sr),"seconds") 
print("Sampling Rate:", sr,"Hz") 
 
import sounddevice as sd 
sd.play(y, sr) 
sd.wait() 
 
 
# TASK 2: Display waveform 
import matplotlib.pyplot as plt 
import librosa.display 
 
plt.figure(figsize=(10,4)) 
lb.display.waveshow(y,sr=sr) 
 
plt.title("Waveform") 
plt.xlabel("Time") 
plt.ylabel("Amplitude") 
plt.show() 
 
 
# TASK 3: Spectogram 
import numpy as np 
 
d=lb.amplitude_to_db(np.abs(lb.stft(y)),ref=np.max) 
plt.figure(figsize=(10,4)) 
lb.display.specshow(d,sr=sr,x_axis="time",y_axis="log") 
plt.title("Spectrogram") 
plt.show() 
 
 
# TASK 4: Mel frequency cepstral coefficients 
mfccs=lb.feature.mfcc(y=y,sr=sr,n_mfcc=13) 
 
plt.figure(figsize=(10,4)) 
lb.display.specshow(mfccs,sr=sr,x_axis="time") 
 
plt.title("MFCCs") 
plt.show() 
 
 
# TASK 5: Chroma feature 
chroma=lb.feature.chroma_stft(y=y,sr=sr) 
 
plt.figure(figsize=(10,4)) 
lb.display.specshow(chroma,sr=sr,x_axis="time",y_axis="chroma") 
 
plt.title("Chroma features") 
plt.show() 
 
 
 
# TASK 6: Tempo and beat 
tempo, beats=lb.beat.beat_track(y=y,sr=sr) 
print("Estimated tempo:",tempo,"BPM") 
 
beat_times=lb.frames_to_time(beats,sr=sr) 
 
plt.figure(figsize=(10,4)) 
lb.display.waveshow(y,sr=sr) 
 
plt.vlines(beat_times,ymin=-1,ymax=1,color='r',linestyle='--',label="Beats") 
plt.legend() 
plt.title("Beat tracking") 
 
plt.show() 
 
 
# TASK 7: Zero crossing 
z=lb.feature.zero_crossing_rate(y) 
 
plt.figure(figsize=(10,4)) 
plt.plot(z[0],label="Zero crossing rate") 
 
plt.xlabel("frames") 
plt.ylabel("rate") 
plt.title("zero crossing rate") 
 
plt.legend() 
plt.show() 
