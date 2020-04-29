from pythonds.basic import Deque


def isPalindrome(str):
    deq = Deque()

    for ch in str:
        deq.addRear(ch)

    temp = True

    while deq.size() > 1 and temp:
        first = deq.removeFront()
        last = deq.removeRear()
        if first != last:
            temp = False

    return temp


print(isPalindrome("radar"))
