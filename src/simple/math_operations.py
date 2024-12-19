from typing import List, Union

class MathOperations:
    @staticmethod
    def sum_list(numbers: List[Union[int, float]]) -> Union[int, float]:
        """Sum all numbers in a list."""
        return sum(numbers)
    
    @staticmethod
    def average(numbers: List[Union[int, float]]) -> float:
        """Calculate the average of numbers in a list."""
        if not numbers:
            raise ValueError("Cannot calculate average of empty list")
        return sum(numbers) / len(numbers)
    
    @staticmethod
    def factorial(n: int) -> int:
        """Calculate factorial of a number."""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n == 0:
            return 1
        return n * MathOperations.factorial(n - 1)