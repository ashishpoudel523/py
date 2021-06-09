lan = {
    "namaste": "hello",
    "sanchai":"fine",
    "kursi":"chair",
    "amount":[1, 3, 4]
}
print(type(lan))

print("Words are:",  lan.keys())

a = input("Enter the Nepali word: \n")

#.get doesn't throw error
print("Meaning of your word is:", lan.get(a))