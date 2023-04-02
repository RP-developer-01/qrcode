import qrcode

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data("https://github.com/RP-developer-01")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.show()
