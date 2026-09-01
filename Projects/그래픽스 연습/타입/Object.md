# Object

<p align="center">
  <img src="../../../Images/Projects/그래픽스 연습/타입/Object.png" alt="Object" width="720" />
</p>

| | |
| --- | --- |
| [Hit](Hit.md) | |
| [Sphere](../교차/Sphere.md) / [Triangle](../교차/Triangle.md) / [Square](../교차/Square.md) | CheckRayCollision |
| [TraceRay](../추적/TraceRay.md) | 재질 씀 |

---

```cpp
class Object
{
public:
	Color amb;  // ambient
	Color diff; // diffuse
	Color spec; // specular
	float alpha = 0.0f;
	float ks = 1.0f; // specular coefficient

	shared_ptr<Texture> ambTexture;
	shared_ptr<Texture> difTexture;

	virtual Hit CheckRayCollision(const Ray& ray) const = 0; // 이 오브젝트랑 광선이 교차하는지
};
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
| `amb`/`diff`/`spec`/`ks`/`alpha`가 Phong 식의 어디인지 | 이름만 있고 식과 안 맞춰 둠 | Phong, ["Illumination for Computer Generated Pictures"](https://doi.org/10.1145/360825.360839), CACM 1975. Wikipedia [Phong reflection model](https://en.wikipedia.org/wiki/Phong_reflection_model) |
| `alpha` 기본값 0 | 안 넣었을 때 스펙큘러가 어떻게 되는지 원문에 없음 | 같은 Phong 식의 지수 \(\alpha\) |
| 굴절이 없는 이유 | Whitted에는 굴절이 있음. 이 코드에는 없음 | Whitted, CACM 1980. [레이트레이싱](../../../Graphics/raytracing/Raytracing.md) |
