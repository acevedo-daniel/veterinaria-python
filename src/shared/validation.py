def read_integer(message: str) -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid integer.")


def read_option(message: str, options: list[str]) -> str:
    while True:
        option = input(message).strip()

        if option in options:
            return option

        print(f"Please enter a valid option: {', '.join(options)}")
