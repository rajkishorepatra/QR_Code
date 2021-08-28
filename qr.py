from pyqrcode import QRCode
import pyqrcode

img = pyqrcode.create(
    "https://www.linkedin.com/in/raj-kishore-patra-247044213/"
)

img.png('myQRcode.png')
img.show()