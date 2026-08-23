from flask import Blueprint, jsonify, render_template, request
from .topics import PREREQUISITES, BUILTIN_COMPLEXITIES
from .algorithms import (
    complexity_series,
    factorial_trace,
    operation_count,
    reference_demo,
    two_pointer_pair,
)

bp = Blueprint("main", __name__)

@bp.get("/")
def index():
    return render_template("index.html")

@bp.get("/api/topics")
def topics():
    return jsonify(PREREQUISITES)

@bp.get("/api/builtins")
def builtins():
    return jsonify(BUILTIN_COMPLEXITIES)

@bp.get("/api/complexity")
def complexity():
    kind = request.args.get("kind", "linear")
    try:
        n = int(request.args.get("n", "32"))
        count = operation_count(kind, n)
        return jsonify({
            "kind": kind,
            "n": n,
            "operations": count,
            "series": complexity_series(kind, n),
        })
    except (ValueError, TypeError) as exc:
        return jsonify({"error": str(exc)}), 400

@bp.get("/api/recursion/factorial")
def recursion_factorial():
    try:
        value = int(request.args.get("value", "5"))
        return jsonify(factorial_trace(value))
    except (ValueError, TypeError) as exc:
        return jsonify({"error": str(exc)}), 400

@bp.get("/api/reference-demo")
def references():
    return jsonify(reference_demo())

@bp.post("/api/two-pointer")
def two_pointer():
    payload = request.get_json(silent=True) or {}
    try:
        values = [int(x) for x in payload.get("values", [])]
        target = int(payload.get("target", 0))
        if len(values) < 2:
            raise ValueError("Provide at least two numbers")
        return jsonify(two_pointer_pair(values, target))
    except (ValueError, TypeError) as exc:
        return jsonify({"error": str(exc)}), 400

@bp.post("/api/quiz/check")
def quiz_check():
    payload = request.get_json(silent=True) or {}
    answers = payload.get("answers", {})
    key = {
        "q1": "O(1)",
        "q2": "base-case",
        "q3": "dict",
        "q4": "alias",
        "q5": "O(n)",
    }
    details = {qid: answers.get(qid) == correct for qid, correct in key.items()}
    score = sum(details.values())
    return jsonify({"score": score, "total": len(key), "details": details})
