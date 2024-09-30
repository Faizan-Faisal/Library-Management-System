# Books Data
book1 = {
    "uid": 1,
    "name": "Lean Startup",
    "author": "Eric Ries",
    "availableStatus": "Available" ,
}
book2 = {
    "uid": 2,
    "name": "Rich Dad Poor Dad",
    "author": "Robert T. Kiyosaki",
    "availableStatus": "Available" ,
}
book3 = {
    "uid": 3,
    "name": "Deep Learning with Python" ,
    "author": "François Chollet",
    "availableStatus": "Available" ,
}
book4 = {
    "uid": 4,
    "name": "Python Machine Learning",
    "author": "Sebastian Raschka",
    "availableStatus": "Available" ,
}
book5 = {
    "uid": 5,
    "name": "Your Journey to Mastery",
    "author": "Andrew Hunt",
    "availableStatus": "Available" ,
}
books = [book1,book2,book3,book4,book5]         # books list

#  User Data
user1 = {
    "uid": 1,
    "name": "Faizan",
    "returned": [],
    "booksBorrowed": [],

}
user2 = {
    "uid": 2,
    "name": "Hassan",
    "returned": [],
    "booksBorrowed": [],

}
user3 = {
    "uid": 3,
    "name": "Husnain",
    "returned": [],
    "booksBorrowed": [],

}
users = [user1, user2, user3]  #  user list

# Adding User
def addingUser():
    addUserName = input("Enter User detail(NAME): ")
    count = len(users) +1

    newUser = {
    "uid" : count ,
    "name" : addUserName,
    "returned" : [],
    "booksBorrowed": []
    }
    users.append(newUser)

# Adding Book
def addingBook():
    addBookName = input("Enter Book NAME: ")
    addAuthorName = input("Enter Author NAME: ")
    count = len(books) +1

    newBook = {
    "uid" : count ,
    "name" :addBookName,
    "author": addAuthorName,
    "availableStatus": "Available",
    }
    books.append(newBook)
    print(books)

# Search Book
def searchingBook(books):
 searchBook = input("Enter Book Name or UID: ")
 lowersearchBook = searchBook.lower()
 bookFound = False


 for book in books:
  # lower casing the letters
  lowerbookName = book.get("name").lower()
  if( lowersearchBook in lowerbookName or lowersearchBook == str(book.get("uid"))):
   print("Book Details:\n")
   for key , value in book.items():
     bookdetail = f"{key} : {value}"
     print(bookdetail)
   bookFound = True
   return book
  
 if(not(bookFound)): 
   print("No book Found")

# Search User
def searchingUser(users):
  searchUser = input("Enter User Name or UID: ")
  lowersearchUser = searchUser.lower()
  userFound = False

  for user in users:
    loweruserName = user.get("name").lower()
    if( lowersearchUser in loweruserName or lowersearchUser == str(user.get("uid"))):
        print("User Detail:\n")
        for key , value in user.items():
         userdetail = f"{key} : {value}"
         print(userdetail)
        userFound = True
        return user
  
  if(not(userFound)): 
   print("No User Found")

# Borrowing Book
def borowedBook(books, users):
    book = searchingBook(books)
    user = searchingUser(users)
    if(book.get("availableStatus") == "Available"):
     book.update({"availableStatus": "Checked-out"})
     user["booksBorrowed"].append(book["name"])
     print(f"Borrowed Book: {book["name"]} to User: {user["name"]}")
    else:
       print("Book is already checked-out")

# Returning Book
def  returningBook(books, users):
    book = searchingBook(books)
    user = searchingUser(users)
    if(book.get("availableStatus") == "Checked-out"):
      book.update({"availableStatus": "Available"})
      user["booksBorrowed"].pop(book["name"])
     
    else:
       print("Book is already in library")

# Viewing Books
def BOOKS(books):
 for book in books:
    for key, value in book.items():
        print(f"{key}: {value}")
 return book
def AvailableBOOKS(books):
 for book in books:
    if(book["availableStatus"]== "Available"):
     for key, value in book.items():
        print(f"{key}: {value}")
 return book
def CheckedoutBOOKS(books):
 for book in books:
    if(book["availableStatus"]== "Checked-out"):
     for key, value in book.items():
        print(f"{key}: {value}")
 return book

def viewingBooks():
    print("------------------\nVIEWWING BOOKS:\n")
    print("1. ALL Books\n2. Available Books\n3. Checked-out Books\n\n")
    choice = int(input("Enter your choice: "))
    while(not(choice >= 1 and choice <=3)):
        choice = int(input("Enter your choice again: "))
    if   choice == 1:
        BOOKS(books)

    elif choice == 2:
        
            AvailableBOOKS(books)
       
    elif choice == 3:
         
          CheckedoutBOOKS(books)

# Viewing Users
def USERS(users):
 for user in users:
    for key, value in user.items():
        print(f"{key}: {value}")
 return user
def BorrowedUsers(users):
 for user in users:
    if(not(user["booksBorrowed"] ==[])):
     for key, value in user.items():
        print(f"{key}: {value}")
 return user
def ClearUsers(users):
 for user in users:
    if (user["booksBorrowed"] ==[]):
     for key, value in user.items():
        print(f"{key}: {value}")
 return user

def viewingUsers():
    print("------------------\nVIEWWING BOOKS:\n")
    print("1. ALL Users\n2. Borrowed Books Users\n3. Cleared-Books Users\n\n")
    choice = int(input("Enter your choice: "))
    while(not(choice >= 1 and choice <=3)):
        choice = int(input("Enter your choice again: "))
    if   choice == 1:
        USERS(users)

    elif choice == 2:
        
          BorrowedUsers(users)
       
    elif choice == 3:
         
          ClearUsers(users)


# Interface

while True:
    print("\nWelcome to library management System\n-------------------- ")
    print("""Please choose an option:\n0. Exit\n1. Search User\n2. Search book\n3. Borrow a book\n4. Return a book\n5. View all books\n6. View all users\n7. Adding Users / Books""")
    option = int(input("Select an option: "))
    if option == 0:
        print("Exiting...")         # exit
        break   
    elif option == 1:
       searchingUser(users)        # search user
       
       n = int(input("Press 0 to exit or any number to back: "))
       if(n == 0):
          print("Exiting....")
          break    
    elif option == 2:
       searchingBook(books)        # search books
       n = int(input("Press 0 to exit or any number to back: "))
       if(n == 0):
          print("Exiting....")
          break
    elif option == 3:
       borowedBook(books, users)   # borrow books
       n = int(input("Press 0 to exit or any number to back: "))
       if(n == 0):
          print("Exiting....")
          break
    elif option == 4:
       returningBook(books, users)                      # return a book
       n = int(input("Press 0 to exit or any number to back: "))
       if(n == 0):
          print("Exiting....")
          break
    elif option == 5:
       viewingBooks()              # view all books
       n = int(input("Press 0 to exit or any number to back: "))
       if(n == 0):
          print("Exiting....")
          break
    elif option == 6:
       viewingUsers()             # view all users
     
       n = int(input("Press 0 to exit or any number to back: "))
       if(n == 0):
          print("Exiting....")
          break
    elif option == 7:
       adding = input("Press 'u' to add User\n Press 'b' to add book: ")
       if (adding.lower() == 'u' ):  
          addingUser()
       elif  (adding.lower() == 'b' ):  
          addingBook()
       n = int(input("Press 0 to exit or any number to back: "))
       if(n == 0):
          print("Exiting....")
    else:
       print("Invalid choice!")
       
       option = int(input("Select option Again: "))