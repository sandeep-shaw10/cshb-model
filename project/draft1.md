# 0 Algorithms

## 0.1 Secure Hash Algorithms

The Secure Hash Algorithms are a family of cryptographic hash functions published by the National Institute of Standards and Technology (NIST) as a U.S. Federal Information Processing Standard (FIPS), including:
1. **SHA-0:** A 160-bit hash function
2. **SHA-1:** A 160-bit hash function that shares characteristics similar to the MD5 hash function
3. **SHA-2:** It consists of two hash functions with different block sizes SHA-256 and SHA-512 and additionally, there are four truncated versions.
4. **SHA-3:** It is formerly known as Keccak as it supports the same hash lengths as SHA-2, and its internal structure differs significantly from the rest of the SHA family. 

### 0.1.1 SHA3-512
In this model, we have used SHA-3 as a principal hashing algorithm. It is because SHA-0 and SHA-1 is no longer used in real-world applications due to security vulnerabilities. SHA-3 is considered a more secure option than SHA-2 as its internal structure differs significantly from the rest of the SHA family.

The comparison among all families of SHA in terms of security: 

![3](./img/3.JPG)

The aim is to implement dynamic encryption using AES where the cipher key will vary according to the information passed. As AES-512 is designed and used to encrypt data which requires 512 bits of cipher key, therefore it is more suitable to use SHA3-512 which generates 512 bits of hash that can be easily passed to the AES algorithm.


### 0.1.2 SHA3-512 Implementation

As SHA3-512 is capable to withstand collision attacks and length extension attacks [x] therefore it is far more secure and efficient. To implement this algorithm, we will be using an external module name **hashlib** in Python programming language. This module provides us with most of the algorithms belonging to the SHA family.

1. Checking the presence of SHA3-512 

```py
import hashlib

# Available algorithm
print(hashlib.algorithms_guaranteed)
```
 
```txt
{
    ‘blake2b’, ‘shake_256’, ‘sha512’, ‘sha3_224’, 
    ‘sha384’, ‘sha3_512’, ‘sha3_256’, ‘sha3_384’, 
    ‘md5’, ‘sha256’, ‘sha224’, ‘sha1’, ‘blake2s’, 
    ‘shake_128’
}
```

We can observe that the algorithm **‘sha3_512’** exist.


2. Using SHA3-512

```py
import sys
import hashlib

if sys.version_info < (3, 6):
	import sha3

str = "CSHB Model"

# create a sha3 hash object
hash_sha3_512 = hashlib.new("sha3_512", str.encode())

print("\nSHA3-512 Hash: \n", hash_sha3_512.hexdigest())
```

```txt
SHA3-512 Hash:
fe3a5c5d82571204dce93169a1d8bedf1857a986d71437ff73090b8f3930c1825275ff565b935e2edc76212d9fb218710438770f1a939b43931b5d280e1e22ee
```



## 0.2 Base64

An encoding scheme that converts binary data into text format so that encoded textual data can be easily transported over the network without being corrupted or any data loss. The problem that arises while sending normal binary data is that bits can be misinterpreted by underlying protocols, and produce incorrect data at receiving node. The term Base64 is taken from the Multipurpose Internet Mail Extension (MIME) standard, which is widely used for HTTP and XML, and was originally developed for encoding email attachments for transmission. 

Base64 encoding and decoding are mainly used in Advance Encryption Standard to represent the encrypted data in this format or to decrypt the message represented in this format. As the encryption and decryption algorithm will require changing base64 data to binary and vice-versa, therefore the use of base64 is considered.

### 0.2.1 Base64 Implementation

The implementation of base64 is simple where the  process of converting binary data into a limited character set of 64
characters. The characters are A-Z, a-z, 0-9, +, and /. This character set is considered the
most common character set, and is referred to as MIME’s Base64. The 6 consecutive bits are converted to specific ASCII character and in case bits are not sufficient then it is padded.

![4](./img/4.JPG)

To implement this algorithm we use a predefined module name **base64** in Python programming language.

```py
from base64 import b64encode, b64decode

DATA = 'data to be encoded'

encoded = b64encode(DATA)
print('Encoded: ', encoded)

decode = base64.b64decode(encoded)
print('Decoded: ', decoded)
```

OUTPUT

```txt
Encoded: ZGF0YSB0byBiZSBlbmNvZGVk
Decoded: data to be encoded
```


## 0.3 AES-512

detailed description: 

[Reference:AES-512](../aes/aes512.py)

## 0.4 LSB Steganography

brief description

## 0.5 Hybrid Blockchain

brief description