def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonacci(n))
