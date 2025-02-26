
def climbstairs(n):
    pre_pre = pre = cur = 1
    for i in range(2, n+1):
        cur = pre + pre_pre
        pre_pre = pre
        pre = cur
    return cur

if __name__ == '__main__':
    print(climbstairs(5))