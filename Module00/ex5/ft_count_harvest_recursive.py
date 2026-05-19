def ft_count_harvest_recursive() -> None:
    def helper(days) -> None:
        if days > 1:
            helper(days - 1)
        print(f"Day {days}")
    days: int = int(input("Days until harvest: "))
    helper(days)
    print("Harvest time!")
