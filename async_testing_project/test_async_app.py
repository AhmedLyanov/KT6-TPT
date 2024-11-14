import pytest
from async_app import fetch_data, process_data, fetch_data_with_error, process_data_with_error

pytestmark = pytest.mark.asyncio

class TestAsyncApp:

    async def test_fetch_data(self):
        result = await fetch_data()
        assert result == "data"

    async def test_fetch_data_with_delay(self):
        result = await fetch_data(delay=2)
        assert result == "data"

    async def test_process_data(self):
        result = await process_data()
        assert result == "Processed data"

    async def test_process_data_with_delay(self):
        result = await process_data(delay=2)
        assert result == "Processed data"

    async def test_fetch_data_with_error(self):
        with pytest.raises(ValueError) as exc_info:
            await fetch_data_with_error()
        assert str(exc_info.value) == "Failed to fetch data"

    async def test_process_data_with_error(self):
        result = await process_data_with_error()
        assert result == "Failed to fetch data"