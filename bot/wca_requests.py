import aiohttp
import asyncio
from pprint import pprint

BASE_URL = 'https://www.worldcubeassociation.org/api/v0'


async def get_wca_profile(wca_id: str) -> dict:
    async with aiohttp.request('get', BASE_URL+f'/persons/{wca_id}') as session:
        res = await session.json()

        return res if not res.get('error') else None


async def parsed_wca_profile(wca_id: str) -> dict:
    profile = await get_wca_profile(wca_id)
    pprint(profile, indent=4)


if __name__ == '__main__':
    asyncio.run(parsed_wca_profile('2021TOLI01'))
