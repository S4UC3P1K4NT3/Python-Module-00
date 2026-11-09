def ft_count_harvest_recursive(n=-1, i=1) -> None:
    if n == -1:
        n = int(input("Days until harvest: "))
    if i > n:
        print("Harvest time!")
    else:
        print("Day", i)
        i += 1
        ft_count_harvest_recursive(n, i)
