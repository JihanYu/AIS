"""구구단(2~9단)을 계산해서 출력하는 간단한 프로그램."""


def print_gugudan(start: int = 2, end: int = 9) -> None:
    for dan in range(start, end + 1):
        print(f"=== {dan}단 ===")
        for i in range(1, 10):
            print(f"{dan} x {i} = {dan * i}")
        print()


if __name__ == "__main__":
    print_gugudan()
