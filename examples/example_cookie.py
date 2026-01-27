import noble_tls
from noble_tls import Client


async def main():
    await noble_tls.update_if_necessary()
    session = noble_tls.Session(
        client=Client.NIKE_IOS_MOBILE,
        debug=True,
    )
    session.cookies.set(
        name="auth_token",
        value="1234567",
        domain=".x.com",
        expires=None,
        path="/",
    )
    session.proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888",
    }
    res = await session.get("https://x.com/i/api/graphql/flaR-PUMshxFWZWPNpq4zA/SearchTimeline")
    print("Status code:", res.status_code)
    print("Cookies:", session.cookies)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
