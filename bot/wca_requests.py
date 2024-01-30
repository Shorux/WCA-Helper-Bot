from pprint import pprint
import aiohttp
import asyncio


BASE_URL = 'https://www.worldcubeassociation.org/api/v0'

pr = '''
    *{type}* 🫴 {best}
        Место в рейтинге👇
            WR:{world_rank}, CR:{continent_rank}, NR:{country_rank}'''


def get_time(mils: int) -> str:
    mils *= 10
    seconds, mils = divmod(mils, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    time_str = f"{minutes}:" if minutes > 0 else ""
    time_str += f"{seconds}.{int(mils)//10}"

    return time_str

print(get_time(890320800)) #3196800

def set_res(res, k):
    if k == '333fm':
        return res if res < 100 else str(res)[:3]+'.'+str(res)[3:]
    elif k == '333mbf':
        return res
    else:
        return get_time(res)


def get_prs(prs: dict) -> str:
    prs_string = ''

    for k, v in prs.items():
        string = f'\n**Дисциплина {k}**:'
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

        prs_string += string

    return prs_string


async def get_wca_profile(wca_id: str) -> dict:
    async with aiohttp.request('get', BASE_URL+f'/persons/{wca_id}') as session:
        res = await session.json()

        return res if not res.get('error') else None


async def parsed_wca_profile(wca_id: str) -> dict:
    profile = await get_wca_profile(wca_id)
    # pprint(profile, indent=4)
    if not profile:
        return None

    person = profile.get('person')
    records = profile.get('records')
    medals = profile.get('medals')
    personal_records = get_prs(profile.get('personal_records'))

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
    pprint(data, indent=4)
    return data


if __name__ == '__main__':
    asyncio.run(parsed_wca_profile('2018TAKH01'))
