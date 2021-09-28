from pptree import *

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

c2 = 0

class SymbolTable:
    def __init__(self):
        self.symbolRow = []
        self.symbolColumn = []

        self.children = []

    def insert(self, name, type, scope):
        self.name = name
        self.type = type_
        self.scope = scope

        self.symbolRow = [name, type_, scope]
        self.symbolColumn.append(self.symbolRow)

    def createNode(self, obj):
        self.children.append(obj)

    def printNode(self):
        x = 0
        while x < len(self.children):
            print(self.children[x])
            x += 1

    def print(self):
        print(self.symbolColumn)

new = SymbolTable()
symbolTableRow = []
symbolTableColumn = []

count = scope = scope2 = 0

for x in table2:
    name = table2[count][0]
    type_ = table2[count][1]

    if count + 1 < len(table2):
        type2 = "identifier"
        name2 = table2[count + 1][0]

    if type_ == "oBRACE":

        scope += 1
    
    elif type_ == "cBRACE":
        scope -= 1
    
    else:
        if type_ == "TYPE":
            #print(type_)
            #print(type2)

            if count + 1 < len(table2):
                if type2 == "identifier":  
                    #print(type_)
                    #print(type2)
                    new.insert(name, type_, scope)
                    new.insert(name2, type2, scope)

                    if table2[count - 1][1] == "oParenthesis":
                        scope2 = scope + 1
                    elif table2[count + 2][1] == "cParenthesis":
                        #print(name2)
                        scope2 = scope + 1
                    else:
                        scope2 = scope

                    symbolTableRow = [name, type_, scope2]
                    symbolTableColumn.append(symbolTableRow)
                    
                    symbolTableRow = [name2, type2, scope2]
                    symbolTableColumn.append(symbolTableRow)


    count += 1


#new.insert(name, type_, scope)
#new.print()
#new.printNode()

count = 0

final1 = []
final = []



program_ = Node("Global")


for x in symbolTableColumn:
    if symbolTableColumn[count][1] == "TYPE":
        final1 = [symbolTableColumn[count][0], symbolTableColumn[count + 1][0], symbolTableColumn[count][2]]
        final.append(final1)

     

    count += 1

#print(final)
count = 0
#print(final[1])

scope = lastScope = 0

for x in final:
    scope = final[count][2]

    if count - 1 != -1:
        lastScope = final[count - 1][2]

    if scope == 0:
        string_ = str(final[count][0]) + " " + str(final[count][1]) + " (scope: " + str(final[count][2]) + ")"
        new2_ = Node(string_, program_)

    elif scope == lastScope:
        string_ = str(final[count][0]) + " " + str(final[count][1]) + " (scope: " + str(final[count][2]) + ")"
        new_ = Node(string_, new_)
        print()

    elif scope > lastScope:
        string_ = str(final[count][0]) + " " + str(final[count][1]) + " (scope: " + str(final[count][2]) + ")"
        new_ = Node(string_, new2_)
        print()

    count += 1


print_tree(program_, horizontal = False)
print("\n")



count = 0
for x in table2:
    #print(table2[count])
    count += 1

AST = Node("AST")

count = 0

for x in table2:
    if count >= len(table2):
        break

    if table2[count][1] == "binOP":
        binop_ = Node(table[count][0], AST)
        if table2[count - 1][0] == "]":
            new_ = Node(table2[count - 2][0], binop_)
        else:
            new_ = Node(table2[count - 1][0], binop_)
        #new2_ = Node(table2[count + 1][0], binop_)

        count2 = count
        next_ = True
        isOperator = False
        countOperator = 0
        opIndex = []

        while next_:
            #print(table2[count2 + 1][0])
            if table2[count2 + 1][0] == ";":
                next_ = False
            elif table2[count2 + 1][0] == ")":
                next_ = False
            else:
                if table2[count2 + 1][1] == "binOP":
                    isOperator = True
                    countOperator += 1
                    opIndex.append(count2 + 1)
                    #new2_ = Node(table2[count2 + 1][0], binop_)
                    #new3_ = Node(table2[count2][0], new2_)
                    #new4_ = Node(table2[count2 + 2][0], new2_)

                elif table2[count2 + 1][1] == "equals":
                    isOperator = True
                    countOperator += 1
                    opIndex.append(count2 + 1)
                    #new2_ = Node(table2[count2 + 1][0], binop_)
                    #new3_ = Node(table2[count2][0], new2_)
                    #new4_ = Node(table2[count2 + 2][0], new2_)

                #print(isOperator)
                #print(countOperator)
                count2 += 1

            
        #print(countOperator)
        if countOperator == 1:
            new2_ = Node(table2[opIndex[0]][0], binop_)
            new3_ = Node(table2[opIndex[0] - 1][0], new2_)
            new4_ = Node(table2[opIndex[0] + 1][0], new2_)
        
        
        #print(opIndex)

        if isOperator == False:
            new2_ = Node(table2[count + 1][0], binop_)
            count += 1
        else:
            count = count2 + 1

    if table2[count][1] == "equals":
        binop_ = Node(table[count][0], AST)
        if table2[count - 1][0] == "]":
            new_ = Node(table2[count - 2][0], binop_)
        else:
            new_ = Node(table2[count - 1][0], binop_)
        #new2_ = Node(table2[count + 1][0], binop_)

        count2 = count
        next_ = True
        isOperator = False
        countOperator = 0
        opIndex = []

        while next_:
            #print(table2[count2 + 1][0])
            if table2[count2 + 1][0] == ";":
                next_ = False
            elif table2[count2 + 1][0] == ")":
                next_ = False
            else:
                if table2[count2 + 1][1] == "binOP":
                    isOperator = True
                    countOperator += 1
                    opIndex.append(count2 + 1)
                    #new2_ = Node(table2[count2 + 1][0], binop_)
                    #new3_ = Node(table2[count2][0], new2_)
                    #new4_ = Node(table2[count2 + 2][0], new2_)

                elif table2[count2 + 1][1] == "equals":
                    isOperator = True
                    countOperator += 1
                    opIndex.append(count2 + 1)
                    #new2_ = Node(table2[count2 + 1][0], binop_)
                    #new3_ = Node(table2[count2][0], new2_)
                    #new4_ = Node(table2[count2 + 2][0], new2_)

                #print(isOperator)
                #print(countOperator)
                count2 += 1

        #print(countOperator)
        if countOperator == 1:
            new2_ = Node(table2[opIndex[0]][0], binop_)
            new3_ = Node(table2[opIndex[0] - 1][0], new2_)
            new4_ = Node(table2[opIndex[0] + 1][0], new2_)

        elif countOperator > 1:
            c3 = 0
            new2_ = Node(table2[opIndex[c3]][0], binop_)
            new3_ = Node(table2[opIndex[c3] - 1][0], new2_)
            new4_ = Node(table2[opIndex[c3] + 2][0], new2_)
            new5_ = Node(table2[opIndex[c3] + 1][0], new4_)
            new6_ = Node(table2[opIndex[c3] + 3][0], new4_)

                

        if isOperator == False:
            new2_ = Node(table2[count + 1][0], binop_)
            count += 1
        else:
            count = count2 + 1

    

        

    count += 1


print_tree(AST, horizontal = False)


