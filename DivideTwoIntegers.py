class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 32-bit integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle edge case for overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)  # XOR to determine if result is negative

        # Work with positive values for simplicity
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            # Double the divisor until it exceeds the dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            # Subtract the largest multiple of divisor
            dividend -= temp
            quotient += multiple

        # Apply the sign
        if negative:
            quotient = -quotient

        # Clamp the result to the 32-bit integer range
        return max(INT_MIN, min(INT_MAX, quotient))
