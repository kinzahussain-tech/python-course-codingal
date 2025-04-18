#take input from user
text = input(("Enter a sentence: "))
text = text.split()
bigWordLen = 0 #initialise

for word in text: #iterate loop
  wordLen = len(word) #string operation
  if wordLen>bigWordLen: #condition 1
    bigWordLen = wordLen

print("\nLargest Word: ")
for word in text: 
  wordLen = len(word)
  if wordLen==bigWordLen: #condition 2
    print(word) #display result