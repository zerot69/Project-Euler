# Project Euler

# Problem 59: XOR decryption
# Each character on a computer is assigned a unique code and the preferred standard is ASCII
# (American Standard Code for Information Interchange).
# For example, uppercase A = 65, asterisk (*) = 42,and lowercase k = 107.#
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
# taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
# restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.#
# For unbreakable encryption, the key is the same length as the plain text message,
# and the key is made up of random bytes.
# The user would keep the encrypted message and the encryption key in different locations, and without both "halves",
# it is impossible to decrypt the message.
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
# If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
# The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
# Your task has been made easy, as the encryption key consists of three lower case characters.
# Using p059_cipher.txt, a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain
# common English words, decrypt the message and find the sum of the ASCII values in the original text.


import time
import string


def decrypt(key, message):
    decrypted = []
    for i, char in enumerate(message):
        decrypted.append(chr(char ^ ord(key[i % len(key)])))
    return ''.join(decrypted)


def evaluate(message):
    common_words = ['the', 'and', 'that', 'with',
                    'this', 'for', 'you', 'have', 'be', 'not', 'are']
    words = message.split()
    score = 0
    for word in words:
        if word.lower() in common_words:
            score += 1
    return score


def main():
    start_time = time.time()
    encrypted = [int(x) for x in open(
        'D:\zerot69\@tuaans.bawps\WORKS\Programming\Python\ProjectEuler\Problem 051-100\problem_059_ciphertext.txt').read().split(',')]
    best_score = 0
    best_decryption = None
    best_key = None
    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            for c in string.ascii_lowercase:
                key = a + b + c
                decryption = decrypt(key, encrypted)
                score = evaluate(decryption)
                if score > best_score:
                    best_score = score
                    best_decryption = decryption
                    best_key = key
    print("Key:", best_key)
    print("Message:", best_decryption)
    print("Problem 59:",
          sum([ord(c) for c in best_decryption]))
    print("Total time: {}".format(time.time() - start_time))


if __name__ == '__main__':
    main()
