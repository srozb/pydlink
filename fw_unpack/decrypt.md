# Decrypting D-Link firmware

1. download the FW file
2. unzip it
3. untar it
4. decrypt aes.key.rsa with rsa private key `./decrypt_fw_key.sh path/to/aes.key.rsa`
5. decrypt aes-encrypted files `./decrypt_fw.sh path/to/file.aes path/to/aes.key`
