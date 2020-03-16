words=[]
count=0
with open("text.txt","r") as file:
  for line in file:
      if line in words:
          words.append(line)
          k+=1
      else:
          pass
  print("The no.of Unique words:",k)