def rmchar (string,target): #the function accepts the string that needs to be modified and the target which is the number of letters to be removed/ the index of the new starting letter.
  
    string = ([*string]) #splits into list of characters
    new_string = string[target::] #slicing the list. we define the starting point to be the index defined in the second parameter or the function (target).
    new_string = "".join(new_string) #since the output have to be a string we join the letters (elements of the list) to form a string of the remaining letters.
    return new_string

#call the function to verify the output
result = rmchar('pynative',4)
print(result)

#output
tive


#well there's an easier approach to this but .. this was what i thought of at the beggining.
