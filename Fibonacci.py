class Fibonacci:
    def even_sum(self, count):
        a, b = 0, 2
        sum_even = 0
        for _ in range(count):
            sum_even += a
            a, b = b +a
        return sum_even
    

fib = Fibonacci
print(fib.even_sum(100))
