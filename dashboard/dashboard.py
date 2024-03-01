import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

#Menyiapkan data day
day = pd.read_csv("https://raw.githubusercontent.com/Nizarrafi/Bike_analysis/main/data/day.csv")
day.head()

#Menyiapkan data hour
hour = pd.read_csv("https://raw.githubusercontent.com/Nizarrafi/Bike_analysis/main/data/hour.csv")
hour.head()

#Mengubah beberapa detail tentang kolom pada day
day.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather',
    'cnt': 'count'
}, inplace=True)

#Mengubah beberapa detail tentang kolom pada hour
hour.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather',
    'cnt': 'count',
    'hr' : 'hour'
}, inplace=True)


# Mengubah angka pada day menjadi keterangan
day['month'] = day['month'].map({
    1: 'Jan', 
    2: 'Feb', 
    3: 'Mar', 
    4: 'Apr', 
    5: 'May', 
    6: 'Jun',
    7: 'Jul', 
    8: 'Aug', 
    9: 'Sep', 
    10: 'Oct', 
    11: 'Nov', 
    12: 'Dec'
})
day['season'] = day['season'].map({
    1: 'Winter',
    2: 'Summer',
    3: 'Fall',
    4: 'Spring'
})
day['weekday'] = day['weekday'].map({
    0: 'Sun', 
    1: 'Mon', 
    2: 'Tue',
    3: 'Wed',
    4: 'Thu',
    5: 'Fri',
    6: 'Sat'
})
day['weather'] = day['weather'].map({
    1: 'clear',
    2: 'cloudy',
    3: 'rain',
    4: 'heavy_rain'
})

# Mengubah angka pada hour menjadi keterangan
hour['month'] = hour['month'].map({
    1: 'Jan', 
    2: 'Feb', 
    3: 'Mar', 
    4: 'Apr', 
    5: 'May', 
    6: 'Jun',
    7: 'Jul', 
    8: 'Aug', 
    9: 'Sep', 
    10: 'Oct', 
    11: 'Nov', 
    12: 'Dec'
})
hour['season'] = hour['season'].map({
    1: 'Winter',
    2: 'Summer',
    3: 'Fall',
    4: 'Spring'
})
hour['weekday'] = hour['weekday'].map({
    0: 'Sun', 
    1: 'Mon', 
    2: 'Tue',
    3: 'Wed',
    4: 'Thu',
    5: 'Fri',
    6: 'Sat'
})
hour['weather'] = hour['weather'].map({
    1: 'clear',
    2: 'cloudy',
    3: 'rain',
    4: 'heavy_rain'
})


#Membuat sidebar
with st.sidebar:
    st.markdown("<h1 style='text-align: center; '>Dicoding Bike</h1>", unsafe_allow_html=True)
    st.image("https://genio.bike/wp-content/uploads/2023/09/genio-M342-kids-bike-sepeda-gunung-anak-24-1170x770.jpg")
    st.markdown("<p style='text-align: center;'>Selamat datang di Dicoding Bike! Kami menyewakan berbagai sepeda dengan kualitas terbaik dan desain yang menarik.</p>", unsafe_allow_html=True)

#Membuat Dashboard
#Judul
st.header('Bike Sharing Dashboard')

# Fungsi untuk visualisasi rata-rata peminjaman per musim
def rent_per_season():
    # Membuat data
    rent_Season=day.groupby('season')['count'].sum().reset_index()

    # Membuat plot
    plt.figure(figsize=(10, 5))

    # Menggunakan seaborn untuk membuat plot batang
    sns.barplot(
        y="count",
        x="season",
        data=rent_Season,
        palette=['#40A2E3', '#F6995C', '#BBE2EC', '#0D9276']
    )

    # Menambahkan judul dan label sumbu
    plt.title("Rata - Rata Penyewaan per Musim", loc="center", fontsize=15)
    plt.ylabel("Rata-Rata Penyewaan")
    plt.xlabel("Musim")

    # Mengatur ukuran label sumbu x
    plt.tick_params(axis='x', labelsize=12)

    # Mengatur format angka di sumbu y agar lebih mudah dibaca
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # Tampilkan plot
    st.pyplot()

# Fungsi untuk visualisasi rata-rata peminjaman per jam
def rent_per_hour():

    rent_hour = hour.groupby('hour')['count'].mean()
    plt.bar( rent_hour.index, rent_hour.values, color='#FBA834')
    plt.title('Rata - Rata Penyewaan per Jam')
    plt.xlabel('Jam')
    plt.ylabel('Rata - Rata Penyewaan')
    plt.xticks(range(0, 24))
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Menampilkan plot di Streamlit
    st.pyplot()


# Memanggil fungsi untuk setiap visualisasi
st.subheader('Rata - Rata Penyewaan per Musim')
rent_per_season()

st.subheader('Rata - Rata Penyewaan per Jam')
rent_per_hour()
