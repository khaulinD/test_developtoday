import httpx
from src.core.logger import get_logger


logger = get_logger(__name__)


async def async_get(
    url: str, params: dict = None, headers: dict = None
) -> dict:
    """
    Perform an asynchronous GET request.

    Args:
        url (str): The URL to send the GET request to.
        params (dict, optional): Optional dictionary of query parameters to send in the request.
        headers (dict, optional): Optional dictionary of headers to include in the request.

    Returns:
        dict: The response data as a JSON object.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()


async def async_post(
    url: str, data: dict = None, headers: dict = None
) -> dict:
    """
    Perform an asynchronous POST request.

    Args:
        url (str): The URL to send the POST request to.
        data (dict, optional): Optional dictionary of form data to send in the request.
        headers (dict, optional): Optional dictionary of headers to include in the request.

    Returns:
        dict: The response data as a JSON object.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=data, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
