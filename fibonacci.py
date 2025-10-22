#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_input():
    N = 0
    while N <= 0:
        try:  
            num = input("Enter the number of fibonacci terms you want:")
            N = int(num)

            if N <= 0:
                print("print enter a positive interger")
            else: 
                return N
        except ValueError:
            printf("Invalid input. Please enter a whole number [integer]");
            N = 0 # wila loop continus

 def generate_fibonacci(N):
     a = 0
     b = 1
     sequence_list = []

      for i in range(N):
          sequence_list.append(a)
          temp = a + b
          a = b
          b = temp
      return sequence_list

def print_sequence(N, sequence):
    print(f"\n--- Fibonaci Sequence for {N} Terms ---")
    print(*sequence_list)
    print("")

def main():
    num = input()
    fib_list = generate_fibonacci(num)
    print_sequence_list(num, fib_list)
# a checker
if __name__ == "__main__":
  #closer
    main()
