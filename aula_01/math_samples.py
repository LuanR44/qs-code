class MathSamples:

    @staticmethod
    def fibonacci(n):
        if n == 0:
            return 0
        if n <= 2:
            return 1
        return MathSamples.fibonacci(n-1) + MathSamples.fibonacci(n-2)

    @staticmethod
    def double(n):
        return n ** 2

    @staticmethod
    def power(base, exponent):
        return base ** exponent

    @staticmethod
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * MathSamples.factorial(n - 1)
