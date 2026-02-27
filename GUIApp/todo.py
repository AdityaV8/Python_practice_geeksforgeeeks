# from functions import get_todos, write_todos
import GUIApp.functions as functions
import time

print(f"Date : {time.strftime('%b %d-20%y ')}")
while True:
    user_action= input("type add or show or edit or quit or complete : ")
    user_action = user_action.strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo+"\n")

        functions.write_todos("todofile.txt",todos)



    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index,item in enumerate(todos):
            print(f"{index+1}-{item}",end ="")



    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print("task is ",todos[number-1])
            todos[number-1]=input("Enter the new task : ")+"\n"
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            print("Please enter like this : edit <no of task> .")
            continue


    elif user_action.startswith("quit"):
        break


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            print(f"{todos.pop(number-1)} task completed.")
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            print("Please enter like this : complete <no of task> .")
        except IndexError:
            print("There is no task with that number.") 
            continue


    else: # any anonymous case can be handled
        print("Hey! you have entered an wrong command")

print("Bye!")
#new_item = [item.strip("\n") for item in todos] #list comprehension