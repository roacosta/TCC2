import numpy as np 
#Carrega os dados
chords = np.genfromtxt('datatest.csv',delimiter=';',dtype='str',invalid_raise = False,usecols=np.arange(0,51))

#>>> from sklearn import preprocessing
#>>> le = preprocessing.LabelEncoder()
#>>> le.fit([1, 2, 2, 6])
#LabelEncoder()
#>>> le.classes_
#array([1, 2, 6])
#>>> le.transform([1, 1, 2, 6])
#array([0, 0, 1, 2]...)
#>>> le.inverse_transform([0, 0, 1, 2])
#array([1, 1, 2, 6])
from sklearn import preprocessing
from sklearn.utils import shuffle
le = preprocessing.LabelEncoder()
le.fit(chords[:,chords.shape[1]-3])
chords[1:,chords.shape[1]-3] = le.transform(chords[1:,chords.shape[1]-3])
chords = shuffle(chords[1:,2:-2].astype(float))

#import seaborn as sns
#corr = wines.corr()
#sns.heatmap(corr, 
#            xticklabels=corr.columns.values,
#            yticklabels=corr.columns.values)
#sns.plt.show()

#A A B C C D D E F F G G
#0 1 2 3 4 5 6 7 8 9 1011 
'''chords[:,0] += chords[:,12] + chords[:,24] + chords[:,36]
chords[:,1] += chords[:,13] + chords[:,25] + chords[:,37]
chords[:,2] += chords[:,14] + chords[:,26] + chords[:,38]
chords[:,3] += chords[:,15] + chords[:,27] + chords[:,39]
chords[:,4] += chords[:,16] + chords[:,28] + chords[:,40]
chords[:,5] += chords[:,17] + chords[:,29] + chords[:,41]
chords[:,6] += chords[:,18] + chords[:,30] + chords[:,42]
chords[:,7] += chords[:,19] + chords[:,31] + chords[:,43]
chords[:,8] += chords[:,20] + chords[:,32] + chords[:,44]
chords[:,9] += chords[:,21] + chords[:,33] + chords[:,45]
chords[:,10] += chords[:,22] + chords[:,34] + chords[:,46]
chords[:,11] += chords[:,23] + chords[:,35]
'''



labelbase =         chords[:,chords.shape[1]-1]
labelVariation1 =   chords[:,chords.shape[1]-2]
labelVariation2 =   chords[:,chords.shape[1]-1]

nsize = int(chords.shape[0]*.7)
Xtr = chords[:nsize,:]
Xte = chords[nsize:,:]
Ytr = labelbase[:nsize]
Yte = labelbase[nsize:]


from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing

scaler = MinMaxScaler(feature_range = (-3,1.5))
scaler.fit(Xtr)
Xtr = scaler.transform(Xtr)
Xte = scaler.transform(Xte)

#Xtr = preprocessing.minmax_scale(Xtr.T,feature_range = (-3,1.5)).T
#Xte = preprocessing.minmax_scale(Xte.T,feature_range = (-3,1.5)).T

from sklearn import linear_model

r=linear_model.LogisticRegression()
Ytr=np.ravel(Ytr)
r.fit(Xtr,Ytr)
Yte=np.ravel(Yte)
y_hat=r.predict(Xtr)

print('   Taxa de acerto (treino):', np.mean(y_hat==Ytr))
y_hat=r.predict(Xte)
print('   Taxa de acerto (teste):', np.mean(y_hat==Yte))