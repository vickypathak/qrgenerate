
import qrcode                                              
image = qrcode.make ('https://ican-doit.w3spaces.com/')
image.save('myQRcode.png')
image.show()

