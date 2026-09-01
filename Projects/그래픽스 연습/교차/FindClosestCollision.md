# FindClosestCollision

<p align="center">
  <img src="../../../Images/Projects/그래픽스 연습/교차/FindClosestCollision.png" alt="FindClosestCollision" width="720" />
</p>

이론: [가장 가까운 교차](../../../Graphics/raytracing/Closest-Hit.md)

<p align="center">
  <img src="../../../Images/Projects/그래픽스 연습/교차/CheckRayCollision.png" alt="CheckRayCollision" width="720" />
</p>

| | |
| --- | --- |
| [Ray](../타입/Ray.md) / [Hit](../타입/Hit.md) / [Object](../타입/Object.md) | 타입 |
| [Sphere](Sphere.md) / [Triangle](Triangle.md) / [Square](Square.md) | CheckRayCollision |
| [TraceRay](../추적/TraceRay.md) | 여기서 부름 |

---

FindClosestCollision은 전달받은 광선이 장면에서 어떤 객체와 가장 먼저 만나는지 찾는 함수다.

모든 객체를 검사해 가장 짧은 충돌 거리를 가진 Hit 구조체를 반환하며, 여기엔 교차점, 법선, 텍스처 좌표 등 셰이딩에 필요한 정보가 담긴다.

```cpp
Hit FindClosestCollision(const Ray& ray) const
{
	float closestD = 1000.0f; // 지금까지 본 가장 가까운 거리. 큰 값으로 시작
	Hit closestHit = Hit{ -1.0f, Vector3(), Vector3() }; // distance < 0 이면 아직 안 맞음

	for (const auto& obj : objects)
	{
		auto hit = obj->CheckRayCollision(ray); // 이 오브젝트와의 교차

		if (hit.distance >= 0.0f) // 맞은 경우만
		{
			if (hit.distance < closestD) // 더 가까우면 교체
			{
				hit.obj = obj;
				closestHit = hit;
				closestD = closestHit.distance;
				closestHit.uv = hit.uv;
			}
		}
	}

	return closestHit;
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
| 왜 “가장 가까운” 교차인지 | 원문은 함수가 하는 일만 있음. 1차 가시성 이유가 없음 | Whitted, ["An Improved Illumination Model for Shaded Display"](https://doi.org/10.1145/358876.358882), CACM 1980 |
| closest-hit / any-hit | 1차는 가장 가까운 점, 그림자는 가리는지만 보면 됨 | Microsoft Learn [Closest-hit shader](https://learn.microsoft.com/en-us/windows/win32/direct3d12/closest-hit-shader), [Any-hit shader](https://learn.microsoft.com/en-us/windows/win32/direct3d12/any-hit-shader) |
| `closestD = 1000` | 무한대 대신 큰 수. 왜 1000인지 원문에 없음 | PBRT [Rays](https://pbr-book.org/3ed-2018/Geometry_and_Transformations/Rays)의 `tMax` |
