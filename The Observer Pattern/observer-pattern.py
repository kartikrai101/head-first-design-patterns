from subject import WeatherStation
from displays import CurrentConditionsDisplay


# main function for demo
def main():
    weatherStation = WeatherStation()
    currentConditionDisplay = CurrentConditionsDisplay()

    currentConditionDisplay.display()

    # let's make the currentConditionDisplay as an observer to our subject
    weatherStation.register_observer(currentConditionDisplay)
    weatherStation.measurements_changed(32.3, 2.45, 63)
    currentConditionDisplay.display()


if __name__ == "__main__":
    main()