# -*- coding: utf-8 -*-
"""그래픽스 연습 / 레이트레이싱 이론 도식."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from diagram_draw import formula, hflow, save, stack, three_col, two_col, vflow  # noqa: E402

THEORY = ROOT / "Images" / "Graphics" / "raytracing"
PR = ROOT / "Images" / "Projects" / "그래픽스 연습"


def main() -> None:
    save(
        hflow(
            "Closest hit",
            ["Ray", "모든 Object", "CheckRayCollision", "가장 짧은 t", "Hit"],
        ),
        THEORY / "Closest-Hit.png",
    )
    save(
        formula(
            "Ray-Sphere",
            ["p(t) = o + t d", "|p - c|² = r²", "t에 대한 이차방정식"],
        ),
        THEORY / "Ray-Sphere.png",
    )
    save(
        vflow(
            "광선-삼각형",
            ["면 법선", "평면까지 t", "점이 삼각형 안인지", "무게중심으로 UV"],
        ),
        THEORY / "Ray-Triangle.png",
    )

    save(
        three_col(
            "그래픽스 연습",
            [
                ("타입", ["Ray", "Hit", "Object"]),
                ("교차", ["FindClosestCollision", "Sphere / Triangle / Square"]),
                ("추적", ["Render", "TraceRay"]),
            ],
        ),
        PR / "그래픽스 연습.png",
    )
    save(
        stack("Ray", ["start 시작점", "dir 방향"]),
        PR / "타입" / "Ray.png",
    )
    save(
        stack("Hit", ["distance", "point / normal / uv", "obj"]),
        PR / "타입" / "Hit.png",
    )
    save(
        stack("Object", ["amb / diff / spec", "CheckRayCollision = 0"]),
        PR / "타입" / "Object.png",
    )
    save(
        vflow(
            "가장 가까운 Hit",
            [
                "closestD = 1000, distance = -1",
                "objects 전부 검사",
                "distance >= 0 이고 더 짧으면 갱신",
                "closestHit 반환",
            ],
        ),
        PR / "교차" / "FindClosestCollision.png",
    )
    save(
        formula(
            "광선-구",
            ["p(t) = start + t * dir", "이차방정식 → d1, d2", "가까운 거리"],
        ),
        PR / "교차" / "Sphere.png",
    )
    save(
        vflow(
            "광선-삼각형",
            ["면 법선", "평면까지 t", "점이 삼각형 안인지", "무게중심으로 UV"],
        ),
        PR / "교차" / "Triangle.png",
    )
    save(
        hflow(
            "Square",
            ["삼각형 2개", "각각 CheckRayCollision", "맞은 쪽 중 가까운 것"],
        ),
        PR / "교차" / "Square.png",
    )
    save(
        three_col(
            "CheckRayCollision",
            [
                ("Sphere", ["이차방정식", "d1, d2", "가까운 쪽", "점 / 법선"]),
                ("Triangle", ["면 법선", "평면 t", "삼각형 안?", "무게중심 UV"]),
                ("Square", ["삼각형 2개", "둘 다 맞으면", "더 가까운 쪽"]),
            ],
        ),
        PR / "교차" / "CheckRayCollision.png",
    )
    save(
        hflow(
            "Render",
            ["픽셀 (x, y)", "월드 좌표", "Ray", "TraceRay"],
        ),
        PR / "추적" / "Render.png",
    )
    save(
        two_col(
            "TraceRay",
            ("1차", ["pixelRay", "FindClosestCollision", "가장 가까운 Hit"]),
            ("그림자", ["hit.point + 1e-4", "FindClosestCollision", "가리는 물체 있나"]),
        ),
        PR / "추적" / "TraceRay.png",
    )
    print("ok")


if __name__ == "__main__":
    main()
