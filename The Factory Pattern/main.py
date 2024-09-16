from pizzaStore import NYPizzaStore, ChicagoPizzaStore


def main():
    # create Pizza Store instances
    ny_pizza_store = NYPizzaStore()
    chicago_pizza_store = ChicagoPizzaStore()

    # kartik wants to order a NY style veggie pizza
    kartik_order = ny_pizza_store.order_pizza('veggie')
    print('\n')

    # srijan wants to order Chicago style cheese pizza
    srijan_order = chicago_pizza_store.order_pizza('cheese')
    print('\n')

    # display the names of both the pizzas
    print('Kartik Ordered: ' + kartik_order.get_name())
    print('Srijan Ordered: ' + srijan_order.get_name())


if __name__ == "__main__":
    main()