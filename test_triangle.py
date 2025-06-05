import pytest
from triangle import calculate_triangle_area

def test_valid_triangle_area():
    """Test the area calculation with valid inputs"""
    base = 5
    height = 7
    expected_area = 17.5  # (5 * 7) / 2
    assert calculate_triangle_area(base, height) == expected_area

def test_negative_base():
    """Test that negative base values are not accepted"""
    with pytest.raises(ValueError, match="Base must be greater than zero"):
        calculate_triangle_area(-5, 7)

def test_negative_height():
    """Test that negative height values are not accepted"""
    with pytest.raises(ValueError, match="Height cannot be negative"):
        calculate_triangle_area(5, -7)

def test_zero_base():
    """Test that zero base values are not accepted"""
    with pytest.raises(ValueError, match="Base must be greater than zero"):
        calculate_triangle_area(0, 7) 