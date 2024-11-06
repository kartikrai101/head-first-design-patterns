from beverage import CaffeineBeverage, Coffee, Tea


def main():
    coffee: CaffeineBeverage = Coffee()
    tea: CaffeineBeverage = Tea()

    coffee.prepare()
    print('\n')
    tea.prepare()


if __name__ == "__main__":
    main()