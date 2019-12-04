def KaplumbagaYarisi(speed_a,speed_b,step):
    if speed_a > speed_b:
        reach_time = (step)/(speed_a - speed_b)
        sec_reach_time = reach_time*3600
        second = sec_reach_time % 60
        minute = sec_reach_time // 60
        hour = 0
        if minute >= 60:
            hour = minute // 60
            minute = minute % 60

        return [hour,minute,second]
    else:
        return [-1,-1,-1]

print(KaplumbagaYarisi(23,20,80))