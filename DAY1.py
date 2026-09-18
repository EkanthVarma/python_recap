email_id = "saketh@codegnan.com"
#print(email_id[7:15])

email_ids = ['ekanthvarma2005@gmail.com','ekanthvarma910@gmail.com','ekanthvarma1204@gmail.com','ekanthvarma11@gmail.com']

print(len(email_ids))
print(email_ids[1])
print(email_ids[-2:])

#store 3 more mail ids at a time
email_ids.extend(['ekanth@gmail.com','varma@gmail.com'])
print(email_ids)

# access each email id one by one
for mail in email_ids:
    print(f'Mail id of person is {mail}')

users = {}
for i in range(len(email_ids)):
    users[i] = email_ids[i]
print(users)

users= dict.fromkeys(email_ids)
users['ekanthvarma2005@gmail.com'] = 95
print(users)

#enumerate - it provide by default a counter object (you can store in desired collection
users = enumerate(email_ids,1)
print(dict(users))

#python - object
#Functions - First class objects
#set is a unordered collection as no indexing
