def duplicate(string):
    duplicatestring=""
    for x in string:
        if x not in duplicatestring:
            duplicatestring+=x
    return duplicatestring
str=input("Enter the string")
print("string after removing duplicate is:",duplicate(str))
