print('Welcom to my project!')
playing = input('Do you want to play: ')
if playing.lower() != 'yes':
    quit()
score = 0
question = 0
answer = input('What does CPU stand for? ')
question +=1
if answer.lower() == 'central processing unit':
    print('Yay correct!')
    score += 1
else:
    print('oops incorrect!')
answer = input('What does GPU stand for? ')
question +=1
if answer.lower() == 'graphics processing unit':
    print('Yay correct!')
    score += 1
else:
    print('oops incorrect!')
answer = input('What does RAM stand for? ')
question +=1
if answer.lower() == 'random access memory':
    print('Yay correct!')
    score += 1
else:
    print('oops incorrect!')
print(f'You answered {score} questions correctly and your score is {(score/question)*100}')
