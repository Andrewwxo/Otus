from aiohttp import ClientSession
from dataclasses import dataclass
import asyncio


@dataclass
class Service:
    name: str
    url: str
    ip_field: str

SERVICES = [
    Service("ipify", "https://api.ipify.org/?format=json", "ip"),
    Service("ip-api", "http://ip-api.com/json", "query"),
    # Service("jsonplaceholder", "https://my-json-server.typicode.com/typicode/demo", "id")
]

async def fetch_json(session: ClientSession, url: str):
    """
    
    :param session: 
    :param url: 
    :return: 
    """
    async with session.get(url) as response:
        return await response.json()

async def fetch_ip(service: Service):
    """
    
    :param service: 
    :return: 
    """
    async with ClientSession() as session:
        result = await fetch_json(session, service.url)
    return result[service.ip_field]

async def get_my_ip():
    service = SERVICES[0]
    my_id = await fetch_ip(service)

def run_main():
    asyncio.run(get_my_ip())

if __name__ == '__main__':
    run_main()
