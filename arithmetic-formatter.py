def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    firstline = ''
    secondline = ''
    separateline = ''
    answerline = ''
    
    for problem in problems:
        values = problem.split(' ')
        if len(values) == 3:
            if values[1] != '+' and values[1] != '-':
                return "Error: Operator must be '+' or '-'."
            
            if not (values[0].isdigit() and values[2].isdigit()):
                return 'Error: Numbers must only contain digits.'

            if len(values[0]) > 4 or len(values[2]) > 4:
                return 'Error: Numbers cannot be more than four digits.'

            longest = ''
            firstline += ' ' * 2
            secondline += values[1] + ' '
            separateline += '--'
            if len(values[0]) >= len(values[2]):
                longest = values[0]
                firstline += values[0]
                separateline += '-' * len(values[0])
                secondline += ' ' * (len(values[0]) - len(values[2])) + values[2] if len(values[0]) > len(values[2]) else values[2]
            else:
                longest = values[2]
                secondline += values[2]
                firstline += ' ' * (len(values[2]) - len(values[0])) + values[0]
                separateline += '-' * len(values[2])

            if values[1] == '+':
                answer = str(int(values[0]) + int(values[2]))
            elif values[1] == '-':
                answer = str(int(values[0]) - int(values[2]))

            answerline += (' ' if len(answer) > len(longest) else ' ' * 2) + answer
            
            if problem != problems[len(problems) - 1]:
                spacing = ' ' * 4
                firstline += spacing
                secondline += spacing
                separateline += spacing
                answerline += spacing
        else:
            return 'Error: Numbers must only contain digits.'
    linebreak = '\n'
    if show_answers == True:
        return firstline + linebreak + secondline + linebreak + separateline + linebreak + answerline
    else:
        return firstline + linebreak + secondline + linebreak + separateline

# test case
print(f'{arithmetic_arranger(["98 + 35", "3801 - 2", "45 + 43", "123 + 49"], True)}')