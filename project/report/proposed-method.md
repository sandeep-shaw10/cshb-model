# Proposed Method

The principle idea is to construct a model where at various phases of data transmission from client to server and vice-versa, a specific algorithm is utilized to secure the data. This algorithm includes hashing, dynamic crypto-steganography, and the use of hybrid blockchain database storage. Thus this model of various algorithms is used to implement a text messaging app system that provides a secure data transfer from the client to the server and stores that particular data inside the database such that the integrity of data is conserved. 

The methodology in which the design and analysis of the solution proposed are:

#### Constant Key Storing

First of all the users of the chatroom will share a common and consistent secret code generated randomly when the chatroom is established. Depending on the nature of security these secret code may be stored either in user's device in decentralized manner or inside more secure layered database in centralized manner. Moreover the unique-id of the chatroom can also be used as the secret code or any randomly generated characters that will remained be constant.

#### Hashing and Dynamic Encryption

Once the connection is established and secret key is generated for the users, we will move on to the next step. The secret key combined with other fields of the message will be used to generate a hash value using Secure Hash Algorithm (SHA-512).

Then this hash value generated above is used as a symmetric key for the Advance Encryption Standard algorithm (AES) to encrypt the message. Moreover we will analyse various AES algorithm like AES-128, AES-192 and AES-256 which belong to the family of same 128 bits cipher key. Further we will compare it with AES-512 algorithm which we try to implement using a matrix of order 8, which will generate 512 bits cipher key.

#### Image Steganography

Once the data is encrypted, it is passed as input to generate an image using Steganography algorithms. We will try to analyse various steganograhy algorithm which suites best of this application and compare it with traditional Least Significant Bit Steganoraphy (LSB). According to the length of the encrypted message, a particular image of given dimensions will be calculated and used for the effective embedding of data inside the image. Then the Stego-object is sent to the server via API. Moreover, this type of image steganography will generate dynamic images based on the encrypted message that can be accommodated very easily and effectively. Moreover it should also provide room for additional bits to check the occurence of errors such as single bit error.

#### Storing Data to Server

At the server, the message is extracted from Stego-object which outputs the encrypted message. This data is fetched and stored inside the database.
While storing the encrypted message in a database, the traditional database will also perform and additional function by linking the hash of the previous messsage in the same chat room with the current message id using any Secure Hashing Algorithm. In this way the message in the chat is linked in a manner similar to blockchain. The funtionality is provided to the user to check or authenticate the integrity in their data. This feature will mine the existing data upto desired period and compare the linked hash value and if the data is removed or manipulated then it will be easily recognized by the user. The database admin can neither view the message nor it can be manipulated. Moreover in case of data breach, it is still encrypted and also the message in the chat room is secured.


#### Fetching Data from Server

The chat data can be retrieved in bulk from the server to the client. As the data was stored in encrypted format therefore it is still secure and at the client side the chat will be decrypted. The symmetric key can be obtained using the constant secret key and other attributes of the message which is passed to the AES and the plain text is obtained from the cipher text and is rendered on the screen.

In this manner, the data is encrypted and decrypted on the client side only therefore it is end-to-end encrypted as the encrypted message is stored on the remote database with a hybrid blockchain functionality to authenticate and check tampering in data if it exists. 