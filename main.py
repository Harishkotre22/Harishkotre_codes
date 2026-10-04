def precedence(operator):

    if operator == "+" or operator == "-":
        return 1
    elif operator == "*" or operator == "/":
        return 2
    elif operator == "^":
        return 3
    else:
        return 0


output = []
operator = []

a = input("Enter the expression")
i = 0


def expressioncheck(a, i, output, operator):

    while i < len(a):

        if a[i].isdigit():
            n = ""

            while i < len(a) and a[i].isdigit():
                n += a[i]
                i += 1

            output.append(int(n))

        elif a[i].isalnum():
            output.append(a[i])
            i += 1

        else:
            newoperator = a[i]

            if newoperator == "(":
                operator.append(newoperator)

            elif newoperator == ")":
                while operator and operator[-1] != "(":
                    output.append(operator.pop())

                if operator and operator[-1] == "(":
                    operator.pop()

            else:
                while operator and (
                        precedence(newoperator) < precedence(operator[-1])
                        or
                        (precedence(newoperator) == precedence(operator[-1]) and newoperator != "^")
                ):
                    output.append(operator.pop())

                operator.append(newoperator)

            i += 1


expressioncheck(a, i, output, operator)

while operator:
    output.append(operator.pop())

print(output)