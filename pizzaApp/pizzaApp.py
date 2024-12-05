import math

def get_pizza_details_and_calculate_order(guests, pizza_type):
    pizza_data = {
        "Sapa": {"slices": 4, "price": 2500},
        "Small Money": {"slices": 6, "price": 2900},
        "Big Boys": {"slices": 8, "price": 4000},
        "Odogwu": {"slices": 12, "price": 5200},
    }

    if pizza_type not in pizza_data:
        raise ValueError("Invalid pizza type")

    slices_per_box = pizza_data[pizza_type]["slices"]
    price_per_box = pizza_data[pizza_type]["price"]

    total_slices = guests
    boxes_needed = math.ceil(total_slices / slices_per_box)
    leftover_slices = (boxes_needed * slices_per_box) - total_slices
    total_price = boxes_needed * price_per_box

    return {
        "boxes": boxes_needed,
        "leftover": leftover_slices,
        "price": total_price,
    }

