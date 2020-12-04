import random
print('-' * 8 + 'Guess The Number' + '-' * 8)
# To create a loop. This variable is used for decision.
Play_again = True
while Play_again:
    # Choose the range.
    Start = int(input("What's the smallest number?"))
    End = int(input("And the largest number?"))
    print('The answer is auto-generated.')
    # Generate integer within this range.
    Num = random.randint(Start, End)
    while Play_again:
        # This loop is used to allow the user to type in answer multiple times.
        Answer = input('Guess a number, from %d to %d' % (Start, End))
        # If to prevent from not typing in a number
        if Answer.isdigit():
            Answer = int(Answer)
            if Answer < Num and Start <= Answer <= End:
                print('Nope, smaller than that.')
            elif Answer == Num and Start <= Answer <= End:
                print('Correct.')
                while True:
                    Choice = input('Want another Game?(yes or no)')
                    # Choosing to play again or not.
                    if str.lower(Choice) == 'yes':
                        break
                    elif str.lower(Choice) == 'no':
                        print('Good bye!')
                        Play_again = False
                        break
                    else:
                        print("Yes or no?")
                        continue
                # Problem here: it will crash if the user didn't type in "yes" or "no".
            elif Answer > Num and Start <= Answer <= End:
                print('Nope, smaller than that.')
            else:
                print('Nope, it\'s from %d to %d' % (Start, End))
        else:
            print("I's a number, plz...")
