import re
red: str = "\033[31m"
green: str = "\033[32m"
defcolor: str = '\033[m'


def celsius_to_fahrenheit(celsius: float) -> float:
    fahrenheit = float((celsius * 9/5) + 32)
    return round(fahrenheit, 2)


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    celsius: float = float((fahrenheit - 32) * 5/9)
    return round(celsius, 2)


def main() -> None:

    pattern = re.compile("^\\d+?\\.?\\d .$")
    while True:
        try:
            temperature: str = input(
                "Enter a temperature and its unit (e.g., \"25 C\" or \"77 F\"): ")
            if pattern.match(temperature):
                temper, unit = temperature.split(" ")
                match unit:
                    case "C":
                        celsius: float = float((temper))
                        print(f"""{green}Temperature in Fahrenheit: \
{celsius_to_fahrenheit(celsius)} F""", end=defcolor+"\n")
                    case "F":
                        fahrenheit: float = float(temper)
                        print(f"""{green}Temperature in Celsius: \
{fahrenheit_to_celsius(fahrenheit)} C""", end=defcolor+"\n")
                    case "q":
                        exit()
                    case _:
                        raise TypeError(
                            "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
            else:
                raise ValueError("Invalid temperature value")
        except ValueError as e:
            print(f"{red}{e}", end=defcolor+"\n")
        except TypeError as e:
            print(f"{red}{e}", end=defcolor+"\n")


if __name__ == "__main__":
    main()
