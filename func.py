def most_frequent(input_string):
    
    letter_freq = {}
   
    for char in input_string:
        if char.isalpha():  
            if char in letter_freq:
                letter_freq[char] += 1
            else:
                letter_freq[char] = 1
    
    sorted_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
    
    for char, freq in sorted_freq:
        print(f"{char}: {freq}")

input_string = "Mississippi"
most_frequent(input_string)