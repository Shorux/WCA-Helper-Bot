from pprint import pprint
import aiohttp
import asyncio

from config import _
BASE_URL = 'https://www.worldcubeassociation.org/api/v0'


def get_time(mils: int) -> str:
    mils *= 10
    seconds, mils = divmod(mils, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    time_str = f"{minutes}:" if minutes > 0 else ""
    time_str += f"{seconds}.{int(mils)//10}"

    return time_str


def set_res(res, k):
    if k == '333fm':
        return res if res < 100 else str(res)[:3]+'.'+str(res)[3:]
    elif k == '333mbf':
        return res
    else:
        return get_time(res)


def get_prs(prs: dict) -> str:
    pr = _['personal_record']
    prs_string = ''

    for k, v in prs.items():
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


async def get_photo(url: str) -> bytes:
    async with aiohttp.request('get', url) as session:
        return await session.read()


async def get_wca_profile(wca_id: str) -> dict | None:
    async with aiohttp.request('get', BASE_URL+f'/persons/{wca_id}') as session:
        res = await session.json()

        if res.get('error'):
            return None

        res['photo_url'] = res['person']['avatar']['url']

        return res 


async def parsed_wca_profile(profile: dict) -> dict:
    profile.pop('photo_url')

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

    return data
