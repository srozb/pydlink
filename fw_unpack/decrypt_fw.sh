#!/bin/bash

echo decrypting $1 with key file:$2
openssl enc -d -aes-128-cbc -nosalt -in $1 -out decrypted_$1 -pass file:$2
