from waduh.utils import get_time
from waduh.math import Arithmetic, triangle

if __name__ == "__main__":
    result = triangle(10, 5, None, type="area")
    arithmetic = Arithmetic(method="add")
    print(f"Result: {result}")
    print(get_time("hour"))
    print(arithmetic.calculate(5, 6))
