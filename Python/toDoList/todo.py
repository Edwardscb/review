# import required modules
import sys
import datetime



# create a help function
def help():
    sa = """Usage :-
$ ./todo add "todo item"    # Add a new todo
$ ./todo ls                 # Show remaining todos
$ ./todo del NUMBER         # Delete a todo
$ ./todo done NUMBER        # Complete a todo
$ ./todo help               # Show usage
$ ./todo report             # Statistics"""
    sys.stdout.buffer.write(sa.encode('utf8'))

def add(item):
    """ Adds todo file to the todo.txt document"""

    todo_File = open('todo.txt', 'a')
    todo_File.write(item)
    todo_File.write("\n")
    todo_File.close()
    item = '"'+item+'"'
    print(f"Added todo: {item}")

def ls():
    """ print the todo list"""
    try:
        app()
        todo_Length = len(todo_Data)

        for item in todo_Length:
            # Looks like we use stdout.buffer when writing bytes?
            sys.stdout.buffer.write(f"[{item}] {todo_Data[todo_Length]}".encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
            todo_Length = todo_Length - 1

    except Exception as e:
        raise e

def done(num):
    """ when called, marks task as complete and writes it to done.txt"""

    try:
        app()
        num = int(num)
        done_File = open('done.txt', 'a')
        todo_String = 'x ' + str(datetime.datetime.today()).split()[0] + ' ' + todo_Data[num]

        done_File.write(todo_String)
        done_File.write("\n")
        done_File.close()
        print(f"Marked todo #{num} as done.")

        with open("todo.txt", "r+") as f:
        # using with is the better practice, because it will be automatically closed when finished
            lines = f.readlines()
            # readlines() will return all lines in the file, as a list where each line is an item in the list object.  It is a method that returns a list containing each line the file as a list item
            # you could also pass an argument to it which would represent the number of bytes not to exceed.
            f.seek(0)
            # seek() is used to change the position of the file handle to a given specific position.  0 sets the reference point at the beginning of the file.

            for i in lines:
                if i.strip('\n') != todo_Data[num]:
                    f.write(i)
            f.truncate()
            # truncate() method resizes the file to the given number of bytes, if not specified, the current position will be used.
    except:
        print(f"Error: todo #{num} does not exist.")

def report():
    """ Used to show statistics, prints total num of completed tasks and total num of pending tasks"""

    app()
    try:
        done_File = open('done.txt', 'r')
        count = 1

        for line in done_File:
            line = line.strip('\n')
            done.update({count: line})
            count = count + 1
            print(f"{str(datetime.datetime.today()).split()[0]} Pending : {len(todo_Data)} Completed : {len(isDone)}")
    except:
        print(f"{str(datetime.datetime.today()).split()[0]} Pending : {len(todo_Data)} Completed : {len(isDone)}")

def del_Item(num):
    """ Deletes an item from the todo list based on its item number"""

    try:
        num = int(num)
        app()

        # utility function defined in main
        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i.strip("\n") != todo_Data[num]:
                    f.write(i)
            f.truncate()
        print(f"Deleted todo #{num}")

    except Exception as e:
        print(f"Error: todo #{num} does not exist. Nothing was deleted.")

def app():
    """ Main application program / functionality """

    try:
        f = open("todo.txt", "r")
        count = 1
        for line in f:
            line = line.strip("\n")
            todo_Data.update({count: line})
            count = count + 1
    except:
        sys.stdout.buffer.write("There are no pending todos!".encode('utf8'))

if __name__ == '__main__':
        try:
            todo_Data = {}
            isDone = []
            args = sys.argv

            if (args[1] == 'del'):
                args[1] = 'del_Item'
            
            if (args[1] == 'add' and len(args[2:]) == 0):
                sys.stdout.buffer.write("Error: Missing todo string. Nothing added.".encode('utf8'))
            
            elif (args[1] == 'done' and len(args[2:]) == 0):
                sys.stdout.buffer.write("Error: Missing NUMBER for marking todo as done.".encode('utf8'))
            
            elif (args[1] == 'del_Item' and len(args[2:]) == 0):
                sys.stdout.buffer.write("Error: Missing NUMBER for deleting todo.".encode("utf8"))

            else:
                # this just returns what the user typed to the user?
                globals()[args[1]](*args[2:])
        
        except Exception as e:
            help()
            