import qrcode

qr_data = input('enter qrcode data\n')
img = qrcode.make(qr_data)
img.save('qr-code.img')
