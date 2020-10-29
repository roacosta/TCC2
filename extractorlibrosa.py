
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
import numpy as np
import math
from matplotlib import pyplot as plt
import os
import librosa
import librosa.display
import math

def browseFiles(directories,wavs):

    for directory in directories:
        if directory.lower().endswith(".wav"):
            wavs.append(directory)
        else:
            directory = [os.path.join(directory, name) for name in os.listdir(directory)]
            browseFiles(directory,wavs)

def extractFeatures(wavs) -> list:
    labels = []
    lastSignal = 0
    dataSet = []

    for wav in wavs:

        print(labels)
        
        labelsToSplit = wav.split('\\')
        splitedlabels = labelsToSplit[1].split("-")
        # directories[len(labels)].replace("records\\","")
    
        y, sr = librosa.load(wav)
        #s_rate, signal = wavfile.read(wav)
        label = [lastSignal, lastSignal + len(y), splitedlabels[0],splitedlabels[1],splitedlabels[2]]
        labels.append(label)

        lastSignal += len(y) + 1
        librosa.feature.chroma_stft(y=y, sr=sr)
        S = np.abs(librosa.stft(y))

        # s_rate é a taxa de amostragem: 44100 Hz
        # signal é o vetor com o sinal de audio (cada 44100 valores representa 1 segundo de audio)
        # 2646000 valores para cada minuto de musica
        
        #i = 0
        #while i < amostras:

        #signalSample = signal[i*1024:((i+1)*1024)-1]
        #i += 1
        
        #freqsNew = np.zeros(shape=(amostras,2))
                                            #freqsNew in position 1 haves max amplitude found in interval between freqsNew[i,0] and freqsNew[i+1,0] 
        #y, sr = librosa.load(wav)


        #librosa.feature.chroma_stft(y=y, sr=sr)
        #librosa.feature.chroma_stft(y=signalSample/2, sr=s_rate/2)
        #S = np.abs(librosa.stft(y))
        chroma = librosa.feature.chroma_stft(S=S, sr=sr) 
        #print(chroma.shape)
        #for i in range(0,chroma.shape[0]):
        #    print(chroma[i])

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
        plt.colorbar()
        plt.title(wav)
        plt.tight_layout()
        #plt.show()                                                #Percorre 48 frequencias escaladas (na nota correta)
        name = wav + '.png'
        plt.savefig(name)
        #freqsNew[j,0] = freqsNew[j-1,0] + freqsNew[j-1,0] * (((220/110) ** (1/12)) -1)              #Calcula a frequenca correta
        for k in range(0,chroma.shape[1]):                                             #Percorre todos os 
            #print("valores[0,",j,"] = ",valores[0,j],"freqsNew[",j,"0] = ",freqsNew[j,0])
        #    if (valores[0,k] > freqsNew[j,0]):
        #        break
        #    if (valores[0,k] <= freqsNew[j,0]) & (valores[0,k] >= freqsNew[j-1,0]):
        #        if (freqsNew[j,1] < valores[1,k]):
        #    freqsNew[k,1] = chroma[k]
        #    freqsNew[k,0] = k
            #print(chroma[k])
            dataSet.append([np.transpose(chroma)[k],label[2:]])  
    return dataSet

def extractFeaturesTest(wavs) -> list:
    dataSet = []

    for wav in wavs:
        y, sr = librosa.load(wav)
        librosa.feature.chroma_stft(y=y, sr=sr)    
        S = np.abs(librosa.stft(y))
        chroma = librosa.feature.chroma_stft(S=S, sr=sr)
        for k in range(0,chroma.shape[1]):
            dataSet.append(np.transpose(chroma)[k])  
    return dataSet

def writeCSV(dataSet,nomeArquivo):
    linha = ""
    frequenciesT = []
    for data in dataSet:
        #print(np.transpose(data[0])[1])
        frequenciesT.append([data[0],data[1]])
        

    f=open(nomeArquivo,'w')
    line = "C;C^;D;D^;E;F;F^;G;G^;A;A^;B;baseNote;variation1;variation2;"
    f.write(line+'\n')
    for frequency in frequenciesT:
        line = ""
        #print(type(frequency))
        for n in frequency[0]:
            #print(n)
            line += str(n) + ";"
        for n in frequency[1]:
            #print(n)
            line += n + ";"
        f.write(line+'\n')
    f.close()

def writeCSVTest(dataSet,nomeArquivo):
    linha = ""
    frequenciesT = []
    for data in dataSet:
        #print(np.transpose(data[0])[1])
        frequenciesT.append(data)
        

    f=open(nomeArquivo,'w')
    line = "C;C^;D;D^;E;F;F^;G;G^;A;A^;B;"
    f.write(line+'\n')
    for frequency in frequenciesT:
        line = ""
        #print(type(frequency))
        for n in frequency:
            #print(n)
            line += str(n) + ";"
        f.write(line+'\n')
    f.close()


     
directories = [os.path.join("records", name) for name in os.listdir("records")]
wavs = []
browseFiles(directories,wavs)
dataSet = extractFeatures(wavs)
writeCSV(dataSet,'datalibrosa.csv')



dataSet = extractFeaturesTest(['testMono.wav'])
writeCSVTest(dataSet,'datalibrosatest.csv')


        

