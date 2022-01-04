import rsa
import os

KEYFILE_PATH = os.environ.get('KEYFILE_PATH')

def start_server():
    cmd = './manage.py migrate && ./manage.py runserver 0:8000'
    os.system(cmd)


def check_keys():
    if os.path.exists(KEYFILE_PATH) == False:
        os.makedirs(KEYFILE_PATH, exist_ok=True)
    if os.path.exists(os.path.join(KEYFILE_PATH, 'private-key.rsa')) == False or os.path.exists(os.path.join(settings.KEYFILE_PATH, 'public-key.rsa')) == False:
        publicKey, privateKey = rsa.newkeys(2048)

        with open(os.path.join(KEYFILE_PATH, 'private-key.rsa'), "w+") as f:
            f.write(privateKey.save_pkcs1().decode())
            f.close()

        with open(os.path.join(KEYFILE_PATH, 'public-key.rsa'), "w+") as f:
            f.write(publicKey.save_pkcs1().decode())
            f.close()



def main():
    check_keys()
    start_server()

if __name__ == '__main__':
    main()
