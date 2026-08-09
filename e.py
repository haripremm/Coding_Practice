import qrcode

text = input("Enter the text or url:")

qr = qrcode.make(text)

filename = "Qrcode.png"

qr.save(filename)

print("QR Generated Sucessfully as", filename)