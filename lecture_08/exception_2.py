def set_password(my_password):
    """Allow user to set a password."""
    my_password = my_password.strip()
    if len(my_password) < 8:
        raise Exception("Password must be at least 8 characters long")
    return my_password

def main():
    """Start of program."""
    your_password = input("Enter your NEW password: ")
    try:
        your_password = set_password(your_password)
        print(f"Password successfully set to {your_password}!")
    except Exception as error:
        print(error)

    print("--- End ---")

if __name__ == '__main__':
    main()