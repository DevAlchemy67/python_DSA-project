import pytest
from dsa_prereq_lab.algorithms import (
    factorial_trace,
    operation_count,
    reference_demo,
    two_pointer_pair,
)

def test_operation_count_models():
    assert operation_count("constant", 100) == 1
    assert operation_count("linear", 10) == 10
    assert operation_count("quadratic", 10) == 100
    assert operation_count("logarithmic", 8) == 3

def test_unknown_complexity_raises():
    with pytest.raises(ValueError):
        operation_count("exponential", 10)

def test_factorial_trace():
    result = factorial_trace(5)
    assert result["result"] == 120
    assert any(event["type"] == "base" for event in result["events"])

def test_reference_demo():
    result = reference_demo()
    assert result["same_object_original_alias"] is True
    assert result["same_object_original_copy"] is False
    assert "recursion" in result["original"]
    assert "recursion" not in result["copied"]

def test_two_pointer_pair():
    result = two_pointer_pair([11, 2, 7, 4], 9)
    assert result["found"] is True
    assert sum(result["pair"]) == 9
