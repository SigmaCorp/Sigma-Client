import aiohttp


def retrieve_data(data, field):
    result = data.get(field, "Not found")
    if type(result) is dict:
        return "Not found"
    return str(result)


async def is_latest_version(current_version):
    url = "https://raw.githubusercontent.com/SigmaCorp/Sigma-Client/main/VERSION.md"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return False
            lastversion = await response.text()

    cversion_int = int("".join(current_version.split(".")))
    lversion_int = int("".join(lastversion.split(".")))

    if lversion_int > cversion_int:
        return (False, lastversion.strip())
    return (True, lastversion.strip())


async def get_changelog():
    url = "https://raw.githubusercontent.com/SigmaCorp/Sigma-Client/main/CHANGELOG.md"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return ""
            return await response.text()
