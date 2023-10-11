def change(music):
    if 'A#' in music:
        item = item.replace("A#", 'a')
    if 'F#' in music:
        music = music.replace('F#', 'f')
    if 'C#' in music:
        music = music.replace('C#', 'c')
    if 'G#' in music:
        music = music.replace('G#', 'g')
    if 'D#' in music:
        music = music.replace('D#', 'd')
    if 'E#' in music:
        music = music.replace("E#", 'e')
    return music


def solution(m, musicinfos):
    answer = []
    index = 0
    for music in musicinfos:
        index += 1
        start, end, title, code = music.split(",")

        # 시간 추출
        start_h, start_m = start.split(":")
        end_h, end_m = end.split(":")
        times = (int(end_h) * 60 + int(end_m)) - (int(start_h) * 60 + int(start_m))

        # # 변환하기
        ch_music = change(code)

        # 음악 길이
        len_music = len(ch_music)

        # 재생된 코드 구하기
        total = ch_music * (times // len_music) + ch_music[:times % len_music]

        # m과 재생된 코드 일치하는지 구하기
        ch_m = change(m)
        if ch_m in total:
            answer.append([times, index, title])
    # print(answer)

    if not answer:
        return "(None)"
    elif len(answer) == 1:
        return answer[0][2]
    else:
        # sorted에서 - 사용하면 내림차순으로 정렬하는 것
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))
        return answer[0][2]


solution("ABCDEFG",	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"] )