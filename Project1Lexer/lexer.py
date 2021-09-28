# AUSTIN JOHNS
# CST-405
# PROJECT 1 - LEXICAL ANALYSIS


lexer_file = open('lexer.GCU-PL', 'r')  # STORING GCU-PL AS READABLE BY PROGRAM
count = 0  # COUNT FOR ITERATION OF EACH LINE
table = []  # TABLE AS A LIST
table2 = []  # TABLE2 AS A LIST
table3 = []  # TABLE3 AS A LIST
table4 = []  # TABLE4 AS A LIST
table5 = []  # TABLE5 AS A LIST

while True:  # STORING VALUES INTO A LIST BASED ON GCU-PL FILE
    count += 1  # COUNT INCREASE

    line = lexer_file.readline()  # STORING EACH LINE OF GCU-PL INTO A LIST
    table.append(line)  # APPEND FROM GCU-PL INTO TABLE

    if not line:  # CHECKING FOR LAST LINE OF GCU-PL
        break  # END LOOP AT END OF LIST

lexer_file.close()  # CLOSES FILE

for x in table:  # CREATING A LIST OF LISTS FOR USE IN A TABLE
    table2.append(
        x.split())  # APPENDING INTO A LIST OF LISTS
table2.pop()  # REMOVING EMPTY LIST

for i in range(0, len(table2)):  # ITERATION THROUGH ROWS OF THE TABLE
    if i != 0: table3.append(
        count_loop - 1)  # STORING STRINGS IN A TABLE FOR LATER RECALL
    count_loop = 0  # FOR COUNTING THE AMOUNT OF STRINGS

    for j in table2[i]:  # ITERATION THROUGH COLUMNS OF TABLE
        count_loop += 1  # KEEPS TRACK OF HOW MANY STRINGS ARE IN A ROW

table3.append(
    count_loop - 1)  # STORING IN A NEW TABLE FOR LATER RECALL

for i in range(0, len(table2)):  # ITERATION THROUGH MAIN LOOP
    count_loop = 0  # KEEPING TRACK OF LOCATION

    for j in table2[i]:  # ITERATION OF LIST OF LISTS
        count_loop += 1  # FOR TRACKING ITERATION

        if table2[i][count_loop - 1] == "int":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "TYPE: int", "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "char":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "TYPE: char",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "return":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "keyword", "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "read":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "keyword", "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "write":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "keyword", "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "writeln":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "keyword", "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "break":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "keyword", "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "if":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "keyword", "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "else":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "keyword", "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "while":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "keyword", "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "+":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "binary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "-":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "binary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "*":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "binary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "/":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "binary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "==":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "binary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "!=":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "binary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "<":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "binary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "<=":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "binary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == ">":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "binary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == ">=":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "binary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "&&":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "binary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "||":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "binary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] == "=":  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "binary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] != "-" and table2[i][count_loop - 1].find("-") == 0:  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "unary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

        elif table2[i][count_loop - 1] != "!" and table2[i][count_loop - 1].find("!") == 0:  # CHECKING TOKEN

            table4 = [table2[i][count_loop - 1], "unary operator",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPENDS TO A NEW LIST

        else:  # TOKEN IS AN IDENTIFIER IF ALL OTHER CHECKS FAIL

            table4 = [table2[i][count_loop - 1], "identifier",
                      "Line " + str(i + 1)]  # TOKEN AND LINE NUMBER
            table5.append(table4)  # APPEND TO A NEW LIST

headers = ["String", "Token", "Line"]  # CATEGORIES FOR TABLE

print("")  # CREATES A NEW LINE

for z in range(0, len(headers)):  # ITERATION THROUGH HEADERS LIST
    print(headers[z].center(25), end="")  # PRINTING CENTERED HEADERS WITH 25PT SPACING

print("")  # CREATES A NEW LINE

for x in range(0, len(table5)):  # ITERATION THROUGH LIST OF STRINGS, TOKENS, AND LINE NUMBERS
    print("")  # CREATES A NEW LINE

    for y in range(0, 3):  # ITERATION THROUGH STRING, TOKENS, AND LINES
        print(table5[x][y].center(25),
              end="")  # PRINTING STRING, TOKEN, AND LINES

print("\n")  # CREATING AN NEW LINE