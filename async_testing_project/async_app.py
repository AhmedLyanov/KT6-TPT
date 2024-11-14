import asyncio

async def fetch_data(delay: int = 1) -> str:
    await asyncio.sleep(delay)
    return "data"

async def process_data(delay: int = 1) -> str:
    data = await fetch_data(delay)
    return f"Processed {data}"

async def fetch_data_with_error(delay: int = 1) -> str:
    await asyncio.sleep(delay)
    raise ValueError("Failed to fetch data")

async def process_data_with_error(delay: int = 1) -> str:
    try:
        data = await fetch_data_with_error(delay)
    except ValueError as e:
        return str(e)
    return f"Processed {data}"