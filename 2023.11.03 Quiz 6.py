def print_christmas_tree(height):
    for a in range(1, height+1):
        spaces = " " * (height - a)
        stars = "*" * (2*a - 1)
        print(spaces + stars)

height = int(input("크리스마스 트리의 높이를 설정하세요: "))
print_christmas_tree(height)
