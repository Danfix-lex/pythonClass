from enum import Enum

class GeoPolitical(Enum):
    NORTH_CENTRAL = ["Benue", "FCT", "Kogi", "Kwara", "Nasarawa", "Niger", "Plateau"]
    NORTH_EAST = ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"]
    NORTH_WEST = ["Kaduna", "Katsina", "Kano", "Kebbi", "Sokoto", "Jigawa", "Zamfara"]
    SOUTH_EAST = ["Abia", "Anambra", "Ebonyi", "Enugu", "Imo"]
    SOUTH_SOUTH = ["Akwa-Ibom", "Bayelsa", "Cross River", "Delta", "Edo", "Rivers"]
    SOUTH_WEST = ["Ekiti", "Lagos", "Osun", "Ondo", "Ogun", "Oyo"]

    @classmethod
    def get_political_zone(cls, state_name: str):
        formatted_state_name = state_name.title()
        for zone in cls:
            if formatted_state_name in zone.value:
                return zone.name.replace("_", " ").title()
        return None

def find_geo_political_zone():
    user_state = input("Please enter your state: ")
    zone = GeoPolitical.get_political_zone(user_state)
    if zone:
        print(f"{user_state.title()} is in {zone} zone")
    else:
        print(f"state '{user_state}' not recognize or not in the list")

if __name__ == "__main__":
    find_geo_political_zone()