import pytest

from main import calculate_packages


@pytest.mark.parametrize("package_count, expected", [
    (1, {'small': 1, 'medium': 0, 'large': 0}),
    (4, {'small': 0, 'medium': 1, 'large': 0}),
    (11, {'small': 1, 'medium': 0, 'large': 1}),
    (13, {'small': 0, 'medium': 1, 'large': 1}),
    (100, {'small': 1, 'medium': 0, 'large': 11}),
    # ...
])
def test_packages_for_1_piece(package_count, expected):
    assert calculate_packages(package_count) == expected
