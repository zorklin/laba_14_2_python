import pandas as pd
import matplotlib.pyplot as plt

file_name = "data.csv"

try:
    data = pd.read_csv(file_name)
except FileNotFoundError:
    print(f"error, file {file_name} not found")
    exit()
except pd.errors.EmptyDataError:
    print("error, file is empty")
    exit()
except pd.errors.ParserError:
    print("error parser")
    exit()

data_ukraine = data[data['Country Name'] == 'Ukraine']
data_usa = data[data['Country Name'] == 'United States']

years = [f"{year} [YR{year}]" for year in range(2000, 2016)]
gdp_ukraine = data_ukraine[years].values.flatten()
gdp_usa = data_usa[years].values.flatten()

plt.figure(figsize = (10, 5))
plt.plot(range(2000, 2016), gdp_ukraine, label = "Ukraine", marker = 'o', color = 'blue')
plt.plot(range(2000, 2016), gdp_usa, label = "United States", marker = 'o', color = 'green')
plt.xlabel('Year')
plt.ylabel('GDP growth (in %)')
plt.title('GDP growth for Ukraine and United States')
plt.legend()
plt.show()

country_input = input("Enter country name (Ukraine or United States): ")
if country_input == 'Ukraine':
    gdp_data = gdp_ukraine
elif country_input == 'United States':
    gdp_data = gdp_usa
else:
    print("error name")
    exit()

plt.figure(figsize = (10, 5))
plt.bar(range(2000, 2016), gdp_data, color = 'orange' if country_input == 'Ukraine' else 'purple')
plt.xlabel('Year')
plt.ylabel('GDP growth (in %)')
plt.title(f'GDP growth for {country_input}')
plt.show()
