# AIRQI - UK Air Quality Monitoring & Analytics

# Function to display the welcome screen

def welcome():

    print('''
====================================
       WELCOME TO AIRSCOPE UK
   UK Air Quality Monitoring System
====================================

Your air quality data, made simple!
''')


# Function to display all city data

def display_city_data():

    print("\n========== AIR QUALITY DATA ==========")
    print("CITY".ljust(15), "AQI".rjust(10))
    print("-" * 27)

    for city, aqi in air_quality_data.items():
        print(city.ljust(15), str(aqi).rjust(10))

    print("=" * 27)


# Function to add new city data

def add_city_data():

    city = input("\nEnter city name: ")
    aqi = float(input("Enter AQI value: "))

    air_quality_data.update({city: aqi})

    print(f"\n{city} has been added or updated successfully!")


# Storing UK capital cities and their AQI values

air_quality_data = {
    "London": 6.5,
    "Cardiff": 5.3,
    "Edinburgh": 4.6,
    "Belfast": 5.0
}  

# Calling the welcome function
welcome()


# Displaying the stored air quality data

# print("\n========== AIR QUALITY DATA ==========")

# print(f"{'CITY':<15} {'AQI':>10}")
# print("-" * 27)

# for city, aqi in air_quality_data.items():
#     print(f"{city:<15} {aqi:>10.1f}")

# print("=" * 27) 



# Allows users to enter new city data by adding or updating one or more dictionary entries

# city = input("\nEnter city name: ")
# aqi = float(input("Enter AQI value: "))
# air_quality_data.update({city: aqi})









# Main menu

while True:

    print("\n========== AIRSCOPE UK ==========")
    print("1. Add new city data")
    print("2. Display all city data")
    print("3. Find highest AQI")
    print("4. Find lowest AQI")
    print("5. Sort cities by AQI")
    print("6. Search for a city")
    print("7. Calculate average AQI")
    print("8. Exit")

    choice = input("\nEnter your choice: ")


    # if choice == "1":

    #     city = input("\nEnter city name: ")
    #     aqi = float(input("Enter AQI value: "))

    #     air_quality_data.update({city: aqi})

    #     print(f"\n{city} has been added or updated successfully!")

    if choice == "1": 
        add_city_data()

    elif choice == "8":
        print("\nThank you for using AIRSCOPE UK!")
        break

#     elif choice == "2":
# # Displaying the air quality data
# # Function to display all city data

#         def display_city_data():
#             print("\n========== AIR QUALITY DATA ==========")
#             print("CITY".ljust(15), "AQI".rjust(10))
#             print("-" * 27)
#         for city, aqi in air_quality_data.items():
#             print(city.ljust(15), str(aqi).rjust(10))

#             print("=" * 27)


    elif choice == "2":
        display_city_data()



    # elif choice == "2":
    #     print("\n========== AIR QUALITY DATA ==========")
    #     print("CITY".ljust(15), "AQI".rjust(10))
    #     print("-" * 27)

    #     for city, aqi in air_quality_data.items():
    #         print(city.ljust(15), str(aqi).rjust(10))

    #     print("=" * 27)

    elif choice == "3":
        highest_aqi = max(air_quality_data.values())

        for city, aqi in air_quality_data.items():
            if aqi == highest_aqi:
                print(f"\nHighest AQI: {city} = {aqi}")


    elif choice == "4":

        lowest_aqi = min(air_quality_data.values())

        for city, aqi in air_quality_data.items():
            if aqi == lowest_aqi:
                print(f"\nLowest AQI: {city} = {aqi}")

    elif choice == "5":

        sorted_cities = sorted(air_quality_data, key=air_quality_data.get)

        print("\n========== CITIES SORTED BY AQI ==========")

        for city in sorted_cities:
            aqi = air_quality_data.get(city)
            print(city.ljust(15), str(aqi).rjust(10))

        print("=" * 42)


    elif choice == "6":

        search_city = input("\nEnter the city you want to search: ")

        if search_city in air_quality_data:
            aqi = air_quality_data.get(search_city)
            print(f"\n{search_city} has an AQI of {aqi}")

        else:
            print("\nCity not found!")

    elif choice == "7":

        total_aqi = sum(air_quality_data.values())

        number_of_cities = len(air_quality_data)

        average_aqi = total_aqi / number_of_cities

        print(f"\nAverage AQI: {average_aqi:.2f}")


# # Finding the city with the highest AQI

# highest_aqi = max(air_quality_data.values())

# for city, aqi in air_quality_data.items():
#     if aqi == highest_aqi:
#         print(f"\nHighest AQI: {city} = {aqi}")



# # Calculating the average AQI

# total_aqi = sum(air_quality_data.values())

# number_of_cities = len(air_quality_data)

# average_aqi = total_aqi / number_of_cities

# print(f"\nAverage AQI: {average_aqi}")



# # Sorting cities by AQI in ascending order

# sorted_cities = sorted(air_quality_data, key=air_quality_data.get)

# print("\n========== CITIES SORTED BY AQI ==========")

# for city in sorted_cities:
#     aqi = air_quality_data.get(city)
#     print(city.ljust(15), str(aqi).rjust(10))

# print("=" * 42)

# # Searching for a city's AQI

# search_city = input("\nEnter the city you want to search: ")

# if search_city in air_quality_data:
#     aqi = air_quality_data.get(search_city)
#     print(f"\n{search_city} has an AQI of {aqi}")

# else:
#     print("\nCity not found!")


# # Finding the city with the lowest AQI

# lowest_aqi = min(air_quality_data.values())

# for city, aqi in air_quality_data.items():
#     if aqi == lowest_aqi:
#         print(f"\nLowest AQI: {city} = {aqi}")




