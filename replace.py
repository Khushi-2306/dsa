text="i love apples"
words=text.split()
for i in range (len(words)):
    if words[i]=="apples":
        words[i]="oranges"

        new_text=" ".join(words)
        print("string before replace of words:",text)
        print("string after replace of words:",new_text)