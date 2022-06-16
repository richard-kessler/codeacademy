## Script to identify compromised user passwords and generate new passwords

## Code Academy Project - Hacking the Fender


## import libraries
import csv
import json

## open password file and parse for 'Username'
with open('passwords.csv') as password_file:
  compromised_users = []
  #password_file = passwords.read()
  password_csv = csv.DictReader(password_file)
  print(password_csv)
  for row in password_csv:
    #password_row = row.DictReader() 
    compromised_users.append(row['Username'])

## open compromised users list, create list of compromised users
with open('compromised_users.txt', 'w') as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)

## open json file, create customer dict for response
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {
    'recipient': 'The Boss',
    'message': 'Misson Success'
  }
  json.dump(boss_message_dict, boss_message)

## open new passwords file, write customer signature 
with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
## pass the customer signature to the new passwords object
  new_passwords_obj.write(slash_null_sig)  
