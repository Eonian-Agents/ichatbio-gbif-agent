import pytest
from dotenv import load_dotenv

from src.agent import GBIFAgent

load_dotenv()

@pytest.fixture(scope="function")
def agent():
    return GBIFAgent()
