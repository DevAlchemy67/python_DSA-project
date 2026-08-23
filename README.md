# DSA Launchpad — Python Prerequisite Portfolio

An interactive **Python + Flask** portfolio project that teaches and demonstrates the prerequisite concepts a computer science student should understand before going deeper into Data Structures & Algorithms.

## Why this belongs in a portfolio

This is not just a collection of solved coding problems. It demonstrates that you can connect **computer science fundamentals** with **full-stack engineering**:

- Python application architecture
- Flask routes and JSON APIs
- HTML/CSS responsive UI
- Client-side JavaScript
- Input validation
- Browser persistence with `localStorage`
- Automated tests with `pytest`
- GitHub Actions CI
- DSA prerequisite knowledge

## Prerequisite topics covered

1. **Python Core**
   - Variables, control flow, loops, functions, scope, exceptions, modules
2. **Built-in Data Structures**
   - `list`, `tuple`, `dict`, `set`, `str`, `deque`, `Counter`, `defaultdict`
3. **Big O & Complexity**
   - O(1), O(log n), O(n), O(n log n), O(n²)
   - time vs. space
   - best / average / worst case
4. **Memory & References**
   - object references, mutability, aliasing, copy behavior, call-stack mental model
5. **OOP for DSA**
   - classes, methods, composition, `__repr__`, dataclasses, invariants
6. **Recursion**
   - base case, recursive case, stack frames, unwinding, stack depth
7. **Problem-Solving Patterns**
   - linear scan, two pointers, sliding window, frequency counting, prefix accumulation
8. **Testing & Engineering**
   - assertions, edge cases, pytest, Git, GitHub Actions

## Interactive features

- Expandable prerequisite roadmap
- Big O growth visualizer
- Factorial recursion / call-stack trace
- Python reference and aliasing demo
- Searchable built-in complexity table
- Two-pointer target-pair playground
- Five-question readiness quiz
- Saved quiz score and theme using browser local storage
- Dark / light mode

## Project structure

```text
dsa-prerequisite-portfolio/
├── .github/
│   └── workflows/
│       └── tests.yml
├── dsa_prereq_lab/
│   ├── static/
│   │   ├── css/style.css
│   │   └── js/app.js
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   ├── algorithms.py
│   ├── routes.py
│   └── topics.py
├── tests/
│   ├── test_algorithms.py
│   └── test_routes.py
├── .gitignore
├── app.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Run locally

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate it

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the app

```bash
python app.py
```

Open `http://127.0.0.1:5000`.

## Run tests

```bash
pytest -q
```

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/topics` | Prerequisite roadmap |
| GET | `/api/builtins` | Python built-in complexity data |
| GET | `/api/complexity?kind=linear&n=32` | Complexity growth model |
| GET | `/api/recursion/factorial?value=5` | Recursive call trace |
| GET | `/api/reference-demo` | Aliasing and copy behavior |
| POST | `/api/two-pointer` | Two-pointer pair search |
| POST | `/api/quiz/check` | Score the readiness quiz |

## Portfolio talking points

When explaining this project in an interview, focus on:

- why hash-backed structures usually provide O(1) average lookup
- why list insertion near the front is O(n)
- why recursion consumes stack space
- why aliasing matters with mutable Python objects
- how a two-pointer algorithm replaces a nested-loop brute force approach on sorted input
- how Flask separates backend logic from the UI
- how automated tests protect behavior as the project grows

## Suggested next versions

- **v1.1:** complexity calculator for user-supplied loops
- **v1.2:** interactive stack vs heap / object-reference diagram
- **v1.3:** sliding-window visualizer
- **v2.0:** linked lists, stacks, queues, and hash table implementations
- **v3.0:** tree / graph visualizers and traversal animations
- **v4.0:** accounts + database + saved learning progress

## License

Use this project freely as a learning and portfolio foundation. Add an MIT license before publishing if you want explicit open-source terms.
