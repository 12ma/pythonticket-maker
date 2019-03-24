first_name=""
last_name=""
age=None
des=""

def data_retrieve():
    global first_name
    first_name=input("Enter first name: ")
    global last_name
    last_name=input("Enter last name: ")
    global age
    age=int(input("Enter your age: "))
    global des
    des=input("Enter your destiny: ")

def data_process():
    print(first_name[0]+"." + last_name +"," + str(age) )
    print("Destination: " + des)

def ticket():
    data_retrieve()
    data_process()

ticket()


