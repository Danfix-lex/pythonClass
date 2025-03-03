def get_fahrenheit(celsius):
    return (9 / 5) * celsius + 32

print(f"{'Celsius':>10} {'Fahrenheit':>12}")


def fahrenheit(c):
    if c > 32:
        return c - 32
    else:
        return c


for c in range(0, 100):
    f = fahrenheit(c)
    print(f"{c:>10} {f:>12.1f}")

