import random
import re
from sys import exit

def main():
    time = 3
    count = 1
    num = 0
    dict = {'0': 5, '1': 10, '2': 20, '3': 50, '4': 100}

    print('猜数字')
    go = int(input('开始：1\n结束：0\n->'))

    while go != 1 and go != 0:
        print('Input 1 or 0.')
        go = int(input('开始：1\n结束：0\n->'))  # 重复输入
    if go == 1:
        pass
    elif go == 0:
        exit()

    print('｛LV0.新手}｛LV1.简单｝｛LV2.一般｝｛LV3.困难｝｛LV4.噩梦｝｛LV5.地狱｝')
    r = input('Level:')
    r = re.sub('\D', '', r)  # 抽出数字

    if r.strip() == '':  # 检查是否含有数字
        print('隐藏难度｛LV6.调戏｝')
        n = 1000
        time = 99
    else:
        n = dict.get(r, 500)

    secret = random.randint(1, n + 1)  # 随机的范围 根据难度调整
    print('猜猜{1-%s}之间的数:' % n)

    while True:  # 机会内循环即可，猜中了可以用break跳出循环
        print('一定是：' , end = '')
        num = input()

        if num.isdigit():  # 检查玩家输入是否有误，防止程序崩溃
            num = int(num)
            if num < 1:
                print('现在就放弃太可惜了')
            elif num > n:
                print('超出范围')
            elif num > secret:
                print('太大')
            elif num < secret:
                print('太小')
            else:
                if count == 1:  # 算是奖励机制？
                    print('棒')
                elif count == 2:
                    print('赞')
                else:
                    print('好')
                break

            time -= 1
            count += 1  # 奖励机制计数

            if time == 0:
                print('正确答案：%s' % secret)
                break
            else:
                print('还有[%s]次机会:' % time)
        else:
            print('要崩溃了!!!')
    print('游戏结束!')

if __name__ == '__main__':
    main()