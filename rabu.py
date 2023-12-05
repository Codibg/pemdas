import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1
df['Status'] = df['Usia'].apply(lambda x: 'Muda' if x < 30 else 'Tua')

# Pertanyaan 2
df['Gaji Bonus'] = df.apply(lambda row: row['Gaji'] * 1.1 if row['Status'] == 'Tua' else row['Gaji'] * 1.05 , axis=1)

# Pertanyaan 3
print("DataFrame setelah diperbarui:")
print(df)
print("Ringkasan hasil:")
print(df.describe())

# Pertanyaan 4
df['Usia di atas 30'] = df['Usia'].apply(lambda x: True if x > 30 else False)

print("DataFrame setelah penambahan kolom Usia di atas 30:")
print(df)
