# Raytracing 구체 구현

<p align="center">
  <img src="../../Images/Graphics/raytracing/Sphere.png" alt="Sphere" width="720" />
</p>

> RayTracing 프로젝트의 구는 RayTracer 생성자가 중심과 반지름, 재질 계수를 가진 Sphere 객체를 장면에 등록하고 TraceRay의 FindClosestCollision이 Sphere의 CheckRayCollision으로 광선-구 이차방정식을 풀어 얻은 교차점·법선을 기반으로 퐁 셰이딩을 계산한 픽셀 색을 화면 사각형 텍스처에 써서 표시하는 방식으로 렌더링된다.

> [!TIP]
> **여담**
>
> 여기서 이차방정식 물어보면
> 해당 방정식은 제가 완벽하게 이해하지 못하여 아직 공부하는 부분이고
> 구현에는 위키피디아의 라인 스피어 교차점에 있는
> 수식을 코드로 변환하여 구현하였다.

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> 광선-구 교차는 표준 기하 문제라서 위키만 보기보다 수식을 한 번 전개해서 적는 게 맞다.
> 광선 p(t) = o + t d, 구 |x - c|^2 = r^2 를 대입하면 t에 대한 이차방정식.
> 판별식 >= 0이면 교차, 작은 양의 t가 가까운 히트.
>
> - **출처:** 기하적으로는 이차식 근의 공식. PBRT / Real-Time Rendering도 같은 전개다.
> 지금은 "위키 수식을 코드로 옮겼고 유도는 공부 중"이 정직한 상태다. 유도만 노트에 추가하면 이 파일이 완성된다.
