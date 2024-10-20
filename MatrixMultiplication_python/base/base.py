import pytest
import random
import json
from memory_profiler import memory_usage

# The matrix multiplication function
def matrix_multiplication(a, b):
    assert len(a) == len(b)
    n = len(a)
    c = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    return c

# Auxiliary function to generate random matrices of size n x n
def generate_random_matrix(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

# Store test results
results = []

# Benchmark test
@pytest.mark.parametrize("size", [100, 200, 500, 700])
def test_matrix_multiplication_benchmark(benchmark, size):
    # Generate two random matrices of size n x n
    a = generate_random_matrix(size)
    b = generate_random_matrix(size)

    # Measure memory and CPU usage before the benchmark
    mem_before = memory_usage()[0]

    # Run the benchmark for matrix multiplication
    result = benchmark.pedantic(
        matrix_multiplication,
        args=(a, b),
        iterations=10,
        rounds=2
    )

    # Measure memory and CPU usage after the benchmark
    mem_after = memory_usage()[0]

    # Calculate the memory and CPU usage difference
    memory_diff = mem_after - mem_before

    # Store the results in the list
    results.append({
        'matrix_size': size,
        'execution_time_mean': benchmark.stats['mean'] * 1000, # Convert to milliseconds
        'memory_usage_mb': memory_diff
    })

    # Save the results to a JSON file if the last size was reached
    if size == 700:
        with open('benchmark_results.json', 'w') as f:
            json.dump(results, f, indent=4)
        print("\n\n Benchmark results saved to 'benchmark_results.json'")
