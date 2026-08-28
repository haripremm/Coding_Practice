import qrcode

text = input("Enter the text or url:")

qr = qrcode.make(text)

filename = "Qrcode.png"

qr.save(filename)

print("QR Generated Sucessfully as", filename)

#Reverse A String

text = input("Enter the string:")
reverse = ""
for i in text:
    reverse = i+reverse
print(reverse)

#Count Vowels in a strig

text = input("Enter the String:")
count = 0
for i in text:
    if i in "aeiou":
        count+=1
print(count)

#Remove the Repeatig words
text = input("Enter the String:")
result= ""
for i in text:
    if i not in result:
        result+=i
print(result)

#find first not repeating letter

text = input("Enter the number:")
for i in text:
    if text.count(i)==1:
        print(i)
        break

#Find largest digit number in text

a = int(input("Enter the number:"))
count =0
while a>0:
    digit = a%10
    count = count*10+digit
    a//=10
print(count)

#find the common element in the list
a=[1,2,3,4,5]
b=[2,6,7,3,1]
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)

#Reverse the list
a=[12,23,34,45,56]
b=[]
for i in a:
    b.insert(0,i)
print(b)

#Reverse word without Charcter
text = "I Love Myself"
word = text.split()
result = " ".join(word[::-1])
print(result)







