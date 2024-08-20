def even_odd():
    nums = input("Enter a list of numbers: ")

    num_list= [int(num) for num in nums.split()]

    even = 0
    odd = 0
    for num in num_list:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print(f"Number of even numbers: {even}") 
    print(f"Number of odd numbers: {odd}")

even_odd()    
          