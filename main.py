import random
print('-' * 8 + '数字炸弹' + '-' * 8)
Play_again = True
while Play_again:
    Start = int(input('请输入最小数字'))
    End = int(input('请输入最大数字'))
    print('答案将会随机生成')
    Num = random.randint(Start, End)
    while True:
        Answer = input('猜一个数字，' + str(Start) + '到' + str(End))
        if Answer.isdigit():
            Answer = int(Answer)
            if Answer < Num and Start <= Answer <= End:
                print('错了，比这大')
            elif Answer == Num and Start <= Answer <= End:
                print('对了')
                while True:
                    Choice = input('还要再玩吗？')
                    if str.lower(Choice) == 'yes':
                        break
                    elif str.lower(Choice) == 'no':
                        Play_again = False
                        break
                    else:
                        print('到底玩不玩啊')
                        continue
            elif Answer > Num and Start <= Answer <= End:
                print('错了，比这小')
            else:
                print('sb,' + str(Start) + '到' + str(End) + '!')
        else:
            print('额额额，是数字。。。')
