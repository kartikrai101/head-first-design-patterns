from subject import WeatherStation
from observer import Observer, CurrentDisplayElement


def main():
    observer1 = CurrentDisplayElement()

    weather_station = WeatherStation()
    weather_station.add_observer(observer1)
    observer1.display()
    print("\n")

    weather_station.measurements_changed(34.20, 56.5, 0.45)

    weather_station.remove_observer(observer1)

    weather_station.measurements_changed(43.22, 27.5, 0.38)

    observer1.display()


if __name__ == "__main__":
    main()