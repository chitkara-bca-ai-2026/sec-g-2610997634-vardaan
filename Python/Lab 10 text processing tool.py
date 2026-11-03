print("==============================================================")
print("                TEXT PROCESSING TOOL")
print("==============================================================")

sentence=input("Enter a sentence :")

print("--- Processing  results ---")

position=int(input("Enter position for indexing :"))
print("Character at postion  :",position,":",repr(sentence[position]))

start=int(input("Enter start index for slicing :"))
end=int(input("Enter end index for slicing :"))
print("Sliced string[0:5] :",repr(sentence[start:end]))

print("Uppercase  :",sentence.upper())
print("Lowercase  :",sentence.lower())

word=input("Enter word to replace :")
replacement=input("Enter replacement word :")
After_replace=sentence.replace(word,replacement)
print("After replace :",After_replace)

print("Length of sentence :",len(sentence))

print("==============================================================")
print("Analysis Complete!")
print("==============================================================")