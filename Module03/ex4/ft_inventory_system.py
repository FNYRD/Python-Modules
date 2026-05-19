#!/usr/bin/env python3
def main() -> None:
    inventory: dict = {"Moderate": {
                                    "potion": 5
                                   },
                       "Scarce": {
                                    "armor": 3,
                                    "shield": 2,
                                    "sword": 1,
                                    "helmet": 1
                                }
                       }
    print("=== Inventory System Analysis ===")
    num: int = 0
    types: int = 0
    for category, values in inventory.items():
        for key, value in values.items():
            types += value
            num += 1
    max_key: str = ""
    min_key: str = ""
    max_value: int = 0
    min_value: int = 9223372036854775807
    print(f"Total items in inventory: {types}")
    print(f"Unique item types: {num}")
    print("\n=== Current Inventory ===")
    under_stock: list[str] = []
    for category, values in inventory.items():
        for key, value in values.items():
            if int(value) >= max_value:
                max_value = value
                max_key = key
            if int(value) <= min_value:
                min_value = value
                min_key = key
            if value < 2:
                under_stock.append(key)
            print(f"{key}: {value} units ({(int(value) / types * 100):.1f}%)")
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {max_key} ({max_value} units)")
    print(f"Least abundant: {min_key} ({min_value} unit)")
    inventory.update({"Scarce": {
                            "sword": 1,
                            "shield": 2,
                            "armor": 3,
                            "helmet": 1
                          }})
    print("\n=== Item Categories ===")
    for category, values in inventory.items():
        print(f"{category}: {values}")
    flag: int = 0
    print("\n=== Management Suggestions ===")
    print("Restock needed: ", end="")
    for under in under_stock:
        if flag == 0:
            print(f"{under}", end="")
        elif 0 < flag < len(under_stock) - 1:
            print(f", {under}", end="")
        elif flag == len(under_stock) - 1:
            print(f", {under}")
        flag += 1
    print("\n=== Dictionary Properties Demo ===")
    flag = 0
    showing: dict = {
                     "sword": 1,
                     "potion": 5,
                     "shield": 2,
                     "armor": 3,
                     "helmet": 1
                    }
    print("Dictionary keys: ", end="")
    for key, value in showing.items():
        if flag == 0:
            print(f"{key}", end="")
        elif 0 < flag < len(showing) - 1:
            print(f", {key}", end="")
        elif flag == len(showing) - 1:
            print(f", {key}")
        flag += 1
    flag = 0
    print("Dictionary values: ", end="")
    for key, value in showing.items():
        if flag == 0:
            print(f"{value}", end="")
        elif 0 < flag < len(showing) - 1:
            print(f", {value}", end="")
        elif flag == len(showing) - 1:
            print(f", {value}")
        flag += 1
    if "sword" in showing:
        print("Sample lookup - 'sword' in inventory: True")


if __name__ == "__main__":
    main()
