
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
import numpy as np
import math
from matplotlib import pyplot as plt
import os

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
    from sklearn.preprocessing import MinMaxScaler

    for wav in wavs:

        s_rate, signal = wavfile.read(wav)
        labelsToSplit = directories[len(labels)].replace("records\\","")
        splitedlabels = labelsToSplit.split("-")
        

        label = [lastSignal, lastSignal + len(signal), splitedlabels[0],splitedlabels[1],splitedlabels[2]]
        labels.append(label)

        lastSignal += len(signal) + 1
        
        
        # s_rate é a taxa de amostragem: 44100 Hz
        # signal é o vetor com o sinal de audio (cada 44100 valores representa 1 segundo de audio)
        # 2646000 valores para cada minuto de musica
        
        i = 0
        while i + 10000 <= (len(signal)):

            signalSample = signal[i:i+8000]
            i = i + 10000
            FFT = abs(scipy.fft(signalSample))
            freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))

            FFT = FFT[range(0,850)]
            freqs = freqs[range(0,850)]

            '''
            plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)])
            plt.xlabel("Frequency (Hz) " + wav)
            plt.ylabel("Amplitude")
            plt.show()
            '''

            valores = np.array([freqs[range(len(FFT)//2)],FFT[range(len(FFT)//2)]])

            #valores na posicao 0 (valores[:,0]) possui as frequencias
            #valores na posicao 1 (valores[:,1]) possui as amplitudes
            
            #print(len(freqs[range(len(FFT)//2)]))

            freqsNew = np.zeros((48, 2))
            freqsNew[0,0] = 55 + (55* (((220/110) ** (1/12)) -1))/2           #freqsNew in position 0 haves frequencies
            freqsNew[0,1] = 0                                                 #freqsNew in position 1 haves max amplitude found in interval between freqsNew[i,0] and freqsNew[i+1,0] 
                                                                                                        
            for j in range(1,48):                                                                           #Percorre 48 frequencias escaladas (na nota correta)
                freqsNew[j,0] = freqsNew[j-1,0] + freqsNew[j-1,0] * (((220/110) ** (1/12)) -1)              #Calcula a frequenca correta
                for k in range(len(freqs[range(len(FFT)//2)])):                                             #Percorre todos os 
                    #print("valores[0,",j,"] = ",valores[0,j],"freqsNew[",j,"0] = ",freqsNew[j,0])
                    if (valores[0,k] > freqsNew[j,0]):
                        break
                    if (valores[0,k] <= freqsNew[j,0]) & (valores[0,k] >= freqsNew[j-1,0]):
                        if (freqsNew[j,1] < valores[1,j]):
                            freqsNew[j,1] = valores[1,j]
                            
            dataSet.append([freqsNew,label])            
    return dataSet




def writeCSV(dataSet,nomeArquivo):
    linha = ""
    frequenciesT = []
    for data in dataSet:
        #print(np.transpose(data[0])[1])
        frequenciesT.append(np.union1d(np.transpose(data[0])[1],data[1]))
        

    f=open(nomeArquivo,'w')
    line = "A;Asus;B;C;Csus;D;Dsus;E;F;Fsus;G;Gsus;A;Asus;B;C;Csus;D;Dsus;E;F;Fsus;G;Gsus;A;Asus;B;C;Csus;D;Dsus;E;F;Fsus;G;Gsus;A;Asus;B;C;Csus;D;Dsus;E;F;Fsus;G;Gsus;baseNote;variation1;variation2"
    f.write(line+'\n')
    for frequency in frequenciesT:
        line = ""
        for n in frequency:
            line += n + ";"
        f.write(line+'\n')
    f.close()


directories = [os.path.join("records", name) for name in os.listdir("records")]
wavs = []
browseFiles(directories,wavs)
dataSet = extractFeatures(wavs)




writeCSV(dataSet,'data.csv')



        

