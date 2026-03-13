from unittest.mock import MagicMock
import pytest

from src.service import UtilityService


@pytest.fixture
def mock_repository():
    return MagicMock()


@pytest.fixture
def mock_logger():
    return MagicMock()


@pytest.fixture
def utility_service(mock_repository, mock_logger):
    return UtilityService(repository=mock_repository, logger=mock_logger)


def test_process_number_prime(utility_service, mock_repository, mock_logger):
    result = utility_service.process_number(7)

    assert result == {
        "number": 7,
        "is_prime": True,
        "factorial": 5040,
    }

    mock_logger.info.assert_called_once_with("Processing number: 7")
    mock_repository.save_result.assert_called_once_with(result)