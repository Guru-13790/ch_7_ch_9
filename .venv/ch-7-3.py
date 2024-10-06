def main():
    airport_data = {}

    while True:
        print("\nOptions:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input("Please enter your choice (1, 2, or 3): ")

        if choice == '1':
            # Enter a new airport
            icao_code = input("Enter the ICAO code of the airport: ").strip().upper()
            airport_name = input("Enter the name of the airport: ").strip()

            if icao_code in airport_data:
                print("This ICAO code already exists. Please use a different code.")
            else:
                airport_data[icao_code] = airport_name
                print("Airport '" + airport_name + "' with ICAO code '" + icao_code + "' has been added.")

        elif choice == '2':
            # Fetch airport information
            icao_code = input("Enter the ICAO code of the airport to fetch: ").strip().upper()

            if icao_code in airport_data:
                print("The airport with ICAO code '" + icao_code + "' is '" + airport_data[icao_code] + "'.")
            else:
                print("No airport found with that ICAO code.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
