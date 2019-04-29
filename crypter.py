from Crypto.Cipher import AES
import base64
from rijndael.cipher.crypt import new
from rijndael.cipher.blockcipher import MODE_CBC
from pkcs7 import *

class RijndaelEncryptor(object):
    def __init__(self):
        self.encoder=PKCS7Encoder()

    def encrypt(self, text, input_key, input_iv='\x00'*16):
		pad_text = self.encoder.encode(text)
		rjn = new(input_key, MODE_CBC, input_iv, blocksize=16)
		return base64.b64encode(rjn.encrypt(pad_text))

    def decrypt(self, text, input_key, input_iv='\x00'*16):
		rjn=new(input_key, MODE_CBC, input_iv, blocksize=16)
		return self.encoder.decode(rjn.decrypt(base64.b64decode(text)))