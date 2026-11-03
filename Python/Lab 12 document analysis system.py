sentence=input("Enter a sentence:")

words=len(sentence.split())
vowels=0
consonents=0
digits=0
spaces=0
special=0

for ch in sentence:
    if ch.lower() in "aeiou":
        vowels+=1
    elif ch.isalpha():
        consonents+=1
    elif ch.isdigit():
        digits+=1
    elif ch ==" ":
        spaces+=1
    else:
        special+=1

total_letters=vowels +consonents
total_characters=len(sentence)

if total_letters>0:
    vowel_percentage=(vowels/total_letters)*100
else:
    vowel_percentage=0

print("===============================================")
print("DOCUMENT ANALYSIS REPORT")
print("================================================")
print("Sentence:",sentence)
print("Total character:",total_characters)


print("---Character Breakdown---")
print("Words            :", words)
print("Vowels           :", vowels)
print("Consonents       :", consonents)
print("Digits           :", digits)
print("Spaces           :", spaces)
print("Special Character:", special)

print("---Summary---")
print("Total Letters:",total_letters)
print("Vowel percentage:,{:.1}%".format(vowel_percentage))

print("===============================================")
print("Analysis Complete!")
print("================================================")