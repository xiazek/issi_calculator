"""Calculator providing basic arithmetic operations."""
import sys


class Calculator:
    """Simple calculator class"""

    @classmethod
    def for_numbers(cls, op1, op2):
        """Create Calculator instance from values that need conversion to float.
        Additional layer, so that we do not need to worry about types inside the class.

        Args:
            op1: First operand (will be converted to float)
            op2: Second operand (will be converted to float)

        Returns:
            Calculator instance if conversion succeeds, None otherwise
        """
        try:
            float_op1 = float(op1)
            float_op2 = float(op2)
            return cls(float_op1, float_op2)
        except (ValueError, TypeError):
            return None

    def __init__(self, op1: float, op2: float):
        """Initialize calculator with two operands.

        Args:
            op1: First operand for arithmetic operations
            op2: Second operand for arithmetic operations
        """
        self.__op1 = op1
        self.__op2 = op2

    def sum(self) -> float:
        """Calculate the sum of two operands.

        Returns:
            The sum of op1 and op2
        """
        return self.__op1 + self.__op2

    def subtract(self) -> float:
        """Calculate the difference between two operands.

        Returns:
            The result of op1 minus op2
        """
        return self.__op1 - self.__op2

    def multiply(self) -> float:
        """Calculate the product of two operands.

        Returns:
            The product of op1 and op2
        """
        return self.__op1 * self.__op2

    def divide(self) -> float | None:
        """Calculate the quotient of two operands.

        Returns:
            - The result of op1 divided by op2 as a float
            - None for division by zero
        """
        if self.__op2 == 0:
            return None
        # eventually we could be just catching ZeroDivisionError when calling.
        return self.__op1 / self.__op2

def main(argv=None):
    """Demonstrate Calculator class usage."""
    if argv is None:
        argv = sys.argv[1:]
    if len(argv) == 2:
        try:
            p1 = float(argv[0])
            p2 = float(argv[1])
            print(f"Calculations for: {p1} {p2}")
            calculator = Calculator(p1, p2)
            print(f"Sum: {calculator.sum()}")
            print(f"Subtract: {calculator.subtract()}")
            print(f"Multiply: {calculator.multiply()}")
            print(f"Divide: {calculator.divide()}")
            return 0
        except ValueError:
            print("Error: Arguments must be numbers")
            return 1
    else:
        print("Usage: python calculator.py <number1> <number2>")
        print("Example: python calculator.py 2 3")
        return 1


if __name__ == "__main__":
    sys.exit(main())
