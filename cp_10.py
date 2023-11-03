높이 = int(input("크리스마스 트리의 높이를 설정하세요: "))
for i in range(1, 높이 + 1):
    print(" " * (높이 - i) + "*" * (2 * i - 1))
