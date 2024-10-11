# here we will demonstrate the usage of Coffee and Tea classes from the template class
from using_template_behavior import Coffee, Tea


def main():
    tea = Tea()
    coffee = Coffee()

    tea.prepare()
    print('\n')
    coffee.prepare()


if __name__ == "__main__":
    main()