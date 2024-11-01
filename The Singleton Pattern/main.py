from threading import Lock


class Singleton:
    _instance = None
    _lock = Lock()  # to make the instance creation part thread safe

    # overriding the new operator
    def __new__(cls, *args, **kwargs):
        raise Exception("Use get_instance() method to access the Singleton instance")

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                # Create a new instance by bypassing the __new__ method.
                cls._instance = super().__new__(cls)
                cls.__init_instance()
        return cls._instance

    @classmethod
    def __init_instance(cls):
        cls._instance.data = {}

    def add_item(self, key: str, value: int):
        Singleton._instance.data[key] = value

    def remove_item(self, key: str):
        del(Singleton._instance.data[key])

    def display_items(self):
        for key, value in Singleton._instance.data.items():
            print(f'{key}: {value}')


def main():
    # create an instance of the singleton class
    instance1 = Singleton.get_instance()
    # add some items
    instance1.add_item("Banana", 10)
    instance1.add_item("Apple", 30)

    # create another instance
    instance2 = Singleton.get_instance()
    # remove some items
    instance2.remove_item("Apple")

    instance1.display_items()


if __name__ == "__main__":
    main()