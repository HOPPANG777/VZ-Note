# Triangle — CheckRayCollision

<p align="center">
  <img src="../../../Images/Projects/그래픽스 연습/교차/Triangle.png" alt="Triangle CheckRayCollision" width="720" />
</p>

이론: [광선-삼각형 교차](../../../Graphics/raytracing/Ray-Triangle.md)

| | |
| --- | --- |
| [FindClosestCollision](FindClosestCollision.md) | 이걸 부름 |
| [Square](Square.md) | 삼각형 2개로 씀 |

---

```cpp
Hit CheckRayCollision(const Ray& ray) const override
{
	Hit hit = Hit{ -1.0f, Vector3(), Vector3() };

	Vector3 point, faceNormal;
	float t, w0, w1;

	if (IntersectRayTriangle(ray.start, ray.dir, v0, v1, v2, point, faceNormal, t, w0, w1))
	{
		hit.distance = t;
		hit.point = point;
		hit.normal = faceNormal;
		hit.uv = uv0 * w0 + uv1 * w1 + uv2 * (1.0f - w0 - w1); // 무게중심으로 UV
	}

	return hit;
}

bool IntersectRayTriangle(
	const Vector3& origin,
	const Vector3& dir,
	const Vector3& v0,
	const Vector3& v1,
	const Vector3& v2,
	Vector3& point,
	Vector3& faceNormal,
	float& t,
	float& w0,
	float& w1
) const
{
	((v1 - v0).Cross(v2 - v0)).Normalize(faceNormal); // 면 법선

	if (-dir.Dot(faceNormal) < 0.0f) return false;           // 뒷면
	if (abs(dir.Dot(faceNormal)) < 1e-2f) return false;      // 거의 평행

	t = (v0.Dot(faceNormal) - origin.Dot(faceNormal)) / dir.Dot(faceNormal); // 평면까지 거리
	if (t < 0.0f) return false; // 광선 반대편

	point = origin + t * dir;

	const Vector3 cross0 = (v2 - v1).Cross(point - v1);
	const Vector3 cross1 = (v0 - v2).Cross(point - v2);
	const Vector3 cross2 = (v1 - v0).Cross(point - v0);

	if (faceNormal.Dot(cross0) < 0.0f ||
		faceNormal.Dot(cross1) < 0.0f ||
		faceNormal.Dot(cross2) < 0.0f)
		return false; // 삼각형 밖

	const float area0 = cross0.Length();
	const float area1 = cross1.Length();
	const float area2 = cross2.Length();
	const float areaSum = area0 + area1 + area2;

	w0 = area0 / areaSum;
	w1 = area1 / areaSum;
	// area0, 1, 2를 구하고
	// areaSum을 구하고
	// w0, w1을 구함

	return true;
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
| 광선–평면 교차 (\(t\) 공식) | 삼각형 검사 전에 평면까지 거리를 구함 | Wikipedia [Line–plane intersection](https://en.wikipedia.org/wiki/Line%E2%80%93plane_intersection) |
| 점이 삼각형 안인지 / 무게중심 좌표 | `cross` 세 번이랑 `w0, w1`. UV도 여기서 보간 | Wikipedia [Barycentric coordinate system](https://en.wikipedia.org/wiki/Barycentric_coordinate_system) |
| 뒷면 버리기 | `-dir.Dot(faceNormal)`이 왜 뒷면인지 원문에 한 줄뿐 | Wikipedia [Back-face culling](https://en.wikipedia.org/wiki/Back-face_culling) |
| 이 코드 vs Möller–Trumbore | 이름이 자주 붙는데, 같은 알고리즘인지 구분해 적어야 함 | Wikipedia [Möller–Trumbore intersection algorithm](https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm), Möller & Trumbore, *Journal of Graphics Tools* 1997 |
