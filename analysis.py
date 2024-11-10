import pandas as pd

file_path = 'path/to/messy_daily_website_visitors.csv'

# Membaca file CSV
data = pd.read_csv(file_path)

# Menampilkan beberapa baris pertama untuk memeriksa struktur data 
print("Data Awal:")
print(data.head())

# Membersihkan data dengan menghapus nilai kosong pada kolom yang relevan
data_cleaned = data.dropna(subset=['Page.Loads', 'Unique.Visits', 'First.Time.Visits', 'Returning.Visits'])

# Menghapus koma pada angka dan mengonversinya menjadi integer
data_cleaned['Page.Loads'] = data_cleaned['Page.Loads'].str.replace(',', '').astype(int)
data_cleaned['Unique.Visits'] = data_cleaned['Unique.Visits'].str.replace(',', '').astype(int)
data_cleaned['First.Time.Visits'] = data_cleaned['First.Time.Visits'].str.replace(',', '').astype(int)
data_cleaned['Returning.Visits'] = data_cleaned['Returning.Visits'].str.replace(',', '').astype(int)

# Menampilkan beberapa baris pertama dari data yang sudah dibersihkan (opsional)
print("\nData Setelah Dibersihkan:")
print(data_cleaned.head())

# 2a. Menghitung total returning visits dan rata-rata unique visits
total_returning_visits = data_cleaned['Returning.Visits'].sum()
average_unique_visits = data_cleaned['Unique.Visits'].mean()

# 2b. Menghitung rata-rata jumlah page loads untuk setiap unique visit
average_page_loads_per_unique_visit = data_cleaned['Page.Loads'].sum() / data_cleaned['Unique.Visits'].sum()

# 2c. Menghitung rata-rata page loads per hari
total_page_loads_per_day = data_cleaned['Page.Loads'].mean()

# Menampilkan hasil
print("\nHasil Analisis:")
print("Total Returning Visits:", total_returning_visits)
print("Rata-rata Unique Visits:", average_unique_visits)
print("Rata-rata Page Loads per Unique Visit:", average_page_loads_per_unique_visit)
print("Rata-rata Page Loads per Hari:", total_page_loads_per_day)
