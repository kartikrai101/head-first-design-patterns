from subject import WeatherStation
from displays import CurrentConditionsDisplay


# main function for demo
def main():
    # create instance of WeatherStation (Subject)
    weather_station = WeatherStation()
    # create instance of a DisplayElement (Observer)
    current_condition_display = CurrentConditionsDisplay()

    current_condition_display.display()

    # let's register our display object as an observer to our WeatherStation subject
    weather_station.register_observer(current_condition_display)
    # create an update in the measurements at the weather station
    weather_station.measurements_changed(32.3, 2.45, 63)
    current_condition_display.display()


if __name__ == "__main__":
    main()