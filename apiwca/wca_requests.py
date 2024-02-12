import general

from aiohttp import ClientSession

from helpers import *
from bot.extra.strings import _


BASE_URL = 'https://www.worldcubeassociation.org/api/v0'


def get_prs_string(lang: str, prs: dict, events: list = None) -> str:
    pr = _.personal_record[lang]
    prs_string = ''

    for event, v in prs.items():
        if events and event not in events:
            continue

        string = _.event[lang].format(event=event)
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


def parsed_wca_profile(lang: str, profile: dict, events: list = None) -> dict:
    person = profile.get('person')
    records = profile.get('records')
    medals = profile.get('medals')
    gender = gender_emoji(person.get('gender'))
    country = general.countries[person.get('country_iso2')]
    prs_string = get_prs_string(lang, profile.get('personal_records'), events)

    data = {
        'name': person['name'],
        'wca_id': person['id'],
        'wrs': records['world'],
        'crs': records['continental'],
        'nrs': records['national'],
        'gold': medals['gold'],
        'silver': medals['silver'],
        'bronze': medals['bronze'],
        'country': country,
        'gender': gender,
        'personal_records': prs_string
    }

    return _.statistic[lang].format(**data)


def parsed_users(lang, users: list[dict]) -> str:
    users_str = _.finded_users[lang]

    for user in users:
        gender = gender_emoji(user.get('gender'))
        country = general.countries[user.get('country_iso2')]

        data = {
            'name': user['name'],
            'wcaid': user['wca_id'],
            'gender': gender,
            'country': country
        }

        users_str += _.user[lang].format(**data)

    if lang == 'uz':
        users_str += _.follow

    return users_str


async def get_wca_profile(wca_id: str) -> dict | None:
    async with ClientSession(trust_env=True) as session:
        async with session.get(BASE_URL + f'/persons/{wca_id}') as resp:
            res = await resp.json()

            if res.get('error'):
                return None

            res['photo_url'] = res['person']['avatar']['url']

            return res


async def search_users(query: str):
    if not query:
        return None

    async with ClientSession(trust_env=True) as session:
        params = {'q': query, 'persons_table': 'true'}
        async with session.get(BASE_URL + f'/search/users', params=params) as resp:
            res = (await resp.json()).get('result')

            if len(res) > 10:
                res = res[:10]

            return res
