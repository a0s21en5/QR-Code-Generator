import qrcode as qr

input_ = input("Enter To Genarate QR Code: ")
img = qr.make(input_)

file_name = input("Enter Your File Name: ")
img.save(file_name)
