import time
import numpy as np
import math

def function0(n):
  n += 1
  function0.name = 'O(1)'

def function1(n):
  if n == 0:
    return 0 
  else:
    n = math.floor(n/2)
  function1.name = 'O(logn)'

def function2(n):
  k = 0
  while (k < n):
  	k+=1
  function2.name = 'O(n)'

def function3(n):
  k = i = 0 
  j = 1 
  while (i < n):
  	i+=1
  	while (j < n):
  	  j= j*2
  	  k+=1
  function3.name = 'o(nlogn)'

def function4(n):
  k = i = j = 0
  while (i < n):
    i += 1
    while (j < n):
      j+=1
      k+=1
  function4.name = 'o(n^2)'

def function5(n):
  function5.name = 'o(2^n)'
  if n == 0:
    return 0 
  elif n == 1:
    return 1 
  return function5(n-1) + function5(n-2)

def function6(n):
  function6.name = 'o(n!)'
  if n == 0:
    return 0 
  i = 0
  while(i<n):
    function6(n-1)
    i+=1

def run_function(function, n, ratio):
  start_time = round(time.time() * 1000)
  function(int(n)/int(ratio))
  end_time = round(time.time() * 1000)
  time_used = f"total time used for {function.name} with n={n}: {(end_time-start_time)*ratio} ms"
  print(time_used)



def run_functions():
  n = input("enter n: ")
  run_function(function0, n, 1)
  run_function(function1, n, 1)
  run_function(function2, n, 1)
  run_function(function3, n, 1)
  run_function(function4, n, 1)
  run_function(function5, n, 40000)
  run_function(function6, n, 100000)


run_functions()