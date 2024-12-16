from pandas import read_csv, concat, DataFrame

data_frame = read_csv('miasta.csv', sep=',')
nowe_dane = {'Rok': 2010, 'Gdansk': 460, 'Poznan': 555, 'Szczecin': 405}
data_frame = concat([data_frame, DataFrame([nowe_dane])], ignore_index=True)

data_frame.to_csv('miasta_dodane.csv', index=False)

print(data_frame)
