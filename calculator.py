"""Calculator providing basic arithmetic operations."""


class Calculator:
    """Simple calculator class"""

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
        return self.__op1 / self.__op2
