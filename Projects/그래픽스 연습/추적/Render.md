# Render

<p align="center">
  <img src="../../../Images/Projects/그래픽스 연습/추적/Render.png" alt="Render" width="720" />
</p>

| | |
| --- | --- |
| [TraceRay](TraceRay.md) | 픽셀마다 부름 |
| [Ray](../타입/Ray.md) | |
| 이론 | [레이트레이싱](../../../Graphics/raytracing/Raytracing.md) · [OpenMP](../../../Language/CPP/OpenMP.md) |

---

픽셀 → 광선.

각 픽셀을 독립적으로 계산해서 병렬화 효율이 높다.
OpenMP로 루프를 병렬화하면 CPU 코어를 다 써서 렌더링 시간을 줄일 수 있다.

```cpp
Vector3 TransformScreenToWorld(const Vector2& screenPos) const
{
	float aspectRatio = float(width) / height;

	float transformedX = aspectRatio * (screenPos.x / (width - 1) * 2.0f - 1.0f);
	float transformedY = -screenPos.y / (height - 1) * 2.0f + 1.0f;

	return Vector3(transformedX, transformedY, 0.0f);
}

void Render(vector<Color>& pixels) const
{
	Vector3 eyePos(0.0f, 0.0f, -1.5f);

	fill(pixels.begin(), pixels.end(), Color());

#pragma omp parallel for
	for (int y = 0; y < height; ++y)
		for (int x = 0; x < width; ++x)
		{
			const Vector3 pixelWorldPos = TransformScreenToWorld(Vector2(float(x), float(y)));

			auto rayDir = pixelWorldPos - eyePos;
			rayDir.Normalize();

			Ray pixelRay{ pixelWorldPos, rayDir }; // 픽셀에서 나가는 광선

			pixels[size_t(x + width * y)] = TraceRay(pixelRay);
		}
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
| 핀홀 카메라 (눈, 이미지 평면, 픽셀 광선) | 코드는 있는데 카메라 모델 설명이 없음 | Wikipedia [Pinhole camera model](https://en.wikipedia.org/wiki/Pinhole_camera_model), [Ray tracing (graphics)](https://en.wikipedia.org/wiki/Ray_tracing_(graphics)) |
| 광선 시작점이 눈인지 픽셀인지 | `pixelRay` 시작이 `pixelWorldPos` | 같은 위키 |
| OpenMP가 루프를 어떻게 나누는지 | 원문은 “픽셀이 독립이라 병렬”만 있음 | [OpenMP specification](https://www.openmp.org/specifications/), Wikipedia [OpenMP](https://en.wikipedia.org/wiki/OpenMP) |
| FOV | 눈–평면 거리와 평면 크기가 FOV인데 원문에 없음 | 위키 핀홀 (초점거리 / 센서 크기) |
