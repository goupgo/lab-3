def main():
    user_input = input("Enter a string: ")

    try:
        decimal_value = int(user_input, 16)
        print(f"The base-10 value is: {decimal_value}")
    except ValueError:
        print("Error: Not a valid hexadecimal string.")

if __name__ == "__main__":
    main()
