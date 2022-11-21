# Introduction

We are living in the modern era of computers and internet where most of our activity is digitalized and is performed online. The information on every aspects of our lives are being uploaded and transferred through internet. In a more generalized way internet is a form of computer network where multiple digital transaction occur within splits of seconds as our data is uploaded and transferred through the computer networks. Moreover, it is also important to secure the privacy as confidential online transaction or information might be accessed or manipulated by the attackers or any other third party attacks. Therefore to protect the data, the role of network security comes into action and to priortize safety of confidential information across the network.

In this project, we have proposed to build a secure and efficient model for data transmission between client and server. This model will be illustrated using a text messaging application using Hashing, Cryptography, Steganography with some concept of Blockchain which will be used to store and retrieve the message data in a more secure manner.

In this model we have tried to address some  major data security threats that usually make any regular chat application vulnerable are:
1. Man in the Middle Attack (MITM)
2. Data Breaching
3. Brute-Force Attack


Following are the fields that we are going to make use of in order to implement our proposed idea:

#### Computer Network:

Computer network is a system that helps us to connect and communicate a large number of self-dependent computers in the intention of sharing
information and resources or in simpler words when two or more computers are connected together, the entire system of two or more connected computers is called a computer networks. Today's user-centric applications are built on the most popular and widely used form of a computer network called internet.

#### Network Security:

In order to make a computer network trustworthy and reliable we have to go through three security measures confidentiality, integrity and availability which forms the basis of Network Security.The measures taken by the application developers and the computer scientists to make confirm these three actions are known as network security.


#### Attacks:

The three goals of security, confidentiality, integrity and availability can be threatened by some third party unethical measures. Such phenomenons are known as attacks. Attacks can take place in any from like snooping, traffic analysis, unauthorized modification, unauthorized access, data breaching etc. But throughout the project we have decided to create an algorithm that deals with two specific type of attacks, MITM or Man in the Middle Attack and Data Breaching. Also we have tried to modify an existing algorithm to prevent any instance of Brute Force Attack.


#### Man in the Middle Attack(MITM):

The MITM or Man in the Middle Attack is a general term of when a third person have view or modify access in a conversation between the server and the client. This breaches one of the most important aspects of network security that is confidentiality.


#### Data Breaching:

A data breach is a security violation, in which sensitive, protected or confidential data is copied, transmitted, viewed, stolen or used by an individual unauthorized to do so. Other terms for Data Breaching are unintentional information disclosure, data leak, information leakage and data spill.

#### Brute Force Attack:

In cryptography, a brute-force attack consists of an attacker systematically checks all possible passwords and passphrases until the correct one is found. This method of hacking uses trial and error to crack passwords, login credentials, and encryption keys. It is a simple yet reliable tactic for gaining unauthorized access to individual accounts and organizations’ systems and networks.

#### Cryptography:

Cryptography is technique of securing information and communications through use of codes so that only those person for whom the information is intended can understand it and process it. Thus preventing unauthorized access to information. The prefix “crypt” means “hidden” and suffix graphy means “writing”.

In Cryptography the techniques which are use to protect information are obtained from mathematical concepts and a set of rule based calculations known as algorithms to convert messages in ways that make it hard to decode it. These algorithms are used for cryptographic key generation, digital signing, verification to protect data privacy, web browsing on internet and to protect confidential transactions such as credit card and debit card transactions.
In our project we have tried to cipher a text message using cryptographic hash algorithms.

#### Hashing:

Unlike Cryptography where the cipher text can be encode and decode, Hashing algorithms are one-way programs which utilises a mathematical function to unscramble the text which can't be further decoded. This That enciphered text can then be stored instead of the password itself, and later used to verify the user.

Features of Hashing Algorithm
1. Takes an arbitrary amount of data input and produces a fixed-size output of enciphered text called a hash value.
2.  Minute change in input data should produce vast change in hash value.

In this project we used SHA-512 to obtain a hash value from arbitary length message which is used as a key for cryptography.

#### Steganography:

Steganography is the technique of hiding secret data within an ordinary, non-secret, file or message in order to avoid detection; the secret data is then extracted at its destination. The use of steganography can be combined with encryption as an extra step for hiding or protecting data.
In this project we have tried to use a PNG file as the pseudo non-secret file for hiding the data.

#### Blockchain:

A blockchain is a distributed database that is shared among the nodes of a computer network. As a database, a blockchain stores information electronically in digital format. Blockchains are best known for their crucial role in cryptocurrency systems, such as Bitcoin, for maintaining a secure and decentralized record of transactions. The innovation with a blockchain is that it guarantees the fidelity and security of a record of data and generates trust without the need for a trusted third party.

We have tried to implement an hybrid model of blockchain technology by implementing some key concept of Blockchain in exisitng databases.