def arithmetic_arranger(problems, show_answers=True):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []

    for value in problems:
        operation = value.split(" ")

        if operation[1] not in ('-+*:'):
            return "Error: Operator must be '+','-','*' or ':'."

        if len(operation[0]) > 4 or len(operation[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        try:
            value1 = int(operation[0])
            value2 = int(operation[2])
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        longest_val = max(len(operation[0]), len(operation[2]))
        width = longest_val + 2

        line1 = f"{operation[0]:>{width}}"
        line2 = operation[1] + f"{operation[2]:>{width - 1}}"

        dash = '-' * width

        try:
            arranged_problems[0] += (' ' * 4) + line1
        except IndexError:
            arranged_problems.append(line1)
        try:
            arranged_problems[1] += (' ' * 4) + line2
        except IndexError:
            arranged_problems.append(line2)
        try:
            arranged_problems[2] += (' ' * 4) + dash
        except IndexError:
            arranged_problems.append(dash)

        if show_answers:
            if operation[1] == '+':
                ans = int(operation[0]) + int(operation[2])
            elif operation[1] == '*':
                ans=int(operation[0]) * int(operation[2])
            elif operation[1] == ':':
                ans=int(operation[0]) / int(operation[2])
            else:
                ans = int(operation[0]) - int(operation[2])
            answer = f"{str(ans):>{width}}"

            try:
                arranged_problems[3] += (' ' * 4) + answer
            except IndexError:
                arranged_problems.append(answer)

    output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
    if show_answers:
        output = output + f"\n{arranged_problems[3]}"
    return output


print(f'\n{arithmetic_arranger(["25 : 5", "3801 * 2", "45 + 43", "123 + 49"])}')