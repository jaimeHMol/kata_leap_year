from typing import Optional


def is_leap(year: Optional[int] = None) -> bool:

    # Check inputs
    if not year:
        year = int(input("Please enter a year number to determine if it is a leap year: "))
    if type(year) is not int or year <= 0:
        raise ValueError("Please enter a valid integer number greater than 0.")

    result = False
    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        result = True
    print(f"The year {year} is leap? {result}")
    return result

if __name__ == "__main__":
    is_leap()