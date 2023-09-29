def solution(book_time):
    def get_time(times):
        return int(times[0:2]) * 60 + int(times[3:])

    books = sorted([[get_time(i[0]), get_time(i[1]) + 10] for i in book_time])

    room = []

    for book_time in books:
        if not room:
            room.append(book_time)
            continue
        for index, room_time in enumerate(room):
            if book_time[0] >= room_time[-1]:
                room[index] = room_time + book_time
                break
        else:
            room.append(book_time)
    return len(room)