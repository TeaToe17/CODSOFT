import random

length = int(input("What is the length of the password you intend to genrate? "))
character_pool = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz,@#!$%^&*().;/][?><]"

password = ''.join(random.choice(character_pool) for _ in range(length))
print(f"password: {password}")