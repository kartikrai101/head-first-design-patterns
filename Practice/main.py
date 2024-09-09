from subject import WeatherStation
from displays import CurrentWeatherDisplay


# here we will demonstrate the functionality of our entire weather station
def main():
    # create a WeatherStation subject
    weather_station = WeatherStation()

    # create a display and check the current weather stats
    current_weather_display = CurrentWeatherDisplay()
    current_weather_display.display()

    # register our current weather display as an observer
    weather_station.add_observer(current_weather_display)

    # update the weather measurements from the weather station
    weather_station.measurements_changed(32.2, 1.25, 37.87)

    # check the current weather display again for the weather stats
    current_weather_display.display()

    # update the weather measurements from the weather station again
    weather_station.measurements_changed(22.0, 1.09, 27.30)

    # check the current weather display again for the weather stats again
    current_weather_display.display()


if __name__ == "__main__":
    main()