from __future__ import annotations
import math

def operation_count(kind: str, n: int) -> int:
    """Return a simple operation-count model for visualizing growth rates."""
    n = max(1, int(n))
    models = {
        "constant": 1,
        "logarithmic": max(1, math.ceil(math.log2(n))),
        "linear": n,
        "linearithmic": max(1, math.ceil(n * math.log2(n))),
        "quadratic": n * n,
    }
    if kind not in models:
        raise ValueError("Unsupported complexity kind")
    return models[kind]

def complexity_series(kind: str, n: int) -> list[dict[str, int]]:
    points = sorted(set([1, 2, 4, 8, 16, 32, 64, 128, max(1, n)]))
    points = [x for x in points if x <= max(128, n)]
    return [{"n": x, "operations": operation_count(kind, x)} for x in points]

def factorial_trace(value: int) -> dict:
    """Return factorial plus a trace that resembles call-stack push/pop behavior."""
    if value < 0 or value > 10:
        raise ValueError("value must be between 0 and 10")

    events: list[dict] = []

    def factorial(n: int, depth: int = 0) -> int:
        events.append({"type": "call", "n": n, "depth": depth, "label": f"factorial({n})"})
        if n <= 1:
            events.append({"type": "base", "n": n, "depth": depth, "label": "base case → 1"})
            result = 1
        else:
            result = n * factorial(n - 1, depth + 1)
        events.append({"type": "return", "n": n, "depth": depth, "result": result, "label": f"return {result}"})
        return result

    result = factorial(value)
    return {"input": value, "result": result, "events": events}

def reference_demo() -> dict:
    original = ["array", "hash map"]
    alias = original
    copied = original.copy()
    alias.append("recursion")
    return {
        "original": original,
        "alias": alias,
        "copied": copied,
        "same_object_original_alias": original is alias,
        "same_object_original_copy": original is copied,
        "explanation": (
            "alias and original reference the same list, so mutating through alias changes original. "
            "copied is a different list object."
        ),
    }

def two_pointer_pair(values: list[int], target: int) -> dict:
    """Find a pair in a sorted copy using the two-pointer pattern."""
    nums = sorted(values)
    left, right = 0, len(nums) - 1
    steps = []
    while left < right:
        total = nums[left] + nums[right]
        steps.append({"left": left, "right": right, "a": nums[left], "b": nums[right], "sum": total})
        if total == target:
            return {"found": True, "pair": [nums[left], nums[right]], "sorted": nums, "steps": steps}
        if total < target:
            left += 1
        else:
            right -= 1
    return {"found": False, "pair": None, "sorted": nums, "steps": steps}
