#!/bin/bash

openssl rsautl -decrypt -inkey keys/private.pem -in $1 -out decrypted_$1

