#!/usr/bin/env python3
def check_temperature(temp_str) -> int:
    try:
        temperature: int = int(temp_str)
        if 0 <= temperature <= 40:
            return temperature
        elif temperature < 0:
            print(f"{temperature}°C is too cold for plants (min 0°C")
        else:
            print(f"{temperature}°C is too high for plants (max 40°C")
    except (ValueError):
        print("Just numbers are allowed")
    return -1


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    option: int = int(input("If you want to run a test press 1\n"
                            "Else press 2\nOption: "))
    if option == 2:
        temperature: str = input("Write the current temperature: ")
        check_temperature(temperature)
    elif option == 1:
        lista: list[int | str] = [25, "abc", 100, -50]
        for number in lista:
            print((f"\nWrite the current temperature: {number}"))
            check_temperature(number)
        print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
