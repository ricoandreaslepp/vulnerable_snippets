#!/usr/bin/zsh
import bcrypt

pwd1 = b'a'*72+b'my_secret_that_no_one_knows'
pwd2 = b'a'*72
s = bcrypt.gensalt()

h1 = bcrypt.hashpw(pwd1, s)

assert bcrypt.checkpw(pwd2, h1)==True
print("correct password!")
