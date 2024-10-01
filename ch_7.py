# Dictionary to store the airport data
airport_data = {}


def add_airport():
    # Function to add a new airport
    icao_code = input("Enter the ICAO code of the airport: ").upper()
    airport_name = input("Enter the name of the airport: ")

    if icao_code in airport_data:
        print(f"Airport with ICAO code {icao_code} already exists.")
    else:
        airport_data[icao_code] = airport_name
        print(f"Airport {airport_name} added with ICAO code {icao_code}.")


def fetch_airport():
    # Function to fetch an existing airport
    icao_code = input("Enter the ICAO code to fetch airport information: ").upper()

    if icao_code in airport_data:
        print(f"The name of the airport with ICAO code {icao_code} is: {airport_data[icao_code]}")
    else:
        print(f"No airport found with ICAO code {icao_code}.")


def main():
    while True:
        print("\n--- Airport Data Management ---")
        print("1. Enter a new airport")
        print("2. Fetch an existing airport")
        print("3. Quit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            add_airport()
        elif choice == '2':
            fetch_airport()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Run the main function
if __name__ == "__main__":
    main()
