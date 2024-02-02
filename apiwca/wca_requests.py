from aiohttp import ClientSession

from config import _


BASE_URL = 'https://www.worldcubeassociation.org/api/v0'


def get_time(mils: int) -> str:
    mils_str = str(mils)[-2:]

    mils *= 10
    seconds, mils = divmod(mils, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    
    if minutes > 0:
        time_str = f"{minutes}:{seconds:02d}.{mils_str}"
    time_str = f"{seconds}.{mils_str}"

    return time_str


def set_res(res, event):
    if event == '333fm':
        return res if res < 100 else str(res)[:2]+'.'+str(res)[2:]
    elif event == '333mbf':
        res = str(res)

        missed = int(res[-2:])
        solved = 99 - int(res[:2]) + missed
        total_cubes = solved + missed

        time_s = int(res[2:-2])
        minutes = time_s // 60
        seconds = time_s % 60

        return f'{solved}/{total_cubes} {minutes}:{seconds:02d}'
    else:
        return get_time(res)


def get_prs(prs: dict, events: list = None) -> str:
    pr = _['personal_record']
    prs_string = ''

    for k, v in prs.items():
        if events and k not in events:
            continue

        string = f'🍼*Дисциплина {k}*:'
        avg = v.get('average')
        single = v.get('single')

        if avg:
            avg['type'] = 'Average'
            avg['best'] = set_res(avg['best'], k)
            string += pr.format(**avg)

        if single:
            single['type'] = 'Single'
            single['best'] = set_res(single['best'], k)
            string += pr.format(**single)

        prs_string += string + '\n\n'

    return prs_string


def parsed_wca_profile(profile: dict, events: list = None) -> dict:
    person = profile.get('person')
    records = profile.get('records')
    medals = profile.get('medals')
    personal_records = get_prs(profile.get('personal_records'), events)

    data = {
        'name': person['name'],
        'wca_id': person['id'],
        'wrs': records['world'],
        'crs': records['continental'],
        'nrs': records['national'],
        'gold': medals['gold'],
        'silver': medals['silver'],
        'bronze': medals['bronze'],
        'personal_records': personal_records
    }

    return data


async def get_wca_profile(wca_id: str) -> dict | None:
    async with ClientSession(trust_env=True) as session:
        async with session.request('get', BASE_URL+f'/persons/{wca_id}') as resp:
            res = await resp.json()

            if res.get('error'):
                return None

            res['photo_url'] = res['person']['avatar']['url']

            return res
