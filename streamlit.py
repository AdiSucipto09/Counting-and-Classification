import streamlit as st
import pandas as pd

option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Home','Dataframe')
)

if option == 'Home' or option == '':
    st.write("""# Halaman Utama""") 
elif option == 'Dataframe':
    st.write("""## Dataframe""") 

    df = pd.read_csv("D:\Kuliah\Semester 6\Kepstun\RestCount\detected_objects.csv")
    df

    st.write("""## Draw Charts""")  

    Car = df[(df['label']=='car')].count()['label']
    Truck = df[(df['label']=='truck')].count()['label']
    Bus = df[(df['label']=='bus')].count()['label']
    label = df['label'].count()
    chart_data = pd.DataFrame(
        df, columns=['label']
    )

    total = Car + Bus + Truck
    data = {
        'car': [Car],
        'bus' : [Bus],
        'truk' : [Truck],
        'Total Terdeteksi': [total],
    }
    table = pd.DataFrame(data, index=['Jumlah Data'])
    
    chart_data = df['label'].value_counts()
    st.bar_chart(chart_data)

    table
