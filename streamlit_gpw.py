
import pandas as pd
import streamlit
url='https://drive.google.com/file/d/1saiaP0TbYwiy0nap5aZrbuZL3_slWeu3/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
streamlit.title('My Parents New Healthy Diner')
streamlit.text('test')
df_all = pd.read_csv(url,usecols=['Nazwa','Waluta','Kurs otwarcia','Kurs maksymalny','Kurs minimalny','Kurs zamknięcia','Zmiana kursu %','Wartość obrotu (w tys.)','Data'])

#df=pd.read_csv('https://drive.google.com/file/d/1saiaP0TbYwiy0nap5aZrbuZL3_slWeu3/view?usp=sharing')

df=df_all[df_all["Nazwa"]=='11BIT']
streamlit.dataframe(df)
