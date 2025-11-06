"""Calculator providing basic arithmetic operations."""
import sys


class Calculator:
    """Simple calculator class"""

    @classmethod
    def for_numbers(cls, op1, op2):
        """Creates Calculator instance from values that need conversion to float.
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

def demo(op1, op2):
    """Demonstrate Calculator class usage."""
    calculator = Calculator(op1, op2)
    print("Sum of operands", calculator.sum())
    print("Quotient of operands", calculator.divide())
    return calculator.sum()

if __name__ == "__main__":
    demo(15.2, 3.0)
    sys.exit(0)
