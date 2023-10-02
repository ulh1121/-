from math import ceil


def solution(fees, records):
    answer = []
    car, car2 = {}, {}
    for i in range(len(records)):
        time_tmp, car1, inorout = records[i].split(" ")
        car[car1] = []
        car2[car1] = []
    for i in range(len(records)):
        time_tmp, car1, inorout = records[i].split(" ")
        car[car1].append(time_tmp)

    ans_dict = sorted(car.keys())
    car = dict(sorted(car.items()))
    print(car)
    for car_num in car:
        cnt = len(car[car_num])
        if cnt % 2 == 1:
            car[car_num].append("23:59")
        total = 0
        payment = 0
        while car[car_num]:
            time_in = car[car_num].pop(0)
            time_cnt1 = int(time_in.split(":")[0]) * 60 + int(time_in.split(":")[1])

            time_out = car[car_num].pop(0)
            time_cnt2 = int(time_out.split(":")[0]) * 60 + int(time_out.split(":")[1])
            total += time_cnt2 - time_cnt1
        if total > fees[0]:
            payment += fees[1]
            total -= fees[0]
            payment += ceil(total / fees[2]) * fees[3]
        elif total <= fees[0]:
            payment = fees[1]

        answer.append(payment)

    return answer