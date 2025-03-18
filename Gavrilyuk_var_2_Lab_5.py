import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 1) Загальна інформація про базу даних
print("\nЗагальна інформація про базу даних:")
print(df.info())

# 2) Перші 5 та останні 10 записів
print("\nПерші 5 записів:")
print(df.head())

print("\nОстанні 10 записів:")
print(df.tail(10))

# 3) Вибірка тих, хто не вижив
not_survived_df = df[df['Survived'] == 0]
print("\nКількість пасажирів, що не вижили:", len(not_survived_df))

# 4) Розподіл пасажирів за класами серед тих, хто не вижив
class_counts = not_survived_df['Pclass'].value_counts()
print("\nРозподіл пасажирів за класами:")
print(class_counts)

# 5) Побудова стовпчастої діаграми за віковими групами
age_bins = [0, 12, 18, 35, 60, 100]
age_labels = ['Діти', 'Підлітки', 'Молодь', 'Дорослі', 'Літні люди']
not_survived_df = not_survived_df.copy()  # Создаем копию перед изменениями
not_survived_df.loc[:, 'AgeGroup'] = pd.cut(not_survived_df['Age'], bins=age_bins, labels=age_labels)
age_distribution = not_survived_df['AgeGroup'].value_counts()

plt.figure(figsize=(8,5))
age_distribution.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Кількість не виживших пасажирів за віковими групами')
plt.xlabel('Вікові групи')
plt.ylabel('Кількість пасажирів')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()
