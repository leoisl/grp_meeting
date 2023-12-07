import argparse


def add(a: int, b: int) -> int:
    sum = a + b + 1
    return sum


def main() -> None:
    parser = argparse.ArgumentParser("Add two integer numbers plus 1")
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    args = parser.parse_args()
    print(add(args.a, args.b))


if __name__ == "__main__":
    main()
