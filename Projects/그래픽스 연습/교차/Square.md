# Square — CheckRayCollision

<p align="center">
  <img src="../../../Images/Projects/그래픽스 연습/교차/Square.png" alt="Square CheckRayCollision" width="720" />
</p>

| | |
| --- | --- |
| [Triangle](Triangle.md) | 삼각형 2개 |
| [FindClosestCollision](FindClosestCollision.md) | 이걸 부름 |

---

사각형 (삼각형 2개).

```cpp
Hit CheckRayCollision(const Ray& ray) const override
{
	const auto& hit1 = triangle1.CheckRayCollision(ray);
	const auto& hit2 = triangle2.CheckRayCollision(ray);

	if (hit1.distance >= 0.0f && hit2.distance >= 0.0f)
		return hit1.distance < hit2.distance ? hit1 : hit2; // 둘 다 맞으면 가까운 쪽
	else if (hit1.distance >= 0.0f)
		return hit1;
	else
		return hit2;
}
```

---

### 내가 적을 칸

> _여기에_

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> 내가 안 적은 설명은 여기 넣지 않는다. 나중에 아래를 적어야 한다.

| 무엇 | 왜 | 볼 곳 |
| --- | --- | --- |
| 쿼드를 삼각형 2개로 나누는 이유 | 원문은 “삼각형 2개”만 있음 | Wikipedia [Polygon mesh](https://en.wikipedia.org/wiki/Polygon_mesh) |
| 네 점이 한 평면인지 | 공면이 아니면 두 삼각형이 접힘. 원문에 없음 | 이 생성자의 `v0..v3` |
