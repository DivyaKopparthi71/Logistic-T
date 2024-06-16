import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression

st.title('Model deployment:Logistic Regression')
st.sidebar.header('User Input Parameters')

def user_input_features():
    Survived=st.sidebar.selectbox('Survived',('1','0'))
    Pclass=st.sidebar.selectbox('Pclass',('1','2','3'))
    Sex = st.sidebar.selectbox('Gender',('female','male'))
    if Sex=='female':
        Sex=1
    else:
        Sex=0

    Age=st.sidebar.number_input('Insert Age')
    Sibsp=st.sidebar.number_input('Insert Sibsp')
    Parch=st.sidebar.number_input('Insert Parch')
    Fare=st.sidebar.number_input('Insert Fare')
    Embarked=st.sidebar.selectbox('Embarked',('S','C','Q'))
    if Embarked=='S':
        Embarked=1
    elif Embarked=='C':
        Embarked=2
    else:
        Embarked=3 
    data={'Survived':Survived,
          'Pclass':Pclass,
          'Sex':Sex,
          'Age':Age,
          'Sibsp':Sibsp,
          'Parch':Parch,
          'Fare':Fare,
          'Embarked':Embarked}
    features=pd.DataFrame(data,index=[0])
    return features

df = user_input_features()
st.subheader('user Input parameters')
st.write(df)


Titanic=pd.read_csv("Titanic_train.csv")
Titanic.drop(["PassengerId","Name","Ticket","Cabin"],inplace=True,axis=1)
Titanic=Titanic.dropna()
X = Titanic.drop("Survived", axis=1)
Y = Titanic["Survived"]
X = pd.get_dummies(X, columns=["Sex","Embarked"], drop_first=True)
df = pd.get_dummies(df, columns=["Sex","Embarked"], drop_first=True)
df = df.reindex(columns=X.columns, fill_value=0)


classifer=LogisticRegression()
classifer.fit(X,Y)
 
prediction=classifer.predict(df)
prediction_proba=classifer.predict_proba(df)

st.write(prediction_proba[0])
st.subheader('predicted Result')
if prediction==0.05:
   st.write("Survived the Titanic")
else:
   st.write("Not Survived the Titanic")