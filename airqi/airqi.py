# AIRQI - UK Air Quality Monitoring & Analytics

print('''
====================================
          WELCOME TO AIRQI
   UK Air Quality Monitoring System
====================================
      
Your air quality data, made simple!
''')

# Storing UK capital cities and their AQI values

air_quality_data = {
    "London": 6.5,
    "Cardiff": 5.3,
    "Edinburgh": 4.6,
    "Belfast": 5.0
}  




# Displaying the stored air quality data

# print("\n========== AIR QUALITY DATA ==========")

# print(f"{'CITY':<15} {'AQI':>10}")
# print("-" * 27)

# for city, aqi in air_quality_data.items():
#     print(f"{city:<15} {aqi:>10.1f}")

# print("=" * 27) 





# Displaying the air quality data

print("\n========== AIR QUALITY DATA ==========")

print("CITY".ljust(15), "AQI".rjust(10))

print("-" * 27)

for city, aqi in air_quality_data.items():
    print(city.ljust(15), str(aqi).rjust(10))

print("=" * 27)
