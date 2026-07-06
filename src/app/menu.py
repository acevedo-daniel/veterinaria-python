from src.shared.format import show_title
from src.shared.validation import read_option


MENU_OPTIONS = [
    "Register owner",
    "Register pet",
    "Show owners",
    "Show pets",
    "Search pet",
    "Schedule appointment",
    "Show appointments",
    "Attend appointment",
    "Cancel appointment",
    "Show consultations",
    "Show statistics",
]


def show_menu(title: str, options: list[str]) -> None:
    show_title(title)

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    print("0. Exit")


def run_menu() -> None:
    valid_options = [str(number) for number in range(len(MENU_OPTIONS) + 1)]

    while True:
        show_menu("Veterinary Clinic", MENU_OPTIONS)
        option = read_option("Select an option: ", valid_options)

        if option == "0":
            print("Program finished successfully.")
            break

        print("This feature has not been implemented yet.")
