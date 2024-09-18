from pizza_store import NYPizzaStore, ChicagoPizzaStore


def main():
    # kartik wants to order a NY Style Cheese Pizza

    # create an instance of NY Pizza Store
    ny_pizza_store = NYPizzaStore()
    # get the pizza order using the order_pizza method on the pizza store instance
    kartik_order = ny_pizza_store.order_pizza('cheese')
    print('Your order of ' + kartik_order.get_name() + ' is ready with the following ingredients:')
    kartik_order.list_ingredients()
    print('\n')

    # Srijan wants to order a Chicago Pepperoni Pizza

    # create an instance of Chicago Pizza Store
    chicago_pizza_store = ChicagoPizzaStore()
    # get the pizza order using the order_pizza method on the pizza store instance
    srijan_order = chicago_pizza_store.order_pizza('pepperoni')
    print('Your order of ' + srijan_order.get_name() + ' is ready with the following ingredients:')
    srijan_order.list_ingredients()


if __name__ == "__main__":
    main()