import hashlib,base58,binascii,ecdsa,qrcode
from PIL import Image

# Create Keys & Addresses (source: https://medium.com/coinmonks/bitcoin-address-generation-on-python-e267df5ff3a3)
# Step1: Generate ECDSA Private Key
ecdsaPrivateKey = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
# # print("ECDSA Private Key: ", ecdsaPrivateKey.to_string().hex())
# # print("------------------------------------------------------")

# Step2: Generate ECDSA Public Key from value at Step#1
ecdsaPublicKey = '04' +  ecdsaPrivateKey.get_verifying_key().to_string().hex()
# # print("ECDSA Public Key: ", ecdsaPublicKey)
# # print("------------------------------------------------------")

# Step3: SHA256(value at Step2)
hash256FromECDSAPublicKey = hashlib.sha256(binascii.unhexlify(ecdsaPublicKey)).hexdigest()
# # print("SHA256(ECDSA Public Key): ", hash256FromECDSAPublicKey)
# # print("------------------------------------------------------")

# Step4: RIDEMP160(value at Step#3)
ridemp160FromHash256 = hashlib.new('ripemd160', binascii.unhexlify(hash256FromECDSAPublicKey))
# # print("RIDEMP160(SHA256(ECDSA Public Key)): ", ridemp160FromHash256.hexdigest())
# # print("------------------------------------------------------")

# Step5: Prepend 00 as network byte to value at Step#4
prependNetworkByte = '00' + ridemp160FromHash256.hexdigest()
# # print("Prepend Network Byte to RIDEMP160(SHA256(ECDSA Public Key)): ", prependNetworkByte)
# # print("------------------------------------------------------")

# Step6: Apply SHA256 to value at Step#5 at 2 times to generate Checksum
hash = prependNetworkByte
for x in range(1,3):
    hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
# #     print("\t|___>SHA256 #", x, " : ", hash)
# # print("------------------------------------------------------")

# Step7: Get first 4 bytes of value at Step#6 as Checksum
cheksum = hash[:8]
# # print("Checksum(first 4 bytes): ", cheksum)
# # print("------------------------------------------------------")

# Step8: Append Checksum to value at Step#5
appendChecksum = prependNetworkByte + cheksum
# # print("Append Checksum to RIDEMP160(SHA256(ECDSA Public Key)): ", appendChecksum)
# # print("------------------------------------------------------")

# Step9: Generate Bitcoin Address with apply Base58 Encoding to value at Step#8
# Allows money to be received, but cannot be sent using this address (watch-only)
bitcoinAddress = base58.b58encode(binascii.unhexlify(appendChecksum))
Receive = bitcoinAddress.decode('utf8')
print("Bitcoin Address: ", Receive)

# Create Wallet Import Format (WIF) in order to send money from address created at Step9 (source: https://en.bitcoin.it/wiki/Wallet_import_format)
# Step10: Add a 0x80 byte in front of it for mainnet addresses or 0xef for testnet addresses. Also add a 0x01 byte at the end if the private key will correspond to a compressed public key.
private = '80'+ ecdsaPrivateKey.to_string().hex()
# # print(private)

# Step11: Perform SHA-256 hash on the extended key
shaprivate = hashlib.sha256(binascii.unhexlify(private)).hexdigest()
# # print(shaprivate)

# Step12: Perform SHA-256 hash on result of SHA-256 hash
doublehash = hashlib.sha256(binascii.unhexlify(shaprivate)).hexdigest()
# # print(doublehash)

# Step13: Take the first 4 bytes (8 characters) of the second SHA-256 hash; this is the checksum
extended = private + doublehash[0:8]
WIF = base58.b58encode(binascii.unhexlify(extended))
Import = WIF.decode('utf8')
print("Wallet Import Format: ", Import)

# Create QR Codes to print on cardstock (files save in same folder as program)
# Step14: Create QR Code to Receive Funds
img = qrcode.make(Receive)
img.save('Receive Address QR Code.png')

# Step15: Create QR Code to Gift Funds with Private Key's ability to move money
img = qrcode.make(Import)
img.save('Import QR Code.png')

# Step16: Open QR Codes upon Program Run
Image.open('Receive Address QR Code.png').show()
Image.open('Import QR Code.png').show()