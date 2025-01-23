def get_country_population():
    countries = {
        "USA": {"California": {"Los Angeles": 4000000, "San Francisco": 870000}},
        "Canada": {"Ontario": {"Toronto": 2930000, "Ottawa": 994837}}
    }

    if userCountry not in countries:
        return "Country not found"
    countryData = countries[userCountry]

    if userState not in countryData:
        return "State not found"
    cityData = countryData[userState]
    return cityData

userCountry = input("Please enter country: ")
userState = input("Please enter state: ")

result = get_country_population()
print(result)