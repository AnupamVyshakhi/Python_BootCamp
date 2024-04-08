s=input("Enter the string")
vowel="aeiouAEIOU"
count=0
for i in s:
    if i in vowel:
        count+=1
print("The number of the vowels is %d"%(count))