import qrcode as qr
import img   # as --- alias
qr= qr.QRCode(
    version=6,
    box_size=8,
    border=3
)
data = '''
 Name: MD.MERAJ
 Age :22
 College: jiet(jodhpur)
 Branch : CSE(AI&ML)
 contact: 6203239376 
 Jiet   : 0291-2868152/53'''

qr.add_data(data) 
qr.make(fit=True)  # limit of qr code space
img=qr.make_image(
    fill ="black",back="White"
)
img.save("MD.MERAJ.png")