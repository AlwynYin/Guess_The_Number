import random
print('-' * 8 + 'Guess The Number' + '-' * 8)
# To create a loop. This variable is used for decision.
Play_again = a = True
while Play_again:
    # Choose the range.
    # This if can only go once, so a burr variable is used.
    if a:
        Start = int(input("What's the smallest number?"))
        End = int(input("And the largest number?"))
        print('The answer is auto-generated.')
        # Generate integer within this range.
        Num = random.randint(Start, End)
        # This loop is used to allow the user to type in answer multiple times.
        a = False
    Answer = input('Guess a number, from %d to %d' % (Start, End))
    # If to prevent from not typing in a number
    if Answer.isdigit():
        Answer = int(Answer)
        if Answer < Num and Start <= Answer <= End:
            print('Nope, larger than %d.' % Answer)
        elif Answer == Num and Start <= Answer <= End:
            print('Correct.')
            while True:
                Choice = input('Want another Game?(yes or no)')
                # Choosing to play again or not.
                if str.lower(Choice) == 'yes':
                    # set a back to true so that the if will run again
                    a = True
                    break
                elif str.lower(Choice) == 'no':
                    print('Good bye!')
                    Play_again = False
                    break
                else:
                    print("yes or no?")
                    continue
        elif Answer > Num and Start <= Answer <= End:
            print('Nope, smaller than %d.' % Answer)
        else:
            print('Nope, it\'s from %d to %d' % (Start, End))
    else:
        print("I's a number, plz...")
