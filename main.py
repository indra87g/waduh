from waduh.utils import get_time, Person
from waduh.math import aritmethic, triangle

if __name__ == "__main__":
    result = triangle(10, 5, None, type="area")
    person1 = Person("Indra", 15)
    print(f"Result: {result}")
    print(get_time("hour"))
    print(person1.name)
