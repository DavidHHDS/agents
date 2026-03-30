#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import xml.etree.ElementTree as ET
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspecciona entidades, paquetes y notas dentro de un SVG generado por PlantUML."
    )
    parser.add_argument("svg_path", help="Ruta al archivo SVG")
    parser.add_argument(
        "--only",
        choices=["all", "entities", "clusters", "notes"],
        default="all",
        help="Filtra el tipo de elementos a mostrar",
    )
    parser.add_argument(
        "--contains",
        default=None,
        help="Solo muestra elementos cuyo nombre o texto contenga este fragmento",
    )
    return parser.parse_args()


def load_root(svg_path: Path) -> ET.Element:
    text = svg_path.read_text(encoding="utf-8")
    svg_start = text.find("<svg")
    if svg_start < 0:
        raise ValueError("El archivo no contiene un nodo <svg>")
    return ET.fromstring(text[svg_start:])


def parse_path_bounds(path_d: str) -> tuple[float, float, float, float]:
    pairs = [
        (float(x), float(y))
        for x, y in re.findall(r"[ML](-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)", path_d)
    ]

    if not pairs:
        values = [float(value) for value in re.findall(r"-?\d+(?:\.\d+)?", path_d)]
        pairs = list(zip(values[0::2], values[1::2]))

    xs = [x for x, _ in pairs]
    ys = [y for _, y in pairs]
    return min(xs), min(ys), max(xs), max(ys)


def text_preview(node: ET.Element, ns: dict[str, str]) -> str:
    texts = [text.text.strip() for text in node.findall("svg:text", ns) if text.text]
    return " | ".join(texts)


def should_print(kind: str, only: str) -> bool:
    return only == "all" or only == kind


def main() -> None:
    args = parse_args()
    svg_path = Path(args.svg_path)
    root = load_root(svg_path)
    ns = {"svg": "http://www.w3.org/2000/svg"}
    needle = args.contains.lower() if args.contains else None

    for node in root.findall('.//svg:g[@class="cluster"]', ns):
        if not should_print("clusters", args.only):
            continue
        name = node.attrib.get("data-qualified-name", "<sin-nombre>")
        rect = node.find("svg:rect", ns)
        if rect is None:
            continue
        line = (
            f"[cluster] {name} "
            f"x={rect.attrib['x']} y={rect.attrib['y']} "
            f"w={rect.attrib['width']} h={rect.attrib['height']}"
        )
        if needle and needle not in line.lower():
            continue
        print(line)

    for node in root.findall('.//svg:g[@class="entity"]', ns):
        name = node.attrib.get("data-qualified-name", "<sin-nombre>")
        preview = text_preview(node, ns)
        is_note = "GMN" in name or name.endswith("Note")
        kind = "notes" if is_note else "entities"
        if not should_print(kind, args.only):
            continue

        rect = node.find("svg:rect", ns)
        path = node.find("svg:path", ns)

        if rect is not None:
            line = (
                f"[{kind[:-1]}] {name} "
                f"x={rect.attrib['x']} y={rect.attrib['y']} "
                f"w={rect.attrib['width']} h={rect.attrib['height']}"
            )
        elif path is not None:
            x1, y1, x2, y2 = parse_path_bounds(path.attrib["d"])
            line = (
                f"[{kind[:-1]}] {name} "
                f"x={x1:.2f} y={y1:.2f} w={(x2 - x1):.2f} h={(y2 - y1):.2f}"
            )
        else:
            line = f"[{kind[:-1]}] {name}"

        if preview:
            line = f"{line} :: {preview}"

        if needle and needle not in line.lower():
            continue

        print(line)


if __name__ == "__main__":
    main()
