from nltk import pos_tag, word_tokenize, Text

f=open("sample.txt","r")
read_data=f.read()
print (read_data)
print("Total no of Tokens are:",len(word_tokenize(read_data)))
tokens=word_tokenize(read_data)

print(tokens)
tokens1=(set(tokens))
tokens2=list(tokens1)
netdata=set(read_data);
for index in range(len((tokens2))):
    print("probability of ",tokens2[index],": is",tokens.count(tokens2[index])/len(tokens));

f.close();