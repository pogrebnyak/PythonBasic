countries_dict = {'Украина': 'Киев','Россия':'Москва','Германия':'Берлин'}
countries = ['Украина', 'Чехия', 'Польша']

for country in countries:
    if country in countries_dict:
        print(countries_dict[country])