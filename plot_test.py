from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, r2_score

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


empreendimentos = ['emp 1', 'emp 2', 'emp 3', 'emp 4', 'emp 5']

kacuracia = []
kprecisao = []
krecall = []
kf1_score = []
kr2_score = []

lgacuracia = []
lgprecisao = []
lgrecall = []
lgf1_score = []
lgr2_score = []

dtacuracia = []
dtprecisao = []
dtrecall = []
dtf1_score = []
dtr2_score = []

rfacuracia = []
rfprecisao = []
rfrecall = []
rff1_score = []
rfr2_score = []


emps = [1, 2, 4, 5, 6]

for i in emps:

    benign = pd.read_csv('dataset/{}.benign.csv'.format(i))
    mirai = pd.read_csv('dataset/{}.mirai.udp.csv'.format(i))
    gafgyt = pd.read_csv('dataset/{}.gafgyt.udp.csv'.format(i))

    benign["target"] = 0
    mirai["target"] = 1
    gafgyt["target"] = 1

    data = pd.concat([benign, mirai, gafgyt], axis=0)

    X = data.drop("target",axis=1)
    y = data["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    #KNEIGHBORS

    knn = KNeighborsClassifier()
    knn.fit(X_train_scaled, y_train)
    ky_pred = knn.predict(X_test_scaled)

    kacuracia.append(accuracy_score(y_test, ky_pred))
    kprecisao.append(precision_score(y_test, ky_pred))
    kf1_score.append(f1_score(y_test, ky_pred))
    krecall.append(recall_score(y_test, ky_pred))

    #LOGISTIC REGRESSION

    lg = LogisticRegression()
    lg.fit(X_train_scaled, y_train)
    lgy_pred = lg.predict(X_test_scaled)

    lgacuracia.append(accuracy_score(y_test, lgy_pred))
    lgprecisao.append(precision_score(y_test, lgy_pred))
    lgf1_score.append(f1_score(y_test, lgy_pred))
    lgrecall.append(recall_score(y_test, lgy_pred))

    #DECISION TREE

    dt = DecisionTreeClassifier()
    dt.fit(X_train_scaled, y_train)
    dty_pred = dt.predict(X_test_scaled)

    dtacuracia.append(accuracy_score(y_test, dty_pred))
    dtprecisao.append(precision_score(y_test, dty_pred))
    dtf1_score.append(f1_score(y_test, dty_pred))
    dtrecall.append(recall_score(y_test, dty_pred))

    #RANDOM FOREST

    rf = RandomForestClassifier()
    rf.fit(X_train_scaled, y_train)
    rfy_pred = rf.predict(X_test_scaled)

    rfacuracia.append(accuracy_score(y_test, rfy_pred))
    rfprecisao.append(precision_score(y_test, rfy_pred))
    rff1_score.append(f1_score(y_test, rfy_pred))
    rfrecall.append(recall_score(y_test, rfy_pred))

#knn - métricas e gráficos
    
#knn acurácia
klabelsacc = np.array(empreendimentos)
kvaluesacc = np.array(kacuracia)

kaccdf =  pd.DataFrame({'Empreendimentos':klabelsacc, 'Valores':kvaluesacc})

kaccfig, kaccax = plt.subplots()
kaccax = plt.bar(klabelsacc, kvaluesacc, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("Acurácia")

#knn precisão
klabelspre = np.array(empreendimentos)
kvaluespre = np.array(kprecisao)

kpredf =  pd.DataFrame({'Empreendimentos':klabelspre, 'Valores':kvaluespre})

kprefig, kpreax = plt.subplots()
kpreax = plt.bar(klabelspre, kvaluespre, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("Precisão")

#knn recall
klabelsrec = np.array(empreendimentos)
kvaluesrec = np.array(krecall)

krecdf =  pd.DataFrame({'Empreendimentos':klabelsrec, 'Valores':kvaluesrec})

krecfig, krecax = plt.subplots()
krecax = plt.bar(klabelsrec, kvaluesrec, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("Recall")

#knn f1_score
klabelsf1 = np.array(empreendimentos)
kvaluesf1 = np.array(kf1_score)

kf1df =  pd.DataFrame({'Empreendimentos':klabelsf1, 'Valores':kvaluesf1})

kf1fig, kf1ax = plt.subplots()
kf1ax = plt.bar(klabelsf1, kvaluesf1, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("F1-Score")


#LG - métricas e gráficos    

#lg acurácia
lglabelsacc = np.array(empreendimentos)
lgvaluesacc = np.array(lgacuracia)

lgaccdf =  pd.DataFrame({'Empreendimentos':lglabelsacc, 'Valores':lgvaluesacc})

lgaccfig, lgaccax = plt.subplots()
lgaccax = plt.bar(lglabelsacc, lgvaluesacc, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("Acurácia")

#lg precisão
lglabelspre = np.array(empreendimentos)
lgvaluespre = np.array(lgprecisao)

lgpredf =  pd.DataFrame({'Empreendimentos':lglabelspre, 'Valores':lgvaluespre})

lgprefig, lgpreax = plt.subplots()
lgpreax = plt.bar(lglabelspre, lgvaluespre, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("Precisão")

#lg recall
lglabelsrec = np.array(empreendimentos)
lgvaluesrec = np.array(lgrecall)

lgrecdf =  pd.DataFrame({'Empreendimentos':lglabelsrec, 'Valores':lgvaluesrec})

lgrecfig, lgrecax = plt.subplots()
lgrecax = plt.bar(lglabelsrec, lgvaluesrec, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("Recall")

#lg f1_score
lglabelsf1 = np.array(empreendimentos)
lgvaluesf1 = np.array(lgf1_score)

lgf1df =  pd.DataFrame({'Empreendimentos':lglabelsf1, 'Valores':lgvaluesf1})

lgf1fig, lgf1ax = plt.subplots()
lgf1ax = plt.bar(lglabelsf1, lgvaluesf1, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("F1-Score")


#DT - métricas e gráficos    

#dt acurácia
dtlabelsacc = np.array(empreendimentos)
dtvaluesacc = np.array(dtacuracia)

dtaccdf =  pd.DataFrame({'Empreendimentos':dtlabelsacc, 'Valores':dtvaluesacc})

dtaccfig, dtaccax = plt.subplots()
dtaccax = plt.bar(dtlabelsacc, dtvaluesacc, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("Acurácia")

#dt precisão
dtlabelspre = np.array(empreendimentos)
dtvaluespre = np.array(dtprecisao)

dtpredf =  pd.DataFrame({'Empreendimentos':dtlabelspre, 'Valores':dtvaluespre})

dtprefig, dtpreax = plt.subplots()
dtpreax = plt.bar(dtlabelspre, dtvaluespre, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("Precisão")

#dt recall
dtlabelsrec = np.array(empreendimentos)
dtvaluesrec = np.array(dtrecall)

dtrecdf =  pd.DataFrame({'Empreendimentos':dtlabelsrec, 'Valores':dtvaluesrec})

dtrecfig, dtrecax = plt.subplots()
dtrecax = plt.bar(dtlabelsrec, dtvaluesrec, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("Recall")

#lg f1_score
dtlabelsf1 = np.array(empreendimentos)
dtvaluesf1 = np.array(dtf1_score)

dtf1df =  pd.DataFrame({'Empreendimentos':dtlabelsf1, 'Valores':dtvaluesf1})

dtf1fig, dtf1ax = plt.subplots()
dtf1ax = plt.bar(dtlabelsf1, dtvaluesf1, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("F1-Score")

#RF - métricas e gráficos    

#rf acurácia
rflabelsacc = np.array(empreendimentos)
rfvaluesacc = np.array(rfacuracia)

rfaccdf =  pd.DataFrame({'Empreendimentos':rflabelsacc, 'Valores':rfvaluesacc})

rfaccfig, rfaccax = plt.subplots()
rfaccax = plt.bar(rflabelsacc, rfvaluesacc, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("Acurácia")

#rf precisão
rflabelspre = np.array(empreendimentos)
rfvaluespre = np.array(rfprecisao)

rfpredf =  pd.DataFrame({'Empreendimentos':rflabelspre, 'Valores':rfvaluespre})

rfprefig, rfpreax = plt.subplots()
rfpreax = plt.bar(rflabelspre, rfvaluespre, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("Precisão")

#rf recall
rflabelsrec = np.array(empreendimentos)
rfvaluesrec = np.array(rfrecall)

rfrecdf =  pd.DataFrame({'Empreendimentos':rflabelsrec, 'Valores':rfvaluesrec})

rfrecfig, rfrecax = plt.subplots()
rfrecax = plt.bar(rflabelsrec, rfvaluesrec, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("Recall")

#rf f1_score
rflabelsf1 = np.array(empreendimentos)
rfvaluesf1 = np.array(rff1_score)

rff1df =  pd.DataFrame({'Empreendimentos':rflabelsf1, 'Valores':rfvaluesf1})

rff1fig, rff1ax = plt.subplots()
rff1ax = plt.bar(rflabelsf1, rfvaluesf1, width=0.1)
plt.xlabel("Empreendimentos")
plt.ylabel("F1-Score")

#streamlit

st.title("Relatório de Métricas - Dataset N-BaIot")

#knn
st.info("K-ésimo Vizinho Próximo - Acurácia")

st.write(kaccdf)

st.pyplot(kaccfig)

st.info("K-ésimo Vizinho Próximo - Precisão")

st.write(kpredf)

st.pyplot(kprefig)

st.info("K-ésimo Vizinho Próximo - Recall")

st.write(krecdf)

st.pyplot(krecfig)

st.info("K-ésimo Vizinho Próximo - F1-Score")

st.write(kf1df)

st.pyplot(kf1fig)

#lG

st.info("Logistic Regression - Acurácia")

st.write(lgaccdf)

st.pyplot(lgaccfig)

st.info("Logistic Regression - Precisão")

st.write(lgpredf)

st.pyplot(lgprefig)

st.info("Logistic Regression - Recall")

st.write(lgrecdf)

st.pyplot(lgrecfig)

st.info("Logistic Regression - F1-Score")

st.write(lgf1df)

st.pyplot(lgf1fig)

#DT

st.info("Decision Tree - Acurácia")

st.write(dtaccdf)

st.pyplot(dtaccfig)

st.info("Decision Tree - Precisão")

st.write(dtpredf)

st.pyplot(dtprefig)

st.info("Decision Tree - Recall")

st.write(dtrecdf)

st.pyplot(dtrecfig)

st.info("Decision Tree - F1-Score")

st.write(dtf1df)

st.pyplot(dtf1fig)

#RF

st.info("Random Forest - Acurácia")

st.write(rfaccdf)

st.pyplot(rfaccfig)

st.info("Random Forest - Precisão")

st.write(rfpredf)

st.pyplot(rfprefig)

st.info("Random Forest - Recall")

st.write(rfrecdf)

st.pyplot(rfrecfig)

st.info("Random Forest - F1-Score")

st.write(rff1df)

st.pyplot(rff1fig)
