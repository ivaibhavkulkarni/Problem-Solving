"""def get_index(num_list,number):
    l = len(num_list)
    for i in range(l):
        if num_list[i] == str(number):
            return i  

num_list = input().split()
number = int(input())
print(get_index(num_list,number))"""

"""def get_index_recursive(num_list, number):
    # Base case: if the list is empty, return -1 indicating the number was not found
    if not num_list:
        return -1
    
    # Base case: if the current number equals the target number, return 0
    if num_list[0] == str(number):
        return 0
    
    # Recursive case: check the rest of the list for the number
    # If the number is found in the rest of the list, return its index plus 1
    index = get_index_recursive(num_list[1:], number)
    if index != -1:
        return index + 1
    
    # If the number is not found in the rest of the list, return -1
    return -1

# Test the function
num_list = input("Enter numbers separated by spaces: ").split()
number = int(input("Enter the number to find: "))
index = get_index_recursive(num_list, number)
print("Index of", number, "in the list:", index)"""

"""def is_pa_recursive(string):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()
    
    # Base case: if the string is empty or has only one character, it's a palindrome
    if len(string) <= 1:
        return True
    
    # Recursive case: check if the first and last characters are the same,
    # then recursively check the substring between them
    if string[0] == string[-1]:
        return is_pa_recursive(string[1:-1])
    
    # If the first and last characters are not the same, it's not a palindrome
    return False

# Read the input string from the user
string = input()

# Check if the string is a palindrome using the recursive function
is_true = is_pa_recursive(string)

# Print the result
print(is_true)"""



def get_fibonacci_series(n):
    fibonacci_series = []
    for i in range(n):
        term = fibonacci(i)
        fibonacci_series.append(term)
    return fibonacci_series