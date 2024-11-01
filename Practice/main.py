from pizzaStore import NYPizzaStore, ChicagoPizzaStore


# Now we will be going through the Simple Factory Pattern
def main():
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza1 = ny_store.create_pizza("cheese")
    pizza2 = chicago_store.create_pizza("indian")

    pizza1.get_name()
    pizza2.get_name()


if __name__ == "__main__":
    main()