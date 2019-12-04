speed_a = int(float(input("Please enter the speed of the Turtle A: ")))
speed_b = int(float(input("Please enter the speed of the Turtle B: ")))
step = int(float(input("Please enter the number of steps: ")))

def TurtleRacing():
    global speed_a, speed_b, step
    if speed_a > speed_b:
        time = (step / (speed_a - speed_b)) * 3600
        second = time % 60
        minute = time // 60
        hour = 0
        if minute >= 60:
            hour = minute // 60
            minute = minute % 60
        return [hour,minute,second]
    else:
        return [-1,-1,-1]

if speed_a == "" and speed_b == "" and step == "":
    print("Please enter an int value!")
else:
    print(TurtleRacing())
