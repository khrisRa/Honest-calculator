import sys
# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
ops = ["+", "*", "-", "/"]
memory = 0


def is_one_digit(v):
    output = v > - 10 and v < 10 and v.is_integer()
    return output


def check(v1, v2, v3):
    try:
        msg = ""
        output = (is_one_digit(v1) and is_one_digit(v2))
        if output:
            msg = msg + msg_6
        else:
            pass
        if (v1 == 1 or v2 == 1) and v3 == "*":
            msg = msg + msg_7
        if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
            msg = msg + msg_8
        else:
            pass
        if msg != "":
            msg = msg_9 + msg
            print(msg)
        else:
            pass
    except ValueError:
        pass
    
    
def sure(result_2, memory_2):
    msg_index = 10
    msg = {
        10:"Are you sure? It is only one digit! (y / n)",
        11:"Don't be silly! It's just one number! Add to the memory? (y / n)",
        12:"Last chance! Do you really want to embarrass yourself? (y / n)"
        }
    while msg_index < 13:
        print(msg[msg_index])
        a = input()
        if a =="y":
            msg_index +=1
        else:
            break
    if msg_index > 12:
        memory_2 = result_2
    else:
        pass
    return memory_2


def store(result_1, memory_1):
    while True:
        has_memory = input(msg_4)
        if has_memory == "y":
            if is_one_digit(result_1):
                memory_1 = sure(result_1, memory_1)
            else:
                memory_1 = result_1
            break
        elif has_memory != "n":
            break
        else:
            break
    return memory_1

    
def cont():
    while True:
        continue_calc = input(msg_5)
        if continue_calc == "y":
            break
        elif continue_calc == "n":
            sys.exit()
        else:
            break
            

while True:
    try:
        print(msg_0)
        calc = input()
        x, oper, y = calc.split()
        if x == "M":  
            x = memory
        if y == "M":
            y = memory
        x = float(x)
        y = float(y)
        if oper in ops:
            check(x, y, oper)
            if oper == "+":
                result = x + y
                print(result) 
                memory = store(result, memory)
                cont()
            elif oper == "-":
                result = x - y
                print(result)
                memory = store(result, memory)
                cont()                
            elif oper == "*":
                result = x * y
                print(result)
                memory = store(result, memory)
                cont()                 
            elif oper == "/" and y != 0:
                result = x / y
                print(result)
                memory = store(result, memory)
                cont()                
            else:
                print(msg_3)
        else:
            print(msg_2)
    except ValueError:
        print(msg_1)