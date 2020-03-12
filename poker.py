def card_queues(queues):
    '''#比较数值大小,因为数值与列表索引一一对应，直接用索引来代替对应原本的数值大小
    #split()默认对所有的空格进行切分 空格，\n,\t，需要考虑到输入形式的替换
    #下述列表推导，r为数值，s为颜色'''
    queues = ['23456789TJQKA'.index(r) for r, s in queues.split()]
    queues.sort()
    return queues


def judge_straight(queues):
    '''# 判断是否为顺子，数值相差为4，利用set去重为5'''
    queues = card_queues(queues)
    return max(queues) - min(queues) == 4 and len(set(queues)) == 5


def judge_color_only(queues):  # 判断是否为同花
    hand_flush = [s for r, s in queues.split()]
    return len(set(hand_flush)) == 1

def judge_32(queues):  # 判断是否为3带2
    for r, s in queues.split():
        if queues.count(r) == 3:
            return True
    return None


def judge_41(queues):
    for r, s in queues.split():
        if queues.count(r) == 4:
            return True
    return None


def type_check(queues):  # 根据基本类型的组合来判断复合类型
    # 同花顺
    if judge_straight(queues) and judge_color_only(queues):
        return 9
    # 4带1
    elif judge_41(queues):
        return 8
    # 葫芦：3带1对
    elif judge_32(queues) and len(set(card_queues(queues))) == 2:
        return 7
    # 同花
    elif judge_color_only(queues):
        return 6
    # 顺子
    elif judge_straight(queues):
        return 5
    # 3带2个单张
    elif judge_32(queues) and len(set(card_queues(queues))) == 3:
        return 4
     # 两对
    elif judge_32(queues) == None and len(set(card_queues(queues))) == 3:
        return 3
    # 对子
    elif len(set(card_queues(queues))) == 4:
        return 2

    # 散牌
    else:
        return 1

#同花顺和顺子比大小
def compare_straight(queues1, queues2):
     high = -1
     if max(card_queues(queues1)) > max(card_queues(queues2)):
         high = max(card_queues(queues1))
         return 2,high
     elif max(card_queues(queues1)) > max(card_queues(queues2)):
         high = max(card_queues(queues2))
         return 1,high
     else:
         return 0,high

#比较铁支四带一，三带二，三带一的大小
def compare_41_32_31(queues1, queues2):
    l1 = card_queues(queues1)
    l2 = card_queues(queues2)
    if max(l1, key=l1.count) > max(l2, key=l2.count):
        high = max(l1, key=l1.count)
        return 2,high
    else:
        high = max(l2, key=l2.count)
        return 0,high
#判断散牌和同花大小(
def compare_ran(queues1, queues2):
    high = -1
    l1 = card_queues(queues1)
    l2 = card_queues(queues2)
    for i in range(len(l1)-1, -1, -1):
        if l1[i] == l2[i]:
            continue
        elif l1[i] > l2[i]:
            high = l1[i]
            return 2,high
        else:
            high = l2[i]
            return 0,high
    return 1,high

#判断对子
def compare_pair1(queues1, queues2):
    high = -1
    l1 = card_queues(queues1)
    l2 = card_queues(queues2)
    m1 = max(l1, key=l1.count)
    m2 = max(l2, key=l2.count)
    if m1 > m2:
        high = m1
        return 2,high
    elif m1 < m2:
        high = m2
        return 0,high
    else:
        for m1 in l1:
            l1.remove(m1)
        for m2 in l2:
            l2.remove(m2)
        return compare_ran(l1 , l2)

#判断两对
def compare_pair2(queues1, queues2):
    high = -1
    l1 = card_queues(queues1)
    l2 = card_queues(queues2)
    m1 = max(l1, key=l1.count)
    m2 = max(l2, key=l2.count)
    for m1 in l1:
        l1.remove(m1)
    for m2 in l2:
        l2.remove(m2)
    m3 = max(l1, key=l1.count)
    m4 = max(l2, key=l2.count)
    if m3 > m4:
        high = m3
        return 2,high
    elif m3 < m4:
        high = m4
        return 0,high
    else:
        l1.append(m1)
        l1.append(m1)
        l2.append(m2)
        l2.append(m2)
        return compare_pair1(l1, l2)
name_list = ['High Card','Pair','Two Pairs','Three of a Kind','Straight','Flush','Full House','Four of a kind','Straight flush']
card_list = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
def compare_unit(queues1, queues2):
    type1 = type_check(queues1)
    type2 = type_check(queues2)
    if type1 > type2:
        print("Black wins-"+name_list[type1-1])
        return "Black wins-"+name_list[type1-1]
    elif type1 < type2:
        print("White wins-"+name_list[type2-1])
        return "White wins-"+name_list[type1-1]
    else:
        if type1 == 1 or type1 == 6:
            final , highcard = compare_ran(queues1,queues2)
        elif type1 == 2:
            final , highcard  = compare_pair1(queues1,queues2)
        elif type1 == 3:
            final , highcard  = compare_pair2(queues1,queues2)
        elif type1 == 5 or type1 == 9:
            final , highcard = compare_straight(queues1,queues2)
        else:
            final , highcard = compare_41_32_31(queues1,queues2)
        if final == 2:
            print("Black wins-high card:"+card_list[highcard])
            return "Black wins-high card:"+card_list[highcard]
        elif final == 0:
            print("White wins-high card:"+card_list[highcard])
            return "White wins-high card:" + card_list[highcard]
        else:
            print("Tie")
            return "Tie"


# if __name__ == "__main__":
#     s = "2H 3D 5S 9C KD"
#     q = "2C 3H 4S 8C KH"
#     compare_unit(s,q)









