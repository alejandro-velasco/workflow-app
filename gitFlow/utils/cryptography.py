import rsa
import os
from django.conf import settings

def encrypt_str(str):
	path = os.path.join(os.environ.get('KEYFILE_PATH'), 'public-key.rsa')
	with open(path, mode='rb') as pubkey:
		keydata = pubkey.read()
	pubkey_encoded = rsa.PublicKey.load_pkcs1(keydata)
	return rsa.encrypt(str.encode(), pubkey_encoded)

def decrypt_str(str):
	path = os.path.join(os.environ.get('KEYFILE_PATH'), 'private-key.rsa')
	with open(path, mode='rb') as privkey:
		keydata = privkey.read()
	privkey_encoded = rsa.PrivateKey.load_pkcs1(keydata)
	return rsa.decrypt(str, privkey_encoded).decode()
