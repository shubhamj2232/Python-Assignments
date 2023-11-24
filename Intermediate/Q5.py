def analyze_weather_data(temperature_readings):
    if not temperature_readings:
        return "List is empty."

    average_temperature = sum(temperature_readings) / len(temperature_readings)
    highest_temperature = max(temperature_readings)
    lowest_temperature = min(temperature_readings)

    result = f"Average Temperature: {average_temperature}\nHighest Temperature: {highest_temperature}\nLowest Temperature: {lowest_temperature}"
    return result

temperature_readings = [25, 28, 21, 24, 27]
analysis_result = analyze_weather_data(temperature_readings)
print(analysis_result)
