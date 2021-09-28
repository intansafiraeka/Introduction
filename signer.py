from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import qrcode
#import codecs


file_in = open("intandut.docx", "rb")
message=file_in.read()
file_in.close()
key = RSA.import_key(open('private.key').read())
h = SHA256.new(message)
print(h.hexdigest())

'''
once hashing is done, we need to create a sign object through 
which we can sign a message
'''

signer=pkcs1_15.new(key)
signature=signer.sign(h)
print(signature)

ttd = qrcode.make(signature.hex())
ttd.save ("ttd.png")

file_out = open("signature.jpg", "wb")
file_out.write(signature)
file_out.close()

file_out = open("intandut1.docx", "wb")
file_out.write(message)
file_out.close()