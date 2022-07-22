import time
import math

# constant time: O(1)
def o_constant(n):
    o_constant.name = 'O(1)'
    k = 0
    k += 1

# Logarithmic time: O(logn)
def o_logarithmic(n):
    o_logarithmic.name = 'O(logn)'
    k = 1
    while (k < n):
        k*=2

# Linear time: O(n)
def o_linear(n):
    o_linear.name = 'O(n)'
    k = 0
    while (k < n):
    	k+=1

# Quasi-Linear time: O(nlogn)
def o_quasilinear(n):
    o_quasilinear.name = 'O(nlogn)'
    k = i = 0
    j = 1
    while (i < n):
    	i+=1
    	while (j < n):
            j*=2
            k+=1

# Quadratic time: O(n^2)
def o_quadratic(n):
    o_quadratic.name = 'O(n^2)'
    k = i = j = 0
    while (i < n):
        i += 1
        while (j < n):
            j+=1
            k+=1

# Exponential time: O(2^n)
def o_exponential(n):
    o_exponential.name = 'O(2^n)'
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return o_exponential(n-1) + o_exponential(n-2)

# Factorial time: O(n!)
def o_factorial(n):
    o_factorial.name = 'O(n!)'
    if n == 0:
        return 0
    i = 0
    while(i<n):
        o_factorial(n-1)
        i+=1

# Calculate function runtime for a given input size
def run_function(function, n, ratio=1):
    start_time = time.time() * 1000000
    function(int(n) / int(ratio))
    end_time = time.time() * 1000000

    total_time = round((end_time - start_time) * ratio)
    display_row(function.name, total_time)

# Display chart header
def print_header(n):
    number = "{:_}".format(n)
    print("\n n =", number)
    print("-"*30)

# Display row in chart
def display_row(name, t):
    name = '{:8}'.format(name)
    (time, label) = convert_time(t)
    time = '{:>6}'.format(time)
    row = " %s | %s %s" % (name, time, label)
    print(row)

# Convert microseconds to other time durations
def convert_time(t):
    label = "ms  ."
    time = t

    if t < 1000: # less than 1 millisecond
        time = '{:>6}'.format("<1")
    elif t < (1000 * 1000): # milliseconds
        time = round(t/1000)
    elif t < (1000 * 1000 * 60): # seconds
        time = round(t/1_000_000)
        label = "sec .."
    elif t < (1000 * 1000 * 60 * 60): # minutes
        time = round(t/60_000_000)
        label = "min ..."
    elif t < (1000 * 1000 * 60 * 60 * 24): # hours
        time = round(t/3_600_000_000)
        label = "hr  ...."
    else: # days
        time = round(t/86_400_000_000)
        label = "day ....."

    return (time, label)

# Get input size from user
def get_n():
    print("default n value: 1_000_000")
    n = input("enter n: ")
    if not n:
        n = 1_000_000
    return int(n)

# Run all functions
def run_functions(n):
    run_function(o_constant, n)
    run_function(o_logarithmic, n)
    run_function(o_linear, n)
    run_function(o_quasilinear, n)
    run_function(o_quadratic, n)
    run_function(o_exponential, n, int(n/25)) # run n = 25 then extrapolate
    run_function(o_factorial, n, int(n/10))   # run n = 10 then extrapolate

# main
n = get_n()
print_header(n)
run_functions(n)
