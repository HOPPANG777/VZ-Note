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

> [!NOTE]
> **보충**
>
> - **출처:** Bui Tuong Phong, "Illumination for Computer Generated Pictures", CACM 1975.
> 픽셀마다 법선을 보간해서 조명하는 게 Phong shading이고,
> 조명 모델 식(ambient+diffuse+specular)은 Phong reflection model이다.
> 면접에서 이름이 섞여 불린다. 둘을 한 문장으로 구분해 두면 좋다.
> - 셰이딩: 정점이 아니라 픽셀에서 조명
> - 반사 모델: I = ambient + diffuse(n·l) + specular(r·v)^n
