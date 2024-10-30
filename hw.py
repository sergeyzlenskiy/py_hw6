import pandas as pd

# Путь к файлу
file_path = 'web_clients_correct.csv'

# Загрузка данных из файла
df = pd.read_csv(file_path)

# Задание 1: Категоризация по возрасту
df['age_category'] = df['age'].apply(lambda x: 'Старше 25' if x > 25 else 'Младше или равен 25')
print("Задание 1: Категории по возрасту")
print(df['age_category'])

# Задание 2: Фильтрация по условиям (пол - мужской, возраст больше 30)
filtered_df = df[(df['sex'] == 'male') & (df['age'] > 30)]

# Вывод отфильтрованных данных
print("\nЗадание 2: Фильтрация по полу и возрасту")
print(filtered_df[['name', 'device_type', 'browser', 'sex', 'age', 'bill', 'region']])