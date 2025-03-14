' sai kiran reddy '
import numpy as np 
import matplotlib.pyplot as plt

def plot_array(data: np.ndarray):
   
    if data.shape != (2, 10):
        raise ValueError("Input array must have a shape of (2, 10)")

    x_vals = data[0]  # First row (X-axis)
    y_vals = data[1]  # Second row (Y-axis)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='b', label="Random Primes")
    plt.title("Random Consecutive Prime Numbers")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis (Prime Numbers)")
    plt.legend()
    plt.grid(True)
    plt.show()


def is_prime(n):
   
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(limit):
   
    num = 2
    while num < limit:
        if is_prime(num):
            yield num
        num += 1


import random

def main():
    size, xsize = 1000, 10  #size of prime pool and array length
    

    primes = list(prime_generator(size))

    start_index = random.randint(0, len(primes) - xsize)
    selected_primes = primes[start_index:start_index + xsize]


    x_values = np.arange(1, xsize + 1)  # X-axis values: 1 to 10
    y_values = np.array(selected_primes)  # Y-axis values: 10 consecutive primes

    data_array = np.vstack((x_values, y_values))  # Stack as a 2-row array

    # Plot the array
    plot_array(data_array)

if __name__ == "__main__":
    main()
