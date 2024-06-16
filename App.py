import pandas as pd
import streamlit as st
from scikit-learn.linear_model import LogisticRegression

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

loaded_model=pickle.load(open('Titanic_model.SAV','rb'))
 
prediction=classifer.predict(df)
prediction_proba=classifer.predict_proba(df)

st.write(prediction_proba[0])
st.subheader('predicted Result')
if prediction==0.05:
   st.write("Survived the Titanic")
else:
   st.write("Not Survived the Titanic")
