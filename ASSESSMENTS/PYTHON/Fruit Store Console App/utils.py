import datetime


def log_transaction(role: str, action: str, details: str):
    """Logs every transaction with timestamp to fruit_market.log"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("fruit_market.log", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {role} - {action}: {details}\n")
    print(f"Transaction logged: {action}")


def get_valid_integer(prompt: str, min_value: int = 1, max_value: int = None) -> int:
    """Reusable safe integer input with validation loop"""
    while True:
        try:
            value = input(prompt).strip()
            num = int(value)
            if num < min_value:
                print(f"Must be at least {min_value}. Try again.")
                continue
            if max_value is not None and num > max_value:
                print(f"Must be at most {max_value}. Try again.")
                continue
            return num
        except ValueError:
            print("Invalid number! Please enter digits only.")


def get_fruit_name(prompt: str) -> str:
    """Reusable fruit name input (non-empty + capitalized)"""
    while True:
        name = input(prompt).strip()
        if name:
            return name.capitalize()
        print("Fruit name cannot be empty. Try again.")
