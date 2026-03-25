import random
import string


def generate_password(length):
    # Characters to use in the password
    letters = string.ascii_letters      # a-z and A-Z
    digits = string.digits              # 0-9
    symbols = string.punctuation        # special characters
    all_characters = letters + digits + symbols

    # Pick random characters and join them into one string
    password = "".join(random.choice(all_characters) for _ in range(length))
    return password


def main():
    print("=== Simple Password Generator ===")

    # Ask user for password length
    length_input = input("Enter password length: ")

    # Basic input validation
    if not length_input.isdigit():
        print("Please enter a valid number.")
        return

    length = int(length_input)

    if length <= 0:
        print("Length must be greater than 0.")
        return

    # Generate and display password
    password = generate_password(length)
    print("Generated Password:", password)


if __name__ == "__main__":
    main()
