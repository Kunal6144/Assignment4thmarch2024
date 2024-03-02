airport_data = {}

def enter_new_airport():
    icao_code = input("Enter the ICAO code of the airport: ").strip().upper()
    airport_name = input("Enter the name of the airport: ").strip()
    airport_data[icao_code] = airport_name
    print("Airport data stored successfully.")

def fetch_airport_info():
    icao_code = input("Enter the ICAO code of the airport: ").strip().upper()
    if icao_code in airport_data:
        print(f"The name of the airport with ICAO code {icao_code} is: {airport_data[icao_code]}")
    else:
        print("Airport data not found.")

def main():
    while True:
        print("\nOptions:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            enter_new_airport()
        elif choice == "2":
            fetch_airport_info()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
