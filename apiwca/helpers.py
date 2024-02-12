def gender_emoji(gender):
    match gender:
        case 'm':
            return '🧑'
        case 'f':
            return '👩'
    return '👤'


def get_time(mils: int) -> str:
    mils_str = str(mils)[-2:]

    mils *= 10
    s, mils = divmod(mils, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)

    return f"{m}:{s:02d}.{mils_str}" if m > 0 else f"{s}.{mils_str}"


def set_res(res, event):
    match event:
        case '333fm':
            return res if res < 100 else str(res)[:2] + '.' + str(res)[2:]
        case '333fm':
            res = str(res)

            missed = int(res[-2:])
            solved = 99 - int(res[:2]) + missed
            total_cubes = solved + missed

            time_s = int(res[2:-2])
            minutes = time_s // 60
            seconds = time_s % 60

            return f'{solved}/{total_cubes} {minutes}:{seconds:02d}'
    return get_time(res)
