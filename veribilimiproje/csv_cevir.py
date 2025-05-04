import pandas as pd

# Excel dosyasını oku
df = pd.read_excel('Dry_Bean_Dataset.xlsx')

# CSV formatında kaydet
df.to_csv('Dry_Bean_Dataset.csv', index=False)

print("Excel dosyası başarıyla CSV formatına çevrildi!")
