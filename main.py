import numpy as np
import matplotlib.pyplot as plt

x = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015])
gdp_growth_canada = np.array([5.2, 1.8, 2.9, 1.9, 3.1, 3.2, 2.7, 2.2, 1.0, -2.9, 3.4, 3.1, 1.7, 2.5, 2.9, 0.7])
gdp_growth_austria = np.array([3.8, 0.8, 0.9, 1.1, 2.3, 2.7, 3.7, 3.8, 1.4, -3.8, 1.9, 2.7, 0.7, 0.2, 0.6, 1.1])

plt.plot(x, gdp_growth_canada, label = "Canada", color = "blue")
plt.plot(x, gdp_growth_austria, label = "Austria", color = "green")
plt.title("GDP Growth Rate in % for Canada and Austria (2000-2015)", fontsize = 15)
plt.xlabel('Year', fontsize = 10, color = 'black')
plt.ylabel('GDP Growth Rate in %', fontsize = 10, color = 'black')
plt.legend()
plt.show()

country = input("Enter country names ('Canada' або 'Austria'): ").strip().capitalize()

if country == "Canada":
    data = gdp_growth_canada
elif country == "Austria":
    data = gdp_growth_austria
else:
    print("Err")
    data = None


if data is not None:
    plt.bar(x, data, color = "red")
    plt.title(f'GDP Growth Rate (%) for {country} (2000-2015)', fontsize = 15)
    plt.xlabel('Year', fontsize = 10, color = 'black')
    plt.ylabel('GDP Growth Rate (%)', fontsize = 10, color = 'black')
    plt.show()