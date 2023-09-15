cache={}
counter=0
def memorize(n):
    
    def inner(num):
        if num not in cache:
            cache[num]= n(num)
        return cache[num]
    return inner  

def count_calls(f):
    def wrapper(*args):
        wrapper.call_count += 1   #this is a wrapper
        return f(*args)
    
    wrapper.call_count = 0
    return wrapper




# def fib(num):
#     if num <= 1:
#         return 1
#     return fib(num-1)+ fib(num-2) #recursiving calling function twice
# print(fib(5))



@count_calls # use wrapper here to count
def fibonacci(num):
    if num <= 1:
        return 1
    if num not in cache:
        cache[num] = fibonacci(num - 1)+ fibonacci(num-2)
        
    return cache[num]



        


print(fibonacci(15))
print(cache)
print(fibonacci.call_count)


