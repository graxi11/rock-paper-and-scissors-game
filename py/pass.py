master_pwd = input('what is the master password? ')

def view():
  with open('passwords.txt', 'r') as f:
    for line in f.readline():
      data = line.rstrip()
     

def add():
   name = input('Account Name: ')
   pwd = input('Password: ')

   with open('passwords.txt', 'a') as f:
     f.write(name + ' ' + pwd + '\n')
      

while True:
   mode = input('would you like to add a new password or view existing ome(view, add), press q to quit?  ')
   if mode == 'q':
    break
 
   if mode == 'view':
    view()
   elif mode == 'add':
    add()
   else:
    print('invalid mode.')          
