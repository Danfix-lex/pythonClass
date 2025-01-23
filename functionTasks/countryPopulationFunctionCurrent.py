def get_country_updated_statistics():
    countries = {
        "USA": {"California": {"Los Angeles": 4000000, "San Francisco": 870000}},
        "Canada": {"Ontario": {"Toronto": 2930000, "Ottawa": 994837}}
    }
    if userCountry in countries:
        return "Country already exists"

    countries[userCountry] = {}
    countries[userCountry][userState] = {}
    countries[userCountry][userState][userFirstCity] = userFirstCityPopulation
    countries[userCountry][userState][userSecondCity] = userSecondCityPopulation
    return countries
iiiiiiiiii
userCountry = input("Please enter country: ")
userState = input("Please enter state: ")
userFirstCity = input("Please enter first City: ")
userFirstCityPopulation = int(input("Please enter first City population: "))
userSecondCity = input("Please enter second City: ")
userSecondCityPopulation = int(input("Please enter second City population: "))

updated_data = get_country_updated_statistics()
print("Country has been updated successfully")
print("Kindly enter the details of the country you want to check the city's information")

def get_country_population(countries_dict):
    if userCountry not in countries_dict:
        return "Country not found"
    countryData = countries_dict[userCountry]
    if userState not in countryData:
        return "State not found"
    return countryData[userState]

userCountry = input("Please enter country: ")
userState = input("Please enter state: ")

result = get_country_population(updated_data)
print(result)