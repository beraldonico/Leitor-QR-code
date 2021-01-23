import qrcode
import image

def create():
    # example data
    data = 'KEY PIX: Chave aleatoria'
    # output file name
    filename = "QR_USER.jpg"
    # generate qr code
    img = qrcode.make(data)
    # save img to a file
    img.save(filename)
    print('QR criado\n')