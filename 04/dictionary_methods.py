myDict = {
    "Fast": "In a quick manner",
    "Ashish": "A learner",
    "Level": [2, 4, 5, 8],
    "second": {'ap':'student'}
}

print(myDict.keys()) #prints all keys of ictionary
print(myDict.items()) #prints the items of the dictionary
print(myDict.values()) #prints all the values in the dictionary

myDict.update(
    {
        "Elon":"Musk",
        "Data":"Science",
        "Class":"1, 2, 3",
        "Fast":"Doing something quickly"
    }
)

if "AP" in myDict:{
    print("Its exists.")
}
else:{
    print("Not exists")
}

#similarities between .get and [] syntax
print(myDict["Ashish"])  #prints values associated with Ashish
print(myDict.get("Ashish")) #prints values associated with Ashish


#differences between .get and [] syntax
print(myDict["Ashish2"]) #throws an error as it is not present in the dictionary
print(myDict.get("Ashish2")) #Returns none as it is not present in dictionary


