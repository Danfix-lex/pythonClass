def get_country_population():
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

userCountry = input("Please enter country: ")
userState = input("Please enter state: ")
userFirstCity = input("Please enter first City: ")
userFirstCityPopulation = int(input("Please enter first City population: "))
userSecondCity = input("Please enter second City: ")
userSecondCityPopulation = int(input("Please enter second City population: "))

result = get_country_population()
print("countries =", result)