# https://www.acmicpc.net/problem/8958





n = int(input())
answers = []

for i in range(n):
    answers.append(input())

grades = []

for i in range(len(answers)):
    cur_answer = answers[i]
    total_grade = 0
    right_in_a_row_count = 0
    for j in range(len(cur_answer)):
        cur_char = cur_answer[j]
        if cur_char == 'O':
            right_in_a_row_count = right_in_a_row_count + 1
        elif cur_char == 'X':
            right_in_a_row_count = 0
        total_grade = total_grade + right_in_a_row_count
    grades.append(total_grade)

for i in range(len(grades)):
    print(grades[i])