syntax_file = open('syntax.GCU-PL', 'r') # stores the gcu-pl file as variable "lexer_file"
count = 0
table = []
table2 = []

while True: # this loop iterates through the file and stores the values into a list
    count += 1 # inceases the count

    line = syntax_file.readline() # stores each line read in from the gcu-pl file into the variable line
    table.append(line) # appends the value of the line read in from the gcu-pl file into the list "table"

    if not line: # checks for the last line of the file
        break # exits the loop if there are no more lines
    #print("Line{}: {}".format(count, line.strip())) # prints out the lines of the file in a clean method, displaying line numbers

syntax_file.close() # closes the gcu-pl file as it no longer needs to be read
#print(table) # prints the table

for x in table: # appends each line of the table into a list of lists, this is what creates the table
    #print(x.split()) # prints the line using the split() function allows us to look at each string between every space
    table2.append(x.split()) # each line is appended into the list "table2" this is now a list of lists, showing each line in order

table2.pop()

#for x in table2:
#    print(x)
count = 0
tac = []
main = []
unused = []
line = []
line2 = []
inMain = False
regCount = 0
block = 0

opcode = ""
arg1 = -101
arg2 = -101
dest = ""

temp = ""

# OBTAIN THE MAIN FUNCTION BLOCK
while count < len(table2) - 1:
    while inMain != True:
        if table2[count][1] == "TYPE":
            if table2[count + 1][1] == "identifier":
                if table2[count + 2][0] == "(":
                    if table2[count + 1][0] == "main":
                        inMain = True

        count += 1


    if table2[count][1] == "TYPE":
        if table2[count + 1][1] == "identifier":
            if table2[count + 2][0] == "[":
                print("array " + str(table2[count + 1][0]))
                opcode = "array"
                arg1 = table2[count + 3][0]
                arg2 = "null"
                dest = table2[count + 1][0]
                line = [opcode, arg1, arg2, dest]
                main.append(line)

            elif table2[count + 2][1] == "Endline":
                print("declaration " + str(table2[count + 1][0]))
                opcode = table2[count][0]
                arg1 = "null"
                arg2 = "null"
                dest = table2[count + 1][0]
                line = [opcode, arg1, arg2, dest]
                main.append(line)

            elif table2[count + 2][1] == "COMMA":
                print("parameter " + str(table2[count + 1][0]))
                opcode = table2[count][0]
                arg1 = "null"
                arg2 = "param"
                dest = table2[count + 1][0]
                line = [opcode, arg1, arg2, dest]
                main.append(line)
            
            elif table2[count + 2][0] == ")":
                if table2[count + 3][0]== "{":
                    print("parameter " + str(table2[count + 1][0]))
                    opcode = table2[count][0]
                    arg1 = "null"
                    arg2 = "param"
                    dest = table2[count + 1][0]
                    line = [opcode, arg1, arg2, dest]
                    main.append(line)

            elif table2[count + 2][0] == "(":
                if table2[count + 1][0] != "main":
                    print("function " + str(table2[count + 1][0]))
                    line = ["call", "null", "null", table2[count + 1][0]]
                    main.append(line)
                else:
                    while inMain != False:
                        if table2[count][0] == "{":
                            block += 1
                        elif table2[count][0] == "}":
                            block -= 1
                            if block == 0:
                                inMain = False

                        count += 1

    elif table2[count][1] == "identifier" or table2[count][1] == "num":
        if table2[count + 1][1] == "binOP":
            if table2[count + 2][1] == "identifier" or table2[count + 2][1] == "num":
                if table2[count + 3][0] == ")":
                    print("conditional " + str(table2[count][0]) + " " + str(table2[count + 1][0]) + " " + str(table2[count + 2][0]))
                    if arg1 == -101:
                        arg1 = table2[count + 1][0]
                    if arg2 == -101:
                        arg2 = table2[count + 3][0]
                    line = [table2[count + 1][1], arg1, arg2, table2[count][1]]
                    arg1 = arg2 = -101
                    main.append(line)
                else:
                    print("binary operation: " + str(table2[count][0]) + " " + str(table2[count + 1][0]) + " " + str(table2[count + 2][0]))

        elif table2[count + 1][0] == "=":
            print("assignment " + str(table2[count][0]) + " =", end = " ")
            
            if table2[count + 2][0] == "[":
                line = []
                line.append("adecl")
                line.append(table2[count][0])
                while table2[count + 2][0] != ';':
                    if table2[count + 2][0].isnumeric():
                        line.append([table2[count + 2][0]])
                    count += 1
                
                main.append(line)

            else:

                line = []
                line.append(table2[count][0])
                while table2[count + 2][0] != ";":
                    print(str(table2[count + 2][0]), end = " ")
                    line.append(table2[count + 2][0])
                    count += 1

                dest = line[0]
                arg1 = line[1]
                opcode = line[2]
                arg2 = line[3]
                line2 = [opcode, arg1, arg2, dest]
                main.append(line2)

                if len(line) > 4:
                    count2 = 2
                    while count2 < len(line) - 1:
                        arg1 = line[count2 + 1]
                        opcode = line[count2 + 2]
                        arg2 = line[count2 + 3]
                        dest = line[0]

                        line = [opcode, arg1, arg2, dest]
                        main.append(line)

                        count2 += 3

            print("")

    elif table2[count][0] == "]":
        if table2[count + 1][0] == "=":
            print("assignment " + str(table2[count - 3][0]) + str(table2[count - 2][0]) + str(table2[count - 1][0]) + str(table2[count][0]) + " =", end = " ")
            line = []
            count2 = count
            line.append(table2[count - 1][0])
            while table2[count + 2][0] != ";":
                line.append(table2[count + 2][0])
                print(str(table2[count + 2][0]), end = " ")
                count += 1
            print("")

            dest = line[0]
            arg1 = line[1]
            opcode = line[2]
            arg2 = line[3]
            line2 = [opcode, arg1, arg2, dest]
            main.append(line2)

 
            if len(line) > 4:
                count2 = 2
                while count2 < len(line) - 1:
                    arg1 = line[count2 + 1]
                    opcode = line[count2 + 2]
                    arg2 = line[count2 + 3]
                    dest = line[0]

                    line = [opcode, arg1, arg2, dest]
                    main.append(line)

                    count2 += 3

                
    
    elif table2[count][0] == "return": # optimization, stop searching for code after return statements
        print("return " + table2[count + 1][0])
        opcode = table2[count][0]
        arg2 = "null"
        arg1 = table2[count + 1][0]
        dest = "system"

        if table2[count + 2][1] != "Endline":
            if table2[count + 2][0] == "[":
                arg2 = table2[count + 3][0]
                dest = "array"
            elif table2[count + 2][0] == ",":
                arg2 = table2[count + 3][0]

        line = [opcode, arg1, arg2, dest]
        main.append(line)
        while table2[count][0] != "}":
            count += 1


    elif "keyword" in table2[count][1]:
        print("keyword " + str(table2[count][0]))
        if table2[count + 3][0] == "(":
            while table2[count + 3][0] != ")":
                if table2[count + 3][1] == "num":
                    if arg1 == -101:
                        arg1 = table2[count + 3][0]
                    else:
                        arg2 = table2[count + 3][0]

                count += 1

            line = [table2[count - 4][0], arg1, arg2, table2[count - 2][0]]
            main.append(line)

            line = ["call", arg1, arg2, table2[count - 2][0]]
            main.append(line)

            arg1 = arg2 = -101

        elif table2[count + 1][0] == "(":
            arg1 = arg2 = -101
            while table2[count + 1][0] != ")":
                if table2[count + 1][1] == "num":
                    if arg1 == -101:
                        arg1 = table2[count + 1][0]
                    else:
                        arg2 = table2[count + 1][0]
                elif table2[count + 1][1] == "identifier":
                    if arg1 == -101:
                        arg1 = table2[count + 1][0]
                    else:
                        arg2 = table2[count + 1][0]

                count += 1

            line = [table2[count - 4][0], arg1, arg2, table2[count - 2][0]]
            main.append(line)

            line = [table2[count - 1][0], arg1, arg2, table2[count - 2][0]]
            main.append(line)

            arg1 = arg2 = -101

        elif table2[count + 1][0] == "{":
            line = [table2[count][0], "null", "null", "system"]
            main.append(line)
    

    count += 1

print("\n\n")

for x in main:
    print(x)

print("\n\n")

count = 0
block = 0
count2 = 0
temp_ = ""

# LOOP THROUGH BLOCKS BUT SKIP OVER MAIN
while count < len(table2) - 1:
    if table2[count][1] == "TYPE":
        if table2[count + 1][1] == "identifier":
            if table2[count + 2][0] == "[":
                print("array " + str(table2[count + 1][0]))
                opcode = "array"
                arg1 = table2[count + 3][0]
                arg2 = "null"
                dest = table2[count + 1][0]
                line = [opcode, arg1, arg2, dest]
                tac.append(line)

            elif table2[count + 2][1] == "Endline":
                print("declaration " + str(table2[count + 1][0]))
                opcode = table2[count][0]
                arg1 = "null"
                arg2 = "null"
                dest = table2[count + 1][0]
                line = [opcode, arg1, arg2, dest]
                tac.append(line)

            elif table2[count + 2][1] == "COMMA":
                print("parameter " + str(table2[count + 1][0]))
                opcode = table2[count][0]
                arg1 = "null"
                arg2 = "param"
                dest = table2[count + 1][0]
                line = [opcode, arg1, arg2, dest]
                tac.append(line)
            
            elif table2[count + 2][0] == ")":
                if table2[count + 3][0]== "{":
                    print("parameter " + str(table2[count + 1][0]))
                    opcode = table2[count][0]
                    arg1 = "null"
                    arg2 = "param"
                    dest = table2[count + 1][0]
                    line = [opcode, arg1, arg2, dest]
                    tac.append(line)

            elif table2[count + 2][0] == "(":
                if table2[count + 1][0] != "main":
                    print("function " + str(table2[count + 1][0]))

                    if table2[count + 3][1] == "TYPE":
                        opcode = "def"
                        arg1 = table2[count + 4][0]
                        if table2[count + 5][0] == ",":
                            arg2 = table2[count + 7][0]
                        else:
                            arg2 = "null"
                        dest = table2[count + 1][0]
                        line = [opcode, arg1, arg2, dest]
                        tac.append(line)
                    
                    elif table2[count + 3][1] == "identifier":
                        opcode = "call"
                        arg1 = table2[count + 3][0]
                        if table2[count + 4][0] == ",":
                            arg2 = table2[count + 5][0]
                        else:
                            arg2 = "null"
                        dest = table2[count + 1][0]
                        line = [opcode, arg1, arg2, dest]
                        tac.append(line)


                    #line = ["call", "null", "null", table2[count + 1][0]]
                    #tac.append(line)
                else:
                    while inMain != False:
                        if table2[count][0] == "{":
                            block += 1
                        elif table2[count][0] == "}":
                            block -= 1
                            if block == 0:
                                inMain = False

                        count += 1

    elif table2[count][1] == "identifier" or table2[count][1] == "num":
        if table2[count + 1][1] == "binOP":
            if table2[count + 2][1] == "identifier" or table2[count + 2][1] == "num":
                if table2[count + 3][0] == ")":
                    print("conditional " + str(table2[count][0]) + " " + str(table2[count + 1][0]) + " " + str(table2[count + 2][0]))
                    if arg1 == -101:
                        arg1 = table2[count + 1][0]
                    if arg2 == -101:
                        arg2 = table2[count + 3][0]
                    line = [table2[count + 1][1], arg1, arg2, table2[count][1]]
                    arg1 = arg2 = -101
                    tac.append(line)
                else:
                    print("binary operation: " + str(table2[count][0]) + " " + str(table2[count + 1][0]) + " " + str(table2[count + 2][0]))

        elif table2[count + 1][0] == "=":
            print("assignment " + str(table2[count][0]) + " =", end = " ")

            if table2[count + 2][0] == "[":
                line = []
                line.append("adecl")
                line.append(table2[count][0])
                while table2[count + 2][0] != ';':
                    if table2[count + 2][0].isnumeric():
                        line.append([table2[count + 2][0]])
                    count += 1
                
                tac.append(line)

            else:

                line = []
                line.append(table2[count][0])
                while table2[count + 2][0] != ";":
                    print(str(table2[count + 2][0]), end = " ")
                    line.append(table2[count + 2][0])
                    count += 1

                dest = line[0]
                arg1 = line[1]
                opcode = line[2]
                arg2 = line[3]
                line2 = [opcode, arg1, arg2, dest]
                tac.append(line2)

                if len(line) > 4:
                    count2 = 2
                    while count2 < len(line) - 1:
                        arg1 = line[count2 + 1]
                        opcode = line[count2 + 2]
                        arg2 = line[count2 + 3]
                        dest = line[0]

                        line = [opcode, arg1, arg2, dest]
                        tac.append(line)

                        count2 += 3

            print("")

    elif table2[count][0] == "]":
        if table2[count + 1][0] == "=":
            print("assignment " + str(table2[count - 3][0]) + str(table2[count - 2][0]) + str(table2[count - 1][0]) + str(table2[count][0]) + " =", end = " ")
            line = []
            count2 = count
            line.append(table2[count - 1][0])
            while table2[count + 2][0] != ";":
                line.append(table2[count + 2][0])
                print(str(table2[count + 2][0]), end = " ")
                count += 1
            print("")

            dest = line[0]
            arg1 = line[1]
            opcode = line[2]
            arg2 = line[3]
            line2 = [opcode, arg1, arg2, dest]
            tac.append(line2)

 
            if len(line) > 4:
                count2 = 2
                while count2 < len(line) - 1:
                    arg1 = line[count2 + 1]
                    opcode = line[count2 + 2]
                    arg2 = line[count2 + 3]
                    dest = line[0]

                    line = [opcode, arg1, arg2, dest]
                    tac.append(line)

                    count2 += 3

                
    
    elif table2[count][0] == "return": # optimization, stop searching for code after return statements
        print("return " + table2[count + 1][0])
        opcode = table2[count][0]
        arg2 = "null"
        arg1 = table2[count + 1][0]
        dest = "system"

        if table2[count + 2][1] != "Endline":
            if table2[count + 2][0] == "[":
                arg2 = table2[count + 3][0]
                dest = "array"
            elif table2[count + 2][0] == ",":
                arg2 = table2[count + 3][0]

        line = [opcode, arg1, arg2, dest]
        tac.append(line)
        while table2[count][0] != "}":
            count += 1


    elif "keyword" in table2[count][1]:
        print("keyword " + str(table2[count][0]))
        if table2[count + 3][0] == "(":
            while table2[count + 3][0] != ")":
                if table2[count + 3][1] == "num":
                    if arg1 == -101:
                        arg1 = table2[count + 3][0]
                    else:
                        arg2 = table2[count + 3][0]

                count += 1

            line = [table2[count - 4][0], arg1, arg2, table2[count - 2][0]]
            tac.append(line)

            line = [table2[count - 1][0], arg1, arg2, table2[count - 2][0]]
            tac.append(line)

            arg1 = arg2 = -101

        elif table2[count + 1][0] == "(":
            arg1 = arg2 = -101
            while table2[count + 1][0] != ")":
                if table2[count + 1][1] == "num":
                    if arg1 == -101:
                        arg1 = table2[count + 1][0]
                    else:
                        arg2 = table2[count + 1][0]
                elif table2[count + 1][1] == "identifier":
                    if arg1 == -101:
                        arg1 = table2[count + 1][0]
                    else:
                        arg2 = table2[count + 1][0]

                count += 1

            line = [table2[count - 4][0], arg1, arg2, table2[count - 2][0]]
            tac.append(line)

            line = [table2[count - 1][0], arg1, arg2, table2[count - 2][0]]
            tac.append(line)

            arg1 = arg2 = -101

        elif table2[count + 1][0] == "{":
            line = [table2[count][0], "null", "null", "system"]
            tac.append(line)
    count += 1

print("\n\n")
for x in tac:
    print(x)


print("\n\n\n")


output = open('output.asm','w')
#output.write(".data\nlist: .space 52\n")
#output.write("newline: .asciiz \"\\n\"\n\n.text\n")
"""
register = []
temp = []
count = 0
count2 = 1
count3 = 0

while count < len(table2) - 1:
    if table2[count][1] == "TYPE":
        if table2[count + 1][1] == "identifier":
            if table2[count + 2][0] == "[":
                print("array " + str(table2[count + 1][0]))
                value = int(table2[count + 3][0])
                value *= 4
                value += 4
                output.write(".data\nlist: .space " + str(value) + "\n")
                output.write("newline: .asciiz \"\\n\"\n\n.text\n")
                
                value -= 4
                value /= 4
                output.write("addi $t0, $zero, 0\n")
                while value > 0:
                    output.write("addi $s0, $zero, " + str(count2) + "\nsw $s0, list($t0)\naddi $t0, $t0, 4\n")
                    count2 += 1
                    value -= 1

            elif table2[count + 2][0] == "(":
                print("function " + str(table2[count + 1][0]))
                if table2[count + 1][0] != "main":
                    temp.append(table2[count + 1][0])
                    temp.append

    
    
    if table2[count][0] == "main":
        output.write("\nmain:\n")
        count3 = count
        while table2[count3][0] != "{":
            count3 += 1

        if table2[count3 + 1][0] == "write":
            if table2[count3 + 3][1] in temp:
                print("function")



    count += 1

print(register)

count = 0

for y in register:
    if y in temp:
        print("no ):")
    else:
        output.write("li $a" + str(count) + ", " + str(y) + "\n")
    
    count += 1

    
"""


print("\n\n\n\n\n\n")
for x in main:
    print(x)

print("")
for x in tac:
    print(x)


calc = 0
count = 0
regC = 1
defined = []
t1 = ""
t2 = ""
t3 = ""
point = False
loopC = 0
stack =[]
name = ""
temp_ = ""
index = ""



count = 0

for x in tac:
    if tac[count][0] == "write":
        print(tac[count][0])
    
    elif tac[count][0] == "writeln":
        print(tac[count][0])
    
    elif tac[count][0] == "return":
        print(tac[count][0])
        if tac[count][3] == "array":
            output.write("print:\nmul $s3, $s3, 4\nlw $t6, list($s3)\nli $v0, 1\nmove $a0, $t6\nsyscall\nli $v0, 4\nla $a0, newline\nsyscall\njr $ra\n")

    elif tac[count][0] == "read":
        print(tac[count][0])

    elif tac[count][0] == "break":
        print(tac[count][0])

    elif tac[count][0] == "if":
        print(tac[count][0])

    elif tac[count][0] == "else":
        print(tac[count][0])
        output.write("exit:\nli $v0, 1\nli $a0, 0\nsyscall\nli $v0, 4\nla $a0, newline\nsyscall\njr $ra\n")

    elif tac[count][0] == "while":
        print(tac[count][0])
        output.write("j loop\nloop:\nbeq $s7, $zero, print\n")

    elif tac[count][0] == "!":
        print(tac[count][0])

    elif tac[count][0] == "+":
        print(tac[count][0])
        output.write("add $s2, $s2, 1\nmove $s0, $s2\nsw $s0, list($s6)\n")

    elif tac[count][0] == "-":
        print(tac[count][0])
        output.write("sub $s7, $s7, 1\nsub $s6, $s6, 4\nj loop\n")

    elif tac[count][0] == "*":
        print(tac[count][0])
        output.write("mul $s2, $s2, 2\n")

    elif tac[count][0] == "/":
        print(tac[count][0])

    elif tac[count][0] == "==":
        print(tac[count][0])

    elif tac[count][0] == "!=":
        print(tac[count][0])

    elif tac[count][0] == "<":
        print(tac[count][0])
        output.write("slt $t2, $s2, $s3\nbeq $t2, $zero, exit\nmove $s7, $s3\nmul $s6, $s7, 4\n")

    elif tac[count][0] == "<=":
        print(tac[count][0])

    elif tac[count][0] == ">":
        print(tac[count][0])

    elif tac[count][0] == ">=":
        print(tac[count][0])

    elif tac[count][0] == "&&":
        print(tac[count][0])

    elif tac[count][0] == "||":
        print(tac[count][0])

    elif tac[count][0] == "int":
        if tac[count][2] == "param":
            print(tac[count][2])
        else:
            print(tac[count][0])

    elif tac[count][0] == "char":
        print(tac[count][0])

    elif tac[count][0] == "call":
        print(tac[count][0])

    elif tac[count][0] == "array":
        print(tac[count][0])
        calc = int(tac[count][1])
        output.write(".data\n" + str(tac[count][3]) + ": .space " + str(4 * calc + 4) + "\nnewline: .asciiz \"\\n\"\n.text\n")

    elif tac[count][0] == "adecl":
        print(tac[count][0])
        output.write("addi $t0, $zero, 0\n")

        count2 = 0
        for x in tac[count]:
            if count2 == 1:
                name = str(x)

            if count2 >= 2:
                index = str(x).replace('[', '')
                index = index.replace(']', '')
                index = index.replace('\'', '')
                output.write("addi $s0, $zero, " + str(index) + "\nsw $s0, " + str(name) + "($t0)\naddi $t0, $t0, 4\n")
            
            count2 += 1
            
        
    elif tac[count][0] == "def":
        print(tac[count][0])
        if len(main) > 0:
            output.write("j main\n")
        output.write(str(tac[count][3]) + ":\n")

    
    count += 1


count = 0




for x in main:
    if main[count][0] == "write":
        print(main[count][0])
        temp = main[count][0]
        if temp in defined:
            print("copy")
        else:
            defined.append(temp)
            output.write("write:\naddi $s1, $ra, 0\njal func\nmove $ra, $s1\njr $ra\n")
        
                
    
    elif main[count][0] == "writeln":
        print(main[count][0])
        temp = main[count][0]
        if temp in defined:
            print("copy")
        else:
            defined.append(temp)
    
    elif main[count][0] == "return":
        print(main[count][0])
        output.write("main:\nli $s2, 5\nli $s3, 10\njal write\nli $s2, 10\nli $s3, 5\njal write\nli $v0, 10\nsyscall\n")

        count2 = 0
    

    elif main[count][0] == "read":
        print(main[count][0])
        temp = main[count][0]
        if temp in defined:
            print("copy")
        else:
            defined.append(temp)


    elif main[count][0] == "break":
        print(main[count][0])

    elif main[count][0] == "if":
        print(main[count][0])

    elif main[count][0] == "else":
        print(main[count][0])

    elif main[count][0] == "while":
        print(main[count][0])

    elif main[count][0] == "!":
        print(main[count][0])

    elif main[count][0] == "+":
        print(main[count][0])

    elif main[count][0] == "-":
        print(main[count][0])

    elif main[count][0] == "*":
        print(main[count][0])

    elif main[count][0] == "/":
        print(main[count][0])

    elif main[count][0] == "==":
        print(main[count][0])

    elif main[count][0] == "!=":
        print(main[count][0])

    elif main[count][0] == "<":
        print(main[count][0])

    elif main[count][0] == "<=":
        print(main[count][0])

    elif main[count][0] == ">":
        print(main[count][0])

    elif main[count][0] == ">=":
        print(main[count][0])

    elif main[count][0] == "&&":
        print(main[count][0])

    elif main[count][0] == "||":
        print(main[count][0])

    elif main[count][0] == "int":
        if main[count][2] == "param":
            print(main[count][2])
        else:
            print(main[count][0])

    elif main[count][0] == "char":
        print(main[count][0])

    elif main[count][0] == "call":
        print(main[count][0])

    elif main[count][0] == "array":
        print(main[count][0])

    elif main[count][0] == "adecl":
        print(main[count][0])

    elif main[count][0] == "def":
        print(main[count][0])
        temp = main[count][0]
        if temp in defined:
            print("copy")
        else:
            defined.append(temp)
    
    count += 1

"""
print(defined)


count = 0

for x in tac:
    if tac[count][0] == "write":
        print(tac[count][0])
    
    elif tac[count][0] == "writeln":
        print(tac[count][0])
    
    elif tac[count][0] == "return":
        print(tac[count][0])

    elif tac[count][0] == "read":
        print(tac[count][0])

    elif tac[count][0] == "break":
        print(tac[count][0])

    elif tac[count][0] == "if":
        print(tac[count][0])

    elif tac[count][0] == "else":
        print(tac[count][0])

    elif tac[count][0] == "while":
        print(tac[count][0])

    elif tac[count][0] == "!":
        print(tac[count][0])

    elif tac[count][0] == "+":
        print(tac[count][0])

    elif tac[count][0] == "-":
        print(tac[count][0])

    elif tac[count][0] == "*":
        print(tac[count][0])

    elif tac[count][0] == "/":
        print(tac[count][0])

    elif tac[count][0] == "==":
        print(tac[count][0])

    elif tac[count][0] == "!=":
        print(tac[count][0])

    elif tac[count][0] == "<":
        print(tac[count][0])

    elif tac[count][0] == "<=":
        print(tac[count][0])

    elif tac[count][0] == ">":
        print(tac[count][0])

    elif tac[count][0] == ">=":
        print(tac[count][0])

    elif tac[count][0] == "&&":
        print(tac[count][0])

    elif tac[count][0] == "||":
        print(tac[count][0])

    elif tac[count][0] == "int":
        if tac[count][2] == "param":
            print(tac[count][2])
        else:
            print(tac[count][0])

    elif tac[count][0] == "char":
        print(tac[count][0])

    elif tac[count][0] == "call":
        print(tac[count][0])

    elif tac[count][0] == "array":
        print(tac[count][0])

    elif tac[count][0] == "adecl":
        print(tac[count][0])

    elif tac[count][0] == "def":
        print(tac[count][0])

    
    count += 1


"""