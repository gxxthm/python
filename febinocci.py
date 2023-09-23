def fibonacci(limit):
    
    first, second = 0, 1

    
    if limit <= 0:
        print("Please enter a positive limit.")
    else:
        print("Fibonacci Series up to limit", limit, ":")
        print(first, end=", ")
        
        while second <= limit:
            print(second, end=", ")
            next1 = first + second
            
           
            first, second = second, next1


limit = int(input("Enter the limit for the Fibonacci series: "))

fibonacci(limit)
