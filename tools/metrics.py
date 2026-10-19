"""Простые воспроизводимые показатели оформления двух вариантов кода."""

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def code_metrics(path: Path) -> dict[str, float | int]:
    """Подсчитать длины строк и размер функций без субъективных оценок."""
    source = path.read_text(encoding="utf-8")
    lines = source.splitlines()
    tree = ast.parse(source)
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    lengths = [node.end_lineno - node.lineno + 1 for node in functions]
    return {
        "lines": len(lines),
        "over_88": sum(len(line) > 88 for line in lines),
        "max_line": max(map(len, lines), default=0),
        "functions": len(functions),
        "max_function_lines": max(lengths, default=0),
    }


if __name__ == "__main__":
    for label, file in (
        ("before", ROOT / "examples/before_format.py"),
        ("after", ROOT / "examples/after_format.py"),
    ):
        print(label, code_metrics(file))
