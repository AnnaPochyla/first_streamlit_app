
import pandas as pd
import streamlit
url='https://drive.google.com/file/d/1saiaP0TbYwiy0nap5aZrbuZL3_slWeu3/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)

#df=pd.read_csv('https://drive.google.com/file/d/1saiaP0TbYwiy0nap5aZrbuZL3_slWeu3/view?usp=sharing')
streamlit.text('test')
streamlit.text(df.size)
streamlit.dataframe(df)
