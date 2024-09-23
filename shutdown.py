import os
import time

n = list(input('Insert movie duration using colons - ":" ').split(':'))

print(n[0], n[1], n[2])

seconds = int(n[2]) + int(n[1]) * 60 + int(n[0]) * 3600 + 300 # extra five minute added

time.sleep(seconds) # seconds

print('chama', seconds)
os.system('shutdown /s /t 1') #/s shut down /t time delay for 1 second
# os.system('sudo shutdown -h now')  # For Linux/Mac
