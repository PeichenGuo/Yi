import random as ran
import os

def DaYanShiFa():
    yaos = []
    for i in range(0, 6):
        grass = 50
        block = [0, 0, 0]
        box = 0
        left = 0
        right = 0
        hang = 0
        for j in range(0, 3):
            # 右手取一策，反于椟中，
            grass -= 1
            box += 1
            # 左右手中分四十九策，置格之左右两大刻
            while left < 1:
                left = int(ran.random() * grass)
            right = grass - left
            # 以左手取左大刻之策执之，而以右手取右大刻之一策，挂于左手之小指间
            right -= 1
            hang += 1
            # 以右手四揲（shé）左手之策
            yu = left % 4
            if yu == 0:
                yu = 4
            # 归其所余之策，或一、或二、或三、或四，而扐（lè）之左手无名指间
            hang += yu
            left -= yu
            # 以右手反过揲之策于左大刻，遂取右大刻之策执之，而以左手四揲之。
            yu = right % 4
            if yu == 0:
                yu = 4
            # 次归其所余之策如前，而扐之左手中指之间
            hang += yu
            right -= yu
            # 次以右手反过揲之策于右大刻，而合左手一挂二扐之策，置于格上第一小刻
            block[j] = hang 
            hang = 0
            # 再以两手取左右大刻之蓍合之
            grass = left + right
            left = 0
            right = 0

            print(f"\t第{i + 1}爻第{j + 1}变结束，所剩蓍草为{grass}")
            t = input()
            if t != "":
                return
        # 三变既毕，乃视其三变所得挂扐过揲之策，而画其爻于版
        tmp = grass / 4
        ch = ""
        if tmp == 9:
            ch = "—— : 老阳"
        elif tmp == 8:
            ch = "-- : 少阴"
        elif tmp == 7:
            ch = "-  : 少阳"
        else:
            ch = "×  : 老阴"
        print(f"\n\t===== 第{i+1}爻为【{ch}】=====\n")
        yaos.append(ch)

    # 凡十有八变而成卦，乃考其卦之变，而占其事之吉凶      
    print("\t================================")
    for yao in yaos:
        print(f"\t\t   {yao}\t")
    print("\t================================")


print("\t================================")
print("\t==     使用此程序起卦的时候   ==")
print("\t==  请在一个南边有窗子的房间里 ==")
print("\t==       站在房间正中央       ==")
print("\t==     把电脑放在你的北面     ==")
print("\t==        按回车以继续      ==")
print("\t================================\n")

input()
print("\t正在盥手焚香致敬")

input()
print("\t盥手焚香致敬完毕")

name = input("\t尊姓大名？\t\n")
thing = input("\t占卜何事？\t\n")
print(f"\n请朗读如下文字：\n\t假尔泰筮有常，假尔泰筮有常。某人{name}，今以{thing}之事，未知可否。爰质所疑于神于灵，吉凶得失，悔吝忧虞，惟尔有神，尚明告之!")

input()
print("\t开始起卦")

DaYanShiFa()

input()
print("\t起卦结束")

input()
print("\t焚香致敬而退")



