import qrcode
link=input("enter link:")
img=qrcode.make(link)
img.save("my_linkedin_qr.png")
print("QR code is generated")
