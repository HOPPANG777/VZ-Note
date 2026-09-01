# Hit

<p align="center">
  <img src="../../../Images/Projects/그래픽스 연습/타입/Hit.png" alt="Hit" width="720" />
</p>

| | |
| --- | --- |
| [Ray](Ray.md) | |
| [Object](Object.md) | |
| [FindClosestCollision](../교차/FindClosestCollision.md) | |

---

```cpp
class Hit
{
public:
	float distance;               // 시작점부터 교차점까지 거리. 안 맞으면 -1
	Vector3 point;                // 교차점
	Vector3 normal;               // 그 지점 법선
	Vector2 uv;                   // 텍스처 좌표
	shared_ptr<class Object> obj; // 맞은 오브젝트
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
| 미스 표시 (`distance < 0`) | 헤더에 약속만 있고, 다른 엔진은 \(t_{\max}\)를 씀 | PBRT [Rays](https://pbr-book.org/3ed-2018/Geometry_and_Transformations/Rays) |
| `obj` 초기값 | 그림자에서 `obj != nullptr`을 봄. 헤더에 안 적힘 | 이 프로젝트 `TraceRay` |
| `uv`를 누가 채우는지 | 삼각형만 채움. 구는 안 넣음 | [Triangle](../교차/Triangle.md) |
