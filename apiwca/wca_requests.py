# import asyncio

from aiohttp import ClientSession

from config import _


BASE_URL = 'https://www.worldcubeassociation.org/api/v0'


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
            return res if res < 100 else str(res)[:2]+'.'+str(res)[2:]
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


def get_prs(prs: dict, events: list = None) -> str:
    pr = _['personal_record']
    prs_string = ''

    for event, v in prs.items():
        if events and event not in events:
            continue

        string = _['event'].format(event=event)
        avg = v.get('average')
        single = v.get('single')

        if avg:
            avg['type'] = 'Average'
            avg['best'] = set_res(avg['best'], event)
            string += pr.format(**avg)

        if single:
            single['type'] = 'Single'
            single['best'] = set_res(single['best'], event)
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


def parsed_users(users: list[dict]) -> str:
    users_str = _['finded_users']

    for user in users:
        gender = user.get('gender')
        if gender == 'm':
            gender = '🧑'
        elif gender == 'f':
            gender = '👩'
        else:
            gender = '👤'
            
        country = user.get('country')

        if not country:
            country = user.get('country_iso2')
        else:
            country = country.get('name')

        data = {
            'name': user['name'],
            'wcaid': user['wca_id'],
            'gender': gender,
            'country': country
        }

        users_str += _['user'].format(**data)
    
    return users_str


async def get_wca_profile(wca_id: str) -> dict | None:
    async with ClientSession(trust_env=True) as session:
        async with session.get(BASE_URL+f'/persons/{wca_id}') as resp:
            res = await resp.json()

            if res.get('error'):
                return None

            res['photo_url'] = res['person']['avatar']['url']

            return res


async def search_users(query: str):
    async with ClientSession(trust_env=True) as session:
        params = {'q': query, 'persons_table': 'true'}
        async with session.get(BASE_URL+f'/search/users', params=params) as resp:
            res = (await resp.json()).get('result')

            if len(res) > 10:
                res = res[:10]
                
            return res
    

# if __name__ == '__main__':
#     parsed_users(asyncio.run(search_users('alexey')))
#     asyncio.run(get_wca_profile('2021toli01'))
    