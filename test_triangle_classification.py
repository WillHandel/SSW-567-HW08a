import pytest
from triagleClassification import classify_triangle

def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles_triangle():
    assert classify_triangle(3, 3, 4) == "Isosceles"
    assert classify_triangle(3, 4, 3) == "Isosceles"
    assert classify_triangle(4, 3, 3) == "Isosceles"

def test_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene and Right"
    assert classify_triangle(5, 4, 3) == "Scalene and Right"
    assert classify_triangle(4, 5, 3) == "Scalene and Right"
    assert classify_triangle(3, 5, 4) == "Scalene and Right"
    assert classify_triangle(5, 3, 4) == "Scalene and Right"
    assert classify_triangle(4, 3, 5) == "Scalene and Right"
    assert classify_triangle(5, 6, 7) == "Scalene"

def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene and Right"
    assert classify_triangle(5, 12, 13) == "Scalene and Right"
    assert classify_triangle(8, 15, 17) == "Scalene and Right"
    assert classify_triangle(7, 24, 25) == "Scalene and Right"