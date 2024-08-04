from waduh.utils import get_time, Person
from waduh.math import aritmethic

if __name__ == "__main__":
    result = aritmethic(10, 5, type="add")
    person1 = Person("Indra", 15)
    print(f"Result: {result}")
    print(get_time("hour"))
    print(person1.name)
