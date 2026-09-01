# TraceRay

<p align="center">
  <img src="../../../Images/Projects/그래픽스 연습/추적/TraceRay.png" alt="TraceRay" width="720" />
</p>

| | |
| --- | --- |
| [FindClosestCollision](../교차/FindClosestCollision.md) | 두 번 부름 |
| [Render](Render.md) | 여기서 부름 |
| 이론 | [레이트레이싱](../../../Graphics/raytracing/Raytracing.md) · [퐁 셰이딩](../../../Graphics/raytracing/Phong-Shading.md) |

---

1차 / 그림자.

교차점에서 광원을 향해 쏜다. 사이에 다른 물체가 가로막나 체크.
Hit 여부만 본다. **재귀 검사 안 한다.**

```cpp
Color TraceRay(const Ray& ray) const
{
	const Hit hit = FindClosestCollision(ray); // 이 광선이 제일 먼저 맞는 곳

	if (hit.distance >= 0.0f)
	{
		Color pointColor;

		if (hit.obj->ambTexture)
			pointColor = hit.obj->amb * hit.obj->ambTexture->SampleLinear(hit.uv);
		else
			pointColor = Color(hit.obj->amb);

		const Vector3 n = hit.normal;
		Vector3 l;
		(light.pos - hit.point).Normalize(l); // 교차점 → 광원

		Ray shadowRay = { hit.point + 1e-4f * l, l }; // 자기 자신에 바로 안 맞게 살짝 띄움

		const auto& shadowHit = FindClosestCollision(shadowRay); // 빛까지 가는 길에 뭔가 있나

		if (shadowHit.obj != nullptr &&
			shadowHit.distance <= (hit.point - light.pos).Length())
			return Color(hit.obj->amb); // 가려지면 ambient만

		const float diff = max(n.Dot(l), 0.0f);

		if (hit.obj->difTexture)
			pointColor += hit.obj->diff * diff * hit.obj->difTexture->SampleLinear(hit.uv);
		else
			pointColor += Color(hit.obj->diff * diff);

		const Vector3 r = 2.0f * n.Dot(l) * n - l;
		const float spec = pow(max((-ray.dir).Dot(r), 0.0f), hit.obj->alpha);
		pointColor += Color(hit.obj->spec * spec * hit.obj->ks);

		return pointColor;
	}

	return Color(); // 아무것도 안 맞음
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
| 그림자 광선 | FindClosest를 한 번 더 부름. Hit 여부만 봄 | Whitted, ["An Improved Illumination Model for Shaded Display"](https://doi.org/10.1145/358876.358882), CACM 1980. Wikipedia [Ray tracing (graphics)](https://en.wikipedia.org/wiki/Ray_tracing_(graphics)) |
| `hit.point + 1e-4f * l` | 자기 자신에 다시 맞는 문제 | PBRT [Managing Rounding Error](https://pbr-book.org/3ed-2018/Shapes/Managing_Rounding_Error) |
| Phong 식과 이 코드의 `diff`/`spec`/`r` | 여담에 세 성분만 있고, 코드와 항을 안 맞춰 둠 | Phong, CACM 1975. Wikipedia [Phong reflection model](https://en.wikipedia.org/wiki/Phong_reflection_model) |
| Phong shading vs Phong reflection | 이름이 섞여 불림. 한 문장으로 구분해 적어야 함 | Wikipedia [Phong shading](https://en.wikipedia.org/wiki/Phong_shading) |
| AO / 간접광 / 광원 샘플링 | 이론 원문에 있는데 이 함수는 안 쏨. 다시 적겠다고 한 부분 | PBRT [Light Sampling](https://pbr-book.org/3ed-2018/Light_Transport_I_Surface_Reflection/Sampling_Light_Sources), Wikipedia [Ambient occlusion](https://en.wikipedia.org/wiki/Ambient_occlusion) |
