def fizzbuzz(a, b):
    if isinstance(a, list) and isinstance(b, list):
        if (len(a) != 0 and len(b) != 0) or (len(a) != 0 or len(b) != 0):
            combined_length = len(a) + len(b)
        
            if (combined_length % 3 == 0 and combined_length  % 5 == 0):
                return "fizzbuzz"
            elif combined_length  % 3 == 0:
                return "fizz"
            elif combined_length  % 5 == 0:
                return "buzz"
            else:
                return combined_length
        else:
            return "Empty lists"
    else:
        return "Invalid input"

print (fizzbuzz([],[]))
print (fizzbuzz(['c','a','n','d','y'],['s','u','s','a','n']))