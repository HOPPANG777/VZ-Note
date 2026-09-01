# 퐁 셰이딩

<p align="center">
  <img src="../../Images/Graphics/raytracing/Phong-Shading.png" alt="Phong-Shading" width="720" />
</p>

> 이게 뭐냐면 조명계산에서 법선벡터에 쏘여진 빛에 대해서 주변광, 난반사, 반사 성분을 각 픽셀마다 계산을 해서 자연스러운 조명 표현을 하는 셰이딩 기법이다.

> [!TIP]
> **여담**
>
> Phong Shading은 Ambient, Diffuse, Specular 세 성분의 합으로 픽셀 색을 계산한다.
> Ambient는 일정한 기본 조명, Diffuse는 법선과 광원 방향 내적, Specular는 시선과 반사 벡터 내적의 거듭제곱으로 구한다.

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> 내가 안 적은 설명은 여기 넣지 않는다. 나중에 아래를 적어야 한다.

| 무엇 | 왜 | 볼 곳 |
| --- | --- | --- |
| Phong shading vs Phong reflection model | 면접에서 이름이 섞임. 한 문장으로 구분해 적어야 함 | Phong, "Illumination for Computer Generated Pictures", CACM 1975. Wikipedia [Phong shading](https://en.wikipedia.org/wiki/Phong_shading), [Phong reflection model](https://en.wikipedia.org/wiki/Phong_reflection_model) |

연습 코드: [TraceRay](../../Projects/그래픽스 연습/추적/TraceRay.md)
