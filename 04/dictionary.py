myDict = {
    "Fast": "In a quick manner",
    "Ashish": "A learner",
    "Level": [2, 4, 5, 8],
    "second": {'ap':'student'}
}

print(myDict['Fast'])
print(myDict['Level'])
print(myDict['second']['ap'])
myDict['Level'] = [4, 6, 7]
print(myDict)