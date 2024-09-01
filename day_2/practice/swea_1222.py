# 2d_practice
# 계산기1 (D4)

def main():
    T = 10
    for tc in range(1, T + 1):
        L = int(input())
        formula = list(input())
        numbers = []
        while formula:
            item = formula.pop()
            if item == "+":
                continue
            numbers.append(int(item))

        summ = sum(numbers)
        print(f"#{tc} {summ}")


if __name__ == "__main__":
    import sys
    sys.stdin = open("../inputs/input_1222.txt")
    main()