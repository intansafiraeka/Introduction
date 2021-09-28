from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import cv2
import cv2_ext

key = RSA.import_key(open('public.key').read())


file_in = open("intandut1.docx", "rb")
message=file_in.read()
file_in.close()

d = cv
signature = cv2.imread("ttd.png")
print(signature)
h = SHA256.new(message)

try:
    pkcs1_15.new(key).verify(h, signature)
    print ("The signature is valid.")
except (ValueError, TypeError):
    print ("The signature is not valid.")