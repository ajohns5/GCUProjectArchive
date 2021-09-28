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
for x in table2:
    #print(table2[c2])
    c2 += 1

"""
                            Type    ID    ;     ,     [     {     char    int    num    (     2UnaryOp     return     read       write      writeln     break     if    while     BinOp     equals     )     ]     }     $
                            0       1     2     3     4     5      6       7      8     9        10          11        12         13          14         15       16     17        18        19       20    21    22    23

program             : 0  | Type      : 0
VarDeclList         : 1  | ID        : 1
VarDecl             : 2  | ;         : 2
VarDecl'            : 3  | ,         : 3
FunDeclList         : 4  | [         : 4
FunDeclList'        : 5  | {         : 5
FunDecl             : 6  | char      : 6
ParamDeclList       : 7  | int       : 7
ParamDeclListTail   : 8  | num       : 8
ParamDeclListTail'  : 9  | (         : 9
ParamDecl           : 10 | 2UnaryOp  : 10
ParamDecl'          : 11 | return    : 11
Block               : 12 | read      : 12
Type                : 13 | write     : 13
StmtList            : 14 | writeln   : 14
StmtList'           : 15 | break     : 15
Stmt                : 16 | if        : 16
Astmt               : 17 | while     : 17
Expr                : 18 | BinOp     : 18
Expr1               : 19 | equals    : 19
Expr2               : 20 | )         : 20
Primary             : 21 | ]         : 21
Expr3               : 22 | }         : 22
ExprList            : 23 | $         : 23
ExprListTail        : 24 | 
ExprListTail'       : 25 | 

"""
stack = ["$", "program"]

c3 = 0
terminal = False
    
print("")

while c3 < len(table2):
    token = table2[c3][1]
    #print(table2[c3][0])
    print("current token " + str(c3) + ", final token " + str(len(table2)))
        
    x = len(stack) - 1

    if terminal:
        if token != "identifier" or "Endline" or "COMMA" or "oBracket" or "oBRACE" or "CHAR" or "INT" or "oParenthesis" or "unOP" or "keywordreturn" or "keywordread" or "keywordwrite" or "keywordwriteln" or "keywordbreak" or "keywordif" or "keywordwhile" or "binOP" or "cParenthesis" or "cBracket" or "cBRACE":
            terminal = False

    if stack[x] == "program":

        if token != "TYPE":
            if terminal == False:
                print("syntax error line " + str(table2[c3][2]))
                break

        elif terminal:
            stack.pop()
            x -= 1

        else:
            stack.pop()
            x -= 1

            program_ = Node("Program")

            if table2[c3 + 2][1] != "Parenthesis":
                terminal = False

                vardecllist_ = Node("VarDeclList", program_)
                stack.append("fundecllist")
                fundecllist_ = Node("FunDeclList", program_)
                x += 1

                stack.append("vardecllist")
                x += 1

            else:
                terminal = False
                stack.append("fundecllist")
                fundecllist_ = Node("FunDeclList", program_)
                x += 1


    elif stack[x] == "vardecllist":

        if token != "TYPE":
            if terminal == False:
                if token == "identifier" or "Endline" or "COMMA" or "oBracket" or "oBRACE" or "CHAR" or "INT" or "oParenthesis" or "unOP" or "keywordreturn" or "keywordread" or "keywordwrite" or "keywordwriteln" or "keywordbreak" or "keywordif" or "keywordwhile" or "binOP" or "cParenthesis" or "cBracket" or "cBRACE":
                    stack.pop()
                    x -= 1

                else:
                    print("syntax error line " + str(table2[c3][2]))
                    break
        
        elif terminal:
            stack.pop()
            x -= 1

        else:
            terminal = False
            stack.pop()
            x -= 1

            if table2[c3 + 2][1] != "oParenthesis":
                vardecllist2_ = Node("VarDeclList", vardecllist_)
                vardecl_ = Node("VarDecl", vardecllist_)

                stack.append("vardecllist")
                stack.append("vardecl")
                x += 2

            else:
                if stack[x] != "fundecllist":
                    stack.pop()

    elif stack[x] == "fundecllist":

        if token != "TYPE":
            if terminal == False:
                print("syntax error line " + str(table2[c3][2]))
                break

        elif terminal:
            stack.pop()
            x -= 1

        else:
            terminal = False
            stack.pop()
            x -= 1

            fundecllist1_ = Node("FunDeclList'", fundecllist_)
            fundecl_ = Node("FunDecl", fundecllist_)
            stack.append("fundecllist1")
            stack.append("fundecl")
            x += 2

    elif stack[x] == "fundecllist1":

        if token == "$":
            terminal = False
            print("done")
            break

        elif token == "TYPE":
            terminal = False
            stack.pop()
            x -= 1
            fundecllist_ = Node("FunDeclList", fundecllist1_)
            stack.append("fundecllist")
            x += 1
        
        elif terminal:
            stack.pop()
            x -= 1

        elif terminal == False:
            print("syntax error on line " + str(table2[c3][2]))
            break
            

    elif stack[x] == "vardecl":

        if token != "TYPE":
            if terminal == False:
                print("syntax error line " + str(table2[c3][2]))
                break

        elif terminal:
            stack.pop()
            x -= 1

        else:
            terminal = False
            stack.pop()
            x -= 1

            if table2[c3 + 2][1] != "oParenthesis":
                type_ = Node("Type", vardecl_)
                identifier_  = Node("Identifier", vardecl_)

                vardecl1_ = Node("VarDecl'", vardecl_)

                stack.append("vardecl1")
                stack.append("identifier")
                stack.append("type")
                x += 3

            else:
                stack.pop()

    elif stack[x] == "vardecl1":

        if token == "Endline":
            terminal = False
            stack.pop()
            x -= 1

            endline_ = Node("Endline", vardecl1_)
            stack.append(";")
            x += 1

        elif token == "oBracket":
            terminal = False
            stack.pop()
            x -= 1

            endline2_ = Node("Endline", vardecl1_)
            cbracket_ = Node("Closed Brace", vardecl1_)

            obracket_ = Node("Open Brace", vardecl1_)
            num_ = Node("Num", vardecl1_)

            stack.append(";")
            stack.append("]")
            stack.append("num")
            stack.append("[")
            x += 4

        elif terminal:
            stack.pop()
            x -= 1

        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))
            break


    elif stack[x] == "fundecl":

        if token != "TYPE":
            if terminal == False:
                print("syntax error line " + str(table2[c3][2]))
                break

        elif terminal:
            stack.pop()
            x -= 1

        else:
            terminal = False
            stack.pop()
            x -= 1

            type_ = Node("Type", fundecl_)
            identifier_ = Node("Identifier", fundecl_)
            oParenthesis_ = Node("Open Parenthesis", fundecl_)
            paramdecllist_ = Node("ParamDeclList", fundecl_)
            cParenthesis_ = Node("Closed Parenthesis", fundecl_)
            block_ = Node("Block", fundecl_)


            stack.append("block")
            stack.append(")")
            stack.append("paramdecllist")
            stack.append("(")
            stack.append("identifier")
            stack.append("type")
            x += 6

    elif stack[x] == "paramdecllist":

        if token == "TYPE":
            terminal = False
            stack.pop()
            x -= 1
            
            paramdecllisttail_ = Node("ParamDeclListTail", paramdecllist_)
            stack.append("paramdecllisttail")
            x += 1

        elif token == "oParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1
        
        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))
            break

        elif terminal:
            stack.pop()
            x -= 1

    elif stack[x] == "paramdecllisttail":

        if token != "TYPE":
            if terminal == False:
                print("syntax error line " + str(table2[c3][2]))
                break

        elif terminal:
            stack.pop()
            x -= 1
        
        else:
            terminal = False
            stack.pop()
            x -= 1

            paramdecllisttail1_ = Node("ParamDeclListTail'", paramdecllisttail_)
            paramdecl_ = Node("ParamDecl", paramdecllisttail_)

            stack.append("paramdecllisttail1")
            stack.append("paramdecl")
            x += 2

    elif stack[x] == "paramdecllisttail1":
        if token == "COMMA":
            terminal = False
            #if stack[x] == "paramdecllisttail1":
            stack.pop()
            x -= 1

            paramdecllisttail_ = Node("ParamDeclListTail", paramdecllisttail1_)
            comma_ = Node("Comma", paramdecllisttail1_)

            stack.append("paramdecllisttail")
            stack.append(",")
            x += 2

        elif token == "cParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1
        
        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))

        elif terminal:
            stack.pop()
            x -= 1

    elif stack[x] == "paramdecl":

        if token != "TYPE":
            if terminal == False:
                print("syntax error line " + str(table2[c3][2]))
                break

        elif terminal:
            stack.pop()
            x -= 1

        else:
            terminal = False
            stack.pop()
            x -= 1

            paramdecl1_ = Node("ParamDecl'", paramdecl_)
            identifier_ = Node("Identifier", paramdecl_)
            type_ = Node("Type", paramdecl_)

            stack.append("paramdecl1")
            stack.append("identifier")
            stack.append("type")
            x += 3

    elif stack[x] == "paramdecl1":

        if token == "COMMA":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif token == "oBracket":
            terminal = False
            stack.pop()
            x -= 1

            oBracket_ = Node("Open Brace", paramdecl1_)
            cBracket_ = Node("Closed Brace", paramdecl1_)

            stack.append("]")
            stack.append("[")
            x += 2

        elif token == "cParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))
            break

        elif terminal:
            stack.pop()
            x -= 1

    elif stack[x] == "block":

        if token != "oBRACE":
            if terminal == False:
                print("syntax error line " + str(table2[c3][2]))
                break

        elif terminal:
            stack.pop()
            x -= 1

        else:
            terminal = False
            stack.pop()
            x -= 1

            oBrace = Node("Open Block", paramdecl1_)
            stmtlist_ = Node("StmtList", paramdecl1_)
            vardecllist_ = Node("VarDeclList", paramdecl1_)
            cBrace = Node("Close Block", paramdecl1_)

            stack.append("}")
            stack.append("vardecllist")
            stack.append("stmtlist")
            stack.append("{")
            x += 4

    elif stack[x] == "type":
        if token == "CHAR":
            terminal = False
            stack.pop()
            x -= 1

            type_ = Node("Char", identifier_)
            stack.append("char")
            x += 1

        elif token == "INT":
            terminal = False
            stack.pop()
            x -= 1

            type_ = Node("Int", identifier_)
            stack.append("int")
            x += 1

        elif token == "TYPE":
            terminal = False
            stack.pop()
            x -= 1

            int_ = Node("int", type_)
            stack.append("int")
            x += 1

        elif terminal:
            stack.pop()
            x -= 1

        elif token == "identifier" or "Endline" or "COMMA" or "oBracket" or "oBRACE" or "CHAR" or "INT" or "oParenthesis" or "unOP" or "keywordreturn" or "keywordread" or "keywordwrite" or "keywordwriteln" or "keywordbreak" or "keywordif" or "keywordwhile" or "binOP" or "cParenthesis" or "cBracket" or "cBRACE":
            stack.pop()
            x -= 1

        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))
            break

    elif stack[x] == "stmtlist":

        if token == "identifier":
            terminal = False
            stack.pop()
            x -= 1

            stmt_ = Node("Stmt", stmtlist_)
            stmtlist1_ = Node("StmtList'", stmtlist_)

            stack.append("stmtlist1")
            stack.append("stmt")
            x += 2

        elif token == "Endline":
            terminal = False
            stack.pop()
            x -= 1

            stmt_ = Node("Stmt", stmtlist_)
            stmtlist1_ = Node("StmtList'", stmtlist_)

            stack.append("stmtlist1")
            stack.append("stmt")
            x += 2

        elif token == "oBRACE":
            terminal = False
            stack.pop()
            x -= 1

            stmt_ = Node("Stmt", stmtlist_)
            stmtlist1_ = Node("StmtList'", stmtlist_)

            stack.append("stmtlist1")
            stack.append("stmt")
            x += 2

        elif token == "num":
            terminal = False
            stack.pop()
            x -= 1

            stmt_ = Node("Stmt", stmtlist_)
            stmtlist1_ = Node("StmtList'", stmtlist_)

            stack.append("stmtlist1")
            stack.append("stmt")
            x += 2

        elif token == "oParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            stmt_ = Node("Stmt", stmtlist_)
            stmtlist1_ = Node("StmtList'", stmtlist_)

            stack.append("stmtlist1")
            stack.append("stmt")
            x += 2

        elif token == "unOP":
            terminal = False
            stack.pop()
            x -= 1

            stmt_ = Node("Stmt", stmtlist_)
            stmtlist1_ = Node("StmtList'", stmtlist_)

            stack.append("stmtlist1")
            stack.append("stmt")
            x += 2

        elif token == "keywordreturn":
            terminal = False
            stack.pop()
            x -= 1

            stmt_ = Node("Stmt", stmtlist_)
            stmtlist1_ = Node("StmtList'", stmtlist_)

            stack.append("stmtlist1")
            stack.append("stmt")
            x += 2

        elif token == "keywordread":
            terminal = False
            stack.pop()
            x -= 1

            stmt_ = Node("Stmt", stmtlist_)
            stmtlist1_ = Node("StmtList'", stmtlist_)

            stack.append("stmtlist1")
            stack.append("stmt")
            x += 2

        elif token == "keywordwrite":
            terminal = False
            stack.pop()
            x -= 1

            stmt_ = Node("Stmt", stmtlist_)
            stmtlist1_ = Node("StmtList'", stmtlist_)

            stack.append("stmtlist1")
            stack.append("stmt")
            x += 2

        elif token == "keywordwriteln":
            terminal = False
            stack.pop()
            x -= 1

            stmt_ = Node("Stmt", stmtlist_)
            stmtlist1_ = Node("StmtList'", stmtlist_)

            stack.append("stmtlist1")
            stack.append("stmt")
            x += 2

        elif token == "keywordbreak":
            terminal = False
            stack.pop()
            x -= 1

            stmt_ = Node("Stmt", stmtlist_)
            stmtlist1_ = Node("StmtList'", stmtlist_)

            stack.append("stmtlist1")
            stack.append("stmt")
            x += 2

        elif token == "keywordif":
            terminal = False
            stack.pop()
            x -= 1

            stack.append("stmtlist1")
            stack.append("stmt")
            x += 2

            stmt_ = Node("Stmt", stmtlist_)
            stmtlist1_ = Node("StmtList'", stmtlist_)

        elif token == "keywordwhile":
            terminal = False
            stack.pop()
            x -= 1

            stmt_ = Node("Stmt", stmtlist_)
            stmtlist1_ = Node("StmtList'", stmtlist_)

            stack.append("stmtlist1")
            stack.append("stmt")
            x += 2

        elif terminal:
            stack.pop()
            x -= 1

        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))
            break

    elif stack[x] == "stmtlist1":
        if token == "identifier":
            terminal = False
            stack.pop()
            x -= 1

            stmtlist_ = Node("StmtList", stmtlist1_)
            
            stack.append("stmtlist")
            x += 1

        elif token == "Endline":
            terminal = False
            stack.pop()
            x -= 1

            tmtlist_ = Node("StmtList", stmtlist1_)

            stack.append("stmtlist")
            x += 1

        elif token == "oBRACE":
            terminal = False
            stack.pop()
            x -= 1

            tmtlist_ = Node("StmtList", stmtlist1_)

            stack.append("stmtlist")
            x += 1

        elif token == "num":
            terminal = False
            stack.pop()
            x -= 1

            tmtlist_ = Node("StmtList", stmtlist1_)

            stack.append("stmtlist")
            x += 1

        elif token == "oParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            tmtlist_ = Node("StmtList", stmtlist1_)

            stack.append("stmtlist")
            x += 1

        elif token == "unOP":
            terminal = False
            stack.pop()
            x -= 1

            tmtlist_ = Node("StmtList", stmtlist1_)

            stack.append("stmtlist")
            x += 1

        elif token == "keywordreturn":
            terminal = False
            stack.pop()
            x -= 1

            tmtlist_ = Node("StmtList", stmtlist1_)

            stack.append("stmtlist")
            x += 1

        elif token == "keywordread":
            terminal = False
            stack.pop()
            x -= 1

            tmtlist_ = Node("StmtList", stmtlist1_)

            stack.append("stmtlist")
            x += 1

        elif token == "keywordwrite":
            terminal = False
            stack.pop()
            x -= 1

            tmtlist_ = Node("StmtList", stmtlist1_)

            stack.append("stmtlist")
            x += 1

        elif token == "keywordwriteln":
            terminal = False
            stack.pop()
            x -= 1

            tmtlist_ = Node("StmtList", stmtlist1_)

            stack.append("stmtlist")
            x += 1

        elif token == "keywordbreak":
            terminal = False
            stack.pop()
            x -= 1

            tmtlist_ = Node("StmtList", stmtlist1_)

            stack.append("stmtlist")
            x += 1

        elif token == "keywordif":
            terminal = False
            stack.pop()
            x -= 1

            tmtlist_ = Node("StmtList", stmtlist1_)

            stack.append("stmtlist")
            x += 1

        elif token == "keywordwhile":
            terminal = False
            stack.pop()
            x -= 1

            tmtlist_ = Node("StmtList", stmtlist1_)

            stack.append("stmtlist")
            x += 1

        elif token == "cBRACE":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif terminal:
            stack.pop()
            x -= 1

        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))
            break


    elif stack[x] == "stmt":

        if token == "identifier":
            terminal = False
            stack.pop()
            x -= 1

            astmt_ = Node("Astmt", stmt_)
            endline_ = Node("Endline", stmt_)

            stack.append(";")
            stack.append("astmt")
            x += 1

        elif token == "Endline":
            terminal = False
            stack.pop()
            x -= 1

            endline_ = Node("Endline", stmt_)

            stack.append(";")
            x += 1

        elif token == "oBRACE":
            terminal = False
            stack.pop()
            x -= 1

            block_ = Node("Block", stmt_)

            stack.append("block")
            x += 1

        elif token == "num":
            terminal = False
            stack.pop()
            x -= 1

            astmt_ = Node("Astmt", stmt_)
            endline_ = Node("Endline", stmt_)

            stack.append(";")
            stack.append("astmt")
            x += 2

        elif token == "oParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            expr_ = Node("Expr", stmt_)
            
            stack.append("expr")
            x += 1

        elif token == "unOP":
            terminal = False
            stack.pop()
            x -= 1

            expr_ = Node("Expr", stmt_)

            stack.append("expr")
            x += 1

        elif token == "keywordreturn":
            terminal = False
            stack.pop()
            x -= 1

            return_ = Node("Return", stmt_)
            expr_ = Node("Expr", stmt_)
            endline_ = Node("Endline", stmt_)

            stack.append(";")
            stack.append("expr")
            stack.append("return")
            x += 3

        elif token == "keywordread":
            terminal = False
            stack.pop()
            x -= 1

            read_ = Node("Read", stmt_)
            identifier_ = Node("Identifier", stmt_)
            endline_ = Node("Endline", stmt_)

            stack.append(";")
            stack.append("identifier")
            stack.append("read")
            x += 3

        elif token == "keywordwrite":
            terminal = False
            stack.pop()
            x -= 1

            while_ = Node("While", stmt_)
            expr_ = Node("Expr", stmt_)
            endline_ = Node("Endline", stmt_)

            stack.append(";")
            stack.append("expr")
            stack.append("write")
            x += 3

        elif token == "keywordwriteln":
            terminal = False
            stack.pop()
            x -= 1

            writeln_ = Node("WriteLn", stmt_)
            endline_ = Node("Endline", stmt_)

            stack.append(";")
            stack.append("writeln")
            x += 2

        elif token == "keywordbreak":
            terminal = False
            stack.pop()
            x -= 1

            break_ = Node("Break", stmt_)
            endline_ = Node("Endline", stmt_)

            stack.append(";")
            stack.append("break")
            x += 2

        elif token == "keywordif":
            terminal = False
            stack.pop()
            x -= 1

            if_ = Node("If", stmt_)
            oParenthesis_ = Node("Open Parenthesis", stmt_)
            expr_ = Node("Expr", stmt_)
            cParenthesis_ = Node("Closed Parenthesis", stmt_)
            stmt2_ = Node("Stmt", stmt_)
            else_ = Node("Else", stmt_)
            stmt3_ = Node("Stmt", stmt_)

            stack.append("stmt")
            stack.append("else")
            stack.append("stmt")
            stack.append(")")
            stack.append("expr")
            stack.append("(")
            stack.append("if")
            x += 7

        elif token == "keywordwhile":
            terminal = False
            stack.pop()
            x -= 1

            while_ = Node("While", stmt_)
            oParenthesis_ = Node("Open Parenthesis", stmt_)
            expr_ = Node("Expr", stmt_)
            cParenthesis_ = Node("Closed Parenthesis", stmt_)
            stmt2_ = Node("Stmt", stmt_)

            stack.append("stmt")
            stack.append(")")
            stack.append("expr")
            stack.append("(")
            stack.append("while")
            x += 5

        elif terminal:
            stack.pop()
            x -= 1

        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))
            break

    elif stack[x] == "astmt":

        if token != "identifier":
            if terminal == False:
                print("syntax error line " + str(table2[c3][2]))
                break

        elif terminal:
            stack.pop()
            x -= 1

        else:
            terminal = False
            stack.pop()
            x -= 1

            identifier_ = Node("Identifier", astmt_)
            expr2_ = Node("Expr2", astmt_)

            stack.append("expr2")
            stack.append("identifier")
            x += 2

    elif stack[x] == "expr":
        if token == "identifier":
            terminal = False
            stack.pop()
            x -= 1

            expr1_ = Node("Expr1", expr_)
            primary_ = Node("Primary", expr_)

            stack.append("expr1")
            stack.append("primary")
            x += 2

        elif token == "num":
            terminal = False
            stack.pop()
            x -= 1

            expr1_ = Node("Expr1", expr_)
            primary_ = Node("Primary", expr_)

            stack.append("expr1")
            stack.append("primary")
            x += 2

        elif token == "oParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            expr1_ = Node("Expr1", expr_)
            primary_ = Node("Primary", expr_)

            stack.append("expr1")
            stack.append("primary")
            x += 2

        elif token == "unOP":
            terminal = False
            stack.pop()
            x -= 1

            unop_ = Node("Unary Operator", expr_)
            exprr_ = Node("Expr", expr_)
            expr1 = Node("Expr1", expr_)


            stack.append("expr1")
            stack.append("expr")
            stack.append("unop")
            x += 3

        elif terminal:
            stack.pop()
            x -= 1

        elif terminal == False: 
            print("syntax error line " + str(table2[c3][2]))
            break

    elif stack[x] == "expr1":

        if token == "identifier":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif token == "Endline":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif token == "COMMA":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif token == "num":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif token == "unOP":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif token == "binOP":
            terminal = False
            stack.pop()
            x -= 1

            binop_ = Node("Binary Operator", expr1_)
            expr_ = Node("Expr", expr1_)
            exprr1_ = Node("Expr", expr1_)

            stack.append("expr1")
            stack.append("expr")
            stack.append("binop")
            x += 3

        elif token == "cParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif token == "cBracket":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif terminal:
            stack.pop()
            x -= 1

        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))
            break

    elif stack[x] == "expr2":

        if token == "oBracket":
            terminal = False
            stack.pop()
            x -= 1

            oBracket_ = Node("Open Brace", expr2_)
            expr_ = Node("Expr", expr2_)
            cBracket = Node("Closed Brace", expr2_)
            equals_ = Node("Equals", expr2_)
            expr_ = Node("Expr", expr2_)
            exprr2_ = Node("Expr2", expr2_)

            stack.append("expr1")
            stack.append("expr")
            stack.append("=")
            stack.append("]")
            stack.append("expr")
            stack.append("[")
            x += 6

        elif token == "equals":
            terminal = False
            stack.pop()
            x -= 1

            equals_ = Node("Equals", expr2_)
            expr1_ = Node("Expr1", expr2_)
            expr_ = Node("Expr", expr2_)

            stack.append("expr1")
            stack.append("expr")
            stack.append("=")
            x += 3

        elif terminal:
            stack.pop()
            x -= 1

        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))
            break

    elif stack[x] == "primary":

        if token == "identifier":
            terminal = False
            stack.pop()
            x -= 1

            identifier_ = Node("Identifier", primary_)
            expr3_ = Node("Expr3", primary_)

            stack.append("expr3")
            stack.append("identifier")
            x += 2

        elif token == "num":
            terminal = False
            stack.pop()
            x -= 1

            num_ = Node("Num", primary_)

            stack.append("num")
            x += 1

        elif token == "oParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            oParenthesis_ = Node("Open Parenthesis", primary_)
            expr_ = Node("Expr", primary_)
            cParenthesis_ = Node("Closed Parenthesis", primary_)

            stack.append(")")
            stack.append("expr")
            stack.append("(")
            x += 3

        elif terminal:
            stack.pop()
            x -= 1

        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))
            break

    elif stack[x] == "expr3":
        terminal = False

        if token == "identifier":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif token == "Endline":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif token == "COMMA":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1
            
        elif token == "oBracket":
            terminal = False
            stack.pop()
            x -= 1

            oBracket = Node("Open Brace", expr3_)
            expr_ = Node("Expr", expr3_)
            cBracket = Node("Closed Brace", expr3_)

            stack.append("]")
            stack.append("expr")
            stack.append("[")
            x += 3

        elif token == "num":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif token == "oParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            oParenthesis_ = Node("Open Parenthesis", expr3_)
            exprlist_ = Node("ExprList", expr3_)
            cParenthesis_ = Node("Closed Parenthesis", expr3_)

            stack.append(")")
            stack.append("exprlist")
            stack.append("(")
            x += 3

        elif token == "unOP":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1
            
        elif token == "cParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif token == "cBracket":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif token == "binOP":
            stack.pop()

        elif terminal:
            stack.pop()
            x -= 1

        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))
            break

    elif stack[x] == "exprlist":

        if token == "identifier":
            terminal = False
            stack.pop()
            x -= 1
            
            exprlisttail_ = Node("ExprListTail", exprlist_)

            stack.append("exprlisttail")
            x += 1

        elif token == "num":
            terminal = False
            stack.pop()
            x -= 1

            exprlisttail_ = Node("ExprListTail", exprlist_)

            stack.append("exprlisttail")
            x += 1

        elif token == "oParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            exprlisttail_ = Node("ExprListTail", exprlist_)

            stack.append("exprlisttail")
            x += 1

        elif token == "unOP":
            terminal = False
            stack.pop()
            x -= 1

            exprlisttail_ = Node("ExprListTail", exprlist_)

            stack.append("exprlisttail")
            x += 1

        elif token == "cParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif terminal:
            stack.pop()
            x -= 1

        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))
            break

    elif stack[x] == "exprlisttail":

        if token == "identifier":
            terminal = False
            stack.pop()
            x -= 1

            expr_ = Node("Expr", exprlisttail_)
            exprlisttail1_ = Node("ExprListTail'", exprlisttail_)

            stack.append("exprlisttail1")
            stack.append("expr")
            x += 2

        elif token == "num":
            terminal = False
            stack.pop()
            x -= 1

            expr_ = Node("Expr", exprlisttail_)
            exprlisttail1_ = Node("ExprListTail'", exprlisttail_)

            stack.append("exprlisttail1")
            stack.append("expr")
            x += 2

        elif token == "oParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            expr_ = Node("Expr", exprlisttail_)
            exprlisttail1_ = Node("ExprListTail'", exprlisttail_)

            stack.append("exprlisttail1")
            stack.append("expr")
            x += 2

        elif token == "unOP":
            terminal = False
            stack.pop()
            x -= 1

            expr_ = Node("Expr", exprlisttail_)
            exprlisttail1_ = Node("ExprListTail'", exprlisttail_)

            stack.append("exprlisttail1")
            stack.append("expr")
            x += 2

        elif terminal:
            stack.pop()
            x -= 1

        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))
            break

    elif stack[x] == "exprlisttail1":

        if token == "COMMA":
            terminal = False
            stack.pop()
            x -= 1

            comma_ = Node("Comma", exprlisttail1_)
            exprlisttail_ = ("ExprListTail", exprlisttail1_)

            stack.append("exprlisttail")
            stack.append(",")
            x += 2

        elif token == "cParenthesis":
            terminal = False
            stack.pop()
            x -= 1

            #stack.append("epsilon")
            #x += 1

        elif terminal:
            stack.pop()
            x -= 1

        elif terminal == False:
            print("syntax error line " + str(table2[c3][2]))
            break

    elif stack[x] == "identifier":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == ";":
        if token == "Endline":
            terminal = True
        
        stack.pop()
        x -= 1

    elif stack[x] == ",":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "[":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "{":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "char":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "int":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "num":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "(":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "unop":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "return":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "read":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "write":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "writeln":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "break":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "if":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "else":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "while":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "binop":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "=":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == ")":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "]":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "}":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "epsilon":
        terminal = True
        stack.pop()
        x -= 1

    elif stack[x] == "$":
        print("done")
        break

    else:
        terminal = False

    #if terminal and table2[c3 - 1][1] == "Endline":
        
    #print(table2[c3][0])

    print(stack)
    print("\n\n")

    if c3 + 1 == len(table2):
        stack.pop()
        terminal = False

    elif terminal:
        c3 += 1

#print(table2[c3][0])

#print(table2[c3][1])


print(stack)
print("")
print_tree(program_)
print("")
#print_tree(program_, horizontal = False)
