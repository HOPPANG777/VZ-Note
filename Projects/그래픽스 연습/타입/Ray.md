# Ray

<p align="center">
  <img src="../../../Images/Projects/그래픽스 연습/타입/Ray.png" alt="Ray" width="720" />
</p>

| | |
| --- | --- |
| [Hit](Hit.md) | |
| [FindClosestCollision](../교차/FindClosestCollision.md) | |
| 이론 | [레이트레이싱](../../../Graphics/raytracing/Raytracing.md) |

---

```cpp
class Ray
{
public:
	Vector3 start; // 광선 시작점
	Vector3 dir;   // 광선 방향
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
| 광선 식 \(p(t)=o+td\), \(t\ge 0\) | `start`/`dir`/`Hit.distance`가 그 \(t\)인지 안 적혀 있음 | PBRT [Rays](https://pbr-book.org/3ed-2018/Geometry_and_Transformations/Rays) |
| `dir`가 단위 벡터인지 | 구 교차 식이 단위 방향을 씀. `Render`만 정규화함 | Wikipedia [Line–sphere intersection](https://en.wikipedia.org/wiki/Line%E2%80%93sphere_intersection) |
