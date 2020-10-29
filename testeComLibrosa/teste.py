import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

y, sr = librosa.load("Amaj_edited2.wav")
librosa.feature.chroma_stft(y=y, sr=sr)

S = np.abs(librosa.stft(y))
chroma = librosa.feature.chroma_stft(S=S, sr=sr)
print(chroma.shape)

for i in range(0,chroma.shape[0]):
    print(chroma[i])



plt.figure(figsize=(10, 4))
librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.title('Chromagram')
plt.tight_layout()
plt.show()