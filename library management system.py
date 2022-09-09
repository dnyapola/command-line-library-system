import fileinput


def view_people():
    with open("PEOPLE.txt") as file:
        title=file.readline()
        print("..........BORROWED BOOKS.......")
        while title !="":
            person_id= file.readline()
            title= title.rstrip("\n")
            person_id = person_id.rstrip("\n")
            print("title:  ", title)
            print("person id: ", person_id)
            print("...............................")
            title= file.readline()  
    file.close()


def add_book():
#allow the admin to add a book to the library
    books = open("BOOKS_DB.txt",'a') 
    title = input("please enter the name of the book you want to add to the library:\n")
    copies= input("enter number of copies of the book:\n")
    books.write(title +"\n")
    books.write(copies +"\n")
    print("you have added" ,title ," with ",copies,"copies to the database\n")
    books.close()
    main()


def view():
    #use my text file as a database to store books in library. allows you to view books
    with open("BOOKS_DB.txt") as file:
        title=file.readline()
        print("..........AVAILABLE BOOKS.......")
        while title !="":
            copies= file.readline()
            title= title.rstrip("\n")
            copies = copies.rstrip("\n")
            print("title:  ", title)
            print("copies: ", copies)
            print("...............................")
            title= file.readline()  
    file.close()

    

def borrow():
    # shows user the books available and allows "them" to select if it isnt in the library it loops back to available books
    print("Available Books Are:\n")
    view()
    book_borrow = input("Please enter the name of the book you want to borrow :")
    book_deduct=1
    with open("BOOKS_DB.txt",'r') as file:
        title=file.read()
        if book_borrow in title:
            person= input ("enter your Unique ID:\n")
            record=open("people.txt",'a')
            record.write(book_borrow +"\n")
            record.write(person +"\n")
            print("Person ID ",person," has borrowed a copy of ",book_borrow,"\n")
            record.close()

            book_deduction=1
            with open("BOOKS_DB.txt",'r') as f:
                newdata=f.readlines()
            replace=""
            line_number = 0
            count = 0
            f=open("BOOKS_DB.txt",'r')
            file= f.read().split('\n')
            for i, line in enumerate(file):
                 if book_borrow in line:
                    for b in file[i+1:i+2]:
                        value = int(b)
                        change = value - (book_deduct)
                        replace = b.replace(b, str(change))
                        line_number = count
                    count = i + 1 
            f.close()
            newdata[count] = replace + '\n'
            with open('BOOKS_DB.txt', 'w') as f:
                for line in newdata:
                    f.write(line)
            view()

        else:
            print("the book is not available. please choose another")
            return borrow()
    
    
def return_book():
    book_return = input("Please enter the name of the book you want to return :")
    with open("BOOKS_DB.txt",'r') as file:
        title=file.read()
        if book_return in title:
            person= input ("enter your Unique ID:\n")
            for line in file:
                if title in line:
                    for i in range(1):
                         next(file, None)
                else:
                    print(line.strip('\n'), end='\n')
    
           

            book_add=1
            with open("BOOKS_DB.txt",'r') as f:
                newdata=f.readlines()
            replace=""
            line_number = 0
            count = 0
            f=open("BOOKS_DB.txt",'r')
            file= f.read().split('\n')
            for i, line in enumerate(file):
                 if book_return in line:
                    for b in file[i+1:i+2]:
                        value = int(b)
                        change = value + (book_add)
                        replace = b.replace(b, str(change))
                        line_number = count
                    count = i + 1 
            f.close()
            newdata[count] = replace + '\n'
            with open('BOOKS_DB.txt', 'w') as f:
                for line in newdata:
                    f.write(line)
            print("you have succesfully returned ",book_return)

            #delete the record from persons database if book is returned
            file =fileinput.input('PEOPLE.txt', inplace=True)
            for line in file:
                if book_return in line:
                    for i in range(1):
                         next(file, None)
                else:
                    print(line.strip('\n'), end='\n')
            book_return 
                
            view()

        else:
            print("update not successful")
            exit()

def main():
    choice  =int(input("WELCOME TO JENGA SCHOOL LIBRARY MANAGEMENT SYSTEM \n Select 1 : To view books \n Select 2: To borrow a book \n Select 3: To Return a book \n Select 4:  To Add a book to the Library \n Select 5: To View borrowed books\n Select 6: To exit\n"))
    if choice==1:
        return view()
    elif choice ==2: 
         return borrow()
    elif choice== 3:
        return return_book()
    elif choice==4:
         return add_book()
    elif choice ==5:
         return view_people()
    elif choice==6:
         exit()
    else:
        print("You didnt select a valid number")
        return main()
   
main()


