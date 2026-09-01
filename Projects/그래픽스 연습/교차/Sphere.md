# Sphere — CheckRayCollision

<p align="center">
  <img src="../../../Images/Projects/그래픽스 연습/교차/Sphere.png" alt="Sphere CheckRayCollision" width="720" />
</p>

이론: [광선-구 교차](../../../Graphics/raytracing/Ray-Sphere.md)

| | |
| --- | --- |
| [FindClosestCollision](FindClosestCollision.md) | 이걸 부름 |
| [Object](../타입/Object.md) | |

---

RayTracing 프로젝트의 구는 RayTracer 생성자가 중심과 반지름, 재질 계수를 가진 Sphere 객체를 장면에 등록하고
TraceRay의 FindClosestCollision이 Sphere의 CheckRayCollision으로 광선-구 이차방정식을 풀어 얻은 교차점·법선을 기반으로
퐁 셰이딩을 계산한 픽셀 색을 화면 사각형 텍스처에 써서 표시하는 방식으로 렌더링된다.

여기서 이차방정식 물어보면
해당 방정식은 제가 완벽하게 이해하지 못하여 아직 공부하는 부분이고
구현에는 위키피디아의 라인 스피어 교차점에 있는
수식을 코드로 변환하여 구현하였다.

```cpp
Hit CheckRayCollision(const Ray& ray) const override
{
	Hit hit = Hit{ -1.0f, Vector3(), Vector3() }; // 기본값: 안 맞음

	const float b = 2.0f * (ray.dir.Dot(ray.start - center));
	const float c = (ray.start - center).LengthSquared() - radius * radius;
	const float nabla = b * b * 0.25f - c; // 판별식

	if (nabla >= 0.0f) // 실근이 있을 때
	{
		const float d1 = -b * 0.5f + sqrt(nabla);
		const float d2 = -b * 0.5f - sqrt(nabla);

		hit.distance = min(d1, d2); // 가까운 쪽
		hit.point = ray.start + hit.distance * ray.dir; // 시작점 + 방향 * 거리
		(hit.point - center).Normalize(hit.normal);     // 중심 → 교차점
	}

	return hit;
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
| 광선–구 이차방정식 유도 | 원문에 “위키 수식을 코드로 옮겼고 유도는 공부 중” | Wikipedia [Line–sphere intersection](https://en.wikipedia.org/wiki/Line%E2%80%93sphere_intersection), 이론 [광선-구 교차](../../../Graphics/raytracing/Ray-Sphere.md) |
| 직선 vs 광선, \(t\ge 0\) | 위키는 직선. `min(d1,d2)`가 음수일 수 있음 | 같은 위키 페이지 |
| `dir` 정규화 | 위키 기하해는 단위 방향 | 같은 위키 페이지 |
