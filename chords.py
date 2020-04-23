import numpy as np 
#Carrega os dados
chords = np.genfromtxt('data.csv',delimiter=';',dtype='str',invalid_raise = False,usecols=np.arange(0,51))



labelbase =         chords[:,chords.shape[1]-3]
labelVariation1 =   chords[:,chords.shape[1]-2]
labelVariation2 =   chords[:,chords.shape[1]-1]

chords = chords[:,:-3]
chords = chords[1:,:].astype(float)

nsize = int(chords.shape[0]*.7)
Xtr = chords[:nsize,:]
Xte = chords[nsize:,:]
Ytr = labelbase[:nsize]
Yte = labelbase[nsize:]

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range = (0,1))
scaler.fit(Xtr)
Xtr = scaler.transform(Xtr)
Xte = scaler.transform(Xte)

from sklearn import linear_model

r=linear_model.LogisticRegression()
Ytr=np.ravel(Ytr)
r.fit(Xtr,Ytr)
Yte=np.ravel(Yte)
y_hat=r.predict(Xtr)

print('   Taxa de acerto (treino):', np.mean(y_hat==Ytr))
y_hat=r.predict(Xte)
print('   Taxa de acerto (teste):', np.mean(y_hat==Yte))