import time
from datetime import datetime
parkplace = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
parking = []


#입차용

def entrance():
    parkplace.sort()
    i = len(parkplace)

    while True:
        if i != 0:
            print("입차를 선택하셨습니다.")
            time.sleep(1.5)
            print("")
            print("입차하실 자리를 선택해주세요.")
            print("초기 화면으로 돌아가려면 0을 눌러주세요")
            time.sleep(1.5)
            print("")
            print("남은 자리는", parkplace, "입니다.")
            time.sleep(1.5)
            print("자리를 입력해 주세요.")
            choice = int(input())

            if choice in parking:
                print("이미 예약된 자리입니다. 다시 입력해 주세요.")
                print("")
                continue

            elif choice <= 15 and choice >= 1:
                parkplace.remove(choice)
                parking.append(choice)
                print(choice,"번 자리에 예약되었습니다.")
                time.sleep(1.5)
                print("")
                print("24시간 이상 주차 시 견인될 수 있습니다.")
                t = datetime.now()
                print("현재 시간은", t, "입니다")
                time.sleep(1.5)
                print("")
                print("감사합니다.")
                time.sleep(1.5)
                print("")
                break

            elif choice == 0:
                break
            else:
                print("1부터 15까지의 숫자를 입력해주세요.")
                time.sleep(1.5)
                continue

        else:
            print("자리가 다 찼습니다.")
            time.sleep(1.5)
            break


#출차용

def out():
    parking.sort()
    s = len(parking)
    while True:
        if s != 0:
            print("출차를 선택하셨습니다.")
            time.sleep(1.5)
            print("출차하실 자리를 선택해주세요.")
            print("초기 화면으로 돌아가려면 0을 선택해주세요.")
            time.sleep(1.5)
            print("")
            print("주차된 자리는", parking, "입니다.")
            time.sleep(1.5)
            print("자리를 입력해 주세요.")
            choice2 = int(input())
            if choice2 in parking:
                parking.remove(choice2)
                parkplace.append(choice2)
                print("안녕히가십시오.")
                time.sleep(1.5)
                print("")
                break
            elif choice2 == 0:
                break
            else:
                print("올바른 숫자를 입력해주세요.")
                print("")
                time.sleep(1.5)
                continue
        else:
            print("입차된 차량이 없습니다.")
            time.sleep(1.5)
            print("")
            break

#초기화면

while True:
    print("무료 주차장 입출차 시스템입니다.")
    time.sleep(1.5)
    print("이용하실 서비스를 선택해주세요.")
    print("")
    time.sleep(1.5)
    print("1. 입차", "2. 출차")
    number = int(input())
    if number == 1:
        entrance()
    elif number == 2:
        out()
    else:
        print("1 또는 2 를 입력해주세요.")
        time.sleep(1.5)
