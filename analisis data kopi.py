# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 12:51:39 2023

@author: ASUS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
plt.style.use('ggplot')
pd.set_option('display.max_columns', None)

dataku = pd.read_csv('df_arabica_clean.csv', header=0, index_col=0 )
dataku['ID'] = dataku.drop('ID', axis=1, inplace=True)
# Menampilkan jumlah baris dan kolom dalam dataframe
print(f'jumlah baris pada data ini adalah {dataku.shape[0]}, jumlah kolom pada data ini adalah {dataku.shape[1]} kolom ')

# Melihat beberapa baris pertama dan terakhir dari dataframe
data_baris_awal = dataku.head()


# Mendapatkan daftar kolom dalam dataframe
data_kolom = pd.DataFrame({'kolom ' : dataku.columns})

# Melihat tipe data untuk setiap fitur
type_data = dataku.dtypes

# Mendapatkan statistik deskriptif dari data kita
data_deskriptif = dataku.describe()

# Mengubah nama kolom menjadi huruf kecil dan tanpa spasi
dataku1 = dataku.copy()
dataku1.columns = dataku1.columns.str.lower()
dataku1.columns = dataku1.columns.str.replace(" ", "_")
dataku1

# Memeriksa duplikat dalam dataframe
print(f'data yang mengandung duplikat {dataku1.duplicated().sum()}, baris duplikat')

# Mengubah kolom 'expiration' menjadi tipe data datetime
dataku1['expiration'] = pd.to_datetime(dataku1['expiration'])


# Mencari nilai yang hilang (missing values)
dataku1.isna().sum()

# Mengisi nilai yang hilang dengan 'N/A'
dataku1 = dataku1.fillna('N/A')
dataku1.isna().sum()


# Mengganti beberapa baris yang tidak berguna: 'ID', 'ICO Number', 'In-Country Partner', 'Certification Address', 'Certification Contact'
# Mengubah semua nama kolom menjadi huruf kecil dan mengganti spasi dengan garis bawah
# Tidak ada duplikat yang ditemukan
# Mengganti nilai yang hilang dengan 'N/A'

# Menganalisis data secara univariat
# Menampilkan distribusi fitur dalam bentuk histogram
#informasi data
dataku.info()



# Mendapatkan nilai-nilai dan jumlah masing-masing negara
country_counts = dataku1['country_of_origin'].value_counts().head(10)

# Mengatur gaya plot
plt.style.use('ggplot')

# Membuat figure dan axes
fig, ax = plt.subplots(figsize=(8, 6))

# Membuat plot batang
country_counts.plot(kind='bar', ax=ax, color='steelblue')

# Memberikan judul dan label sumbu
ax.set_title('Jumlah Asal Negara')
ax.set_xlabel('Negara')
ax.set_ylabel('Jumlah')

# Menampilkan nilai pada setiap batang
for i, v in enumerate(country_counts.values):
    ax.text(i, v, str(v), ha='center')
# Menampilkan plot
plt.tight_layout()
plt.show()


# Menghitung proporsi nilai dalam kolom 'country_of_origin'

# Menghitung jumlah data per negara
negara = dataku1['country_of_origin'].value_counts().head(10)
data_negara = pd.DataFrame({'Negara': negara.index, 'Jumlah': negara.values})

# Menghitung persentase kontribusi negara terhadap total
total = negara.sum()
data_negara['Persentase'] = round((data_negara['Jumlah'] / total) * 100, 2)

# Menampilkan persentase kontribusi negara terhadap total
for index, row in data_negara.iterrows():
    print(f"{row['Negara']} menyumbang {row['Persentase']}% dari total")

# Membuat visualisasi diagram batang
plt.figure(figsize=(10, 6))
plt.bar(data_negara['Negara'], data_negara['Persentase'])
plt.xlabel('Negara')
plt.ylabel('Persentase')
plt.title('Persentase Kontribusi Negara')
plt.xticks(rotation=45)
plt.tight_layout()

# Menampilkan label persentase pada diagram batang
for i, v in enumerate(data_negara['Persentase']):
    plt.text(i, v, str(v) + '%', ha='center', va='bottom')

plt.show()
# Melakukan analisis serupa untuk fitur lainnya seperti 'company', 'variety', dan 'color'

# Menghitung jumlah data per company
company = dataku1['company'].value_counts().head(10)
data_company = pd.DataFrame({'Company': company.index, 'Jumlah': company.values})

# Menghitung persentase kontribusi company terhadap total
total = company.sum()
data_company['Persentase'] = round((data_company['Jumlah'] / total) * 100, 2)

# Menampilkan persentase kontribusi company terhadap total
for index, row in data_company.iterrows():
    print(f"{row['Company']} menyumbang {row['Persentase']}% dari total")

# Membuat visualisasi diagram batang
plt.figure(figsize=(10, 6))
plt.bar(data_company['Company'], data_company['Persentase'])
plt.xlabel('Company')
plt.ylabel('Persentase')
plt.title('Persentase Kontribusi Company')
plt.xticks(rotation=45)
plt.tight_layout()

# Menampilkan label persentase pada diagram batang
for i, v in enumerate(data_company['Persentase']):
    plt.text(i, v, str(v) + '%', ha='center', va='bottom')

plt.show()


# Menghitung jumlah data per variety
variety = dataku1['variety'].value_counts().head(10)
data_variety = pd.DataFrame({'Variety': variety.index, 'Jumlah': variety.values})

# Menghitung persentase kontribusi variety terhadap total
total = variety.sum()
data_variety['Persentase'] = round((data_variety['Jumlah'] / total) * 100, 2)

# Menampilkan persentase kontribusi variety terhadap total
for index, row in data_variety.iterrows():
    print(f"{row['Variety']} menyumbang {row['Persentase']}% dari total")

# Membuat visualisasi diagram batang
plt.figure(figsize=(10, 6))
plt.bar(data_variety['Variety'], data_variety['Persentase'])
plt.xlabel('Variety')
plt.ylabel('Persentase')
plt.title('Persentase Kontribusi Variety')
plt.xticks(rotation=45)
plt.tight_layout()

# Menampilkan label persentase pada diagram batang
for i, v in enumerate(data_variety['Persentase']):
    plt.text(i, v, str(v) + '%', ha='center', va='bottom')

plt.show()

# Menghitung jumlah data per color
color = dataku1['color'].value_counts().head(10)
data_color = pd.DataFrame({'Color': color.index, 'Jumlah': color.values})

# Menghitung persentase kontribusi color terhadap total
total = color.sum()
data_color['Persentase'] = round((data_color['Jumlah'] / total) * 100, 2)

# Menampilkan persentase kontribusi color terhadap total
for index, row in data_color.iterrows():
    print(f"{row['Color']} menyumbang {row['Persentase']}% dari total")

# Membuat visualisasi diagram batang
plt.figure(figsize=(10, 6))
plt.bar(data_color['Color'], data_color['Persentase'])
plt.xlabel('Color')
plt.ylabel('Persentase')
plt.title('Persentase Kontribusi Color')
plt.xticks(rotation=45)
plt.tight_layout()

# Menampilkan label persentase pada diagram batang
for i, v in enumerate(data_color['Persentase']):
    plt.text(i, v, str(v) + '%', ha='center', va='bottom')

plt.show()

# Melakukan analisis bivariat
# Menampilkan scatter plot untuk melihat hubungan antara dua fitur
plt.scatter(dataku1['country_of_origin'], dataku1['flavor'])
plt.xlabel('Negara')
plt.ylabel('Aroma')
plt.title('Hubungan antara Total Cup Points dan Moisture Percentage')
plt.show()



# Menampilkan heatmap korelasi antara semua fitur numerik
plt.figure(figsize=(12, 8))
sns.heatmap(dataku1.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm')


# Menampilkan pairplot untuk beberapa fitur yang dipilih

selected_features = ['total_cup_points', 'aroma', 'flavor', 'aftertaste', 'acidity', 'body']
sns.pairplot(dataku1[selected_features])

# Melakukan perbandingan berdasarkan kelompok menggunakan groupby

dataku1.groupby('country_of_origin')['total_cup_points'].mean().sort_values(ascending=False)

# Mencari negara dengan rata-rata skor total cup points tertinggi dan terendah

# Mencari negara dengan rata-rata skor total cup points tertinggi dan terendah
highest_avg_points = dataku1.groupby('country_of_origin')['total_cup_points'].mean().idxmax()
lowest_avg_points = dataku1.groupby('country_of_origin')['total_cup_points'].mean().idxmin()

# Membuat bar plot untuk membandingkan rata-rata skor total cup points tertinggi dan terendah

avg_points_comparison = dataku1.groupby('country_of_origin')['total_cup_points'].mean().loc[[highest_avg_points, lowest_avg_points]]
ax = avg_points_comparison.plot(kind='bar', title='Perbandingan Rata-rata Skor Total Cup Points', rot=0)
ax.set_xlabel('Negara')
ax.set_ylabel('Rata-rata Skor')
