# 뷰포트

<p align="center">
  <img src="../../Images/Graphics/DirectX/Viewport.png" alt="Viewport" width="720" />
</p>

> 뷰포트는 GPU가 렌더링한 장면을 화면의 어느 영역에 출력할지 정하는 사각형 영역이다.

클립 공간에서 온 좌표를 픽셀 좌표로 바꿀 때 이 사각형을 쓴다.
분할 화면이면 뷰포트를 여러 개 쓰기도 한다.

---

> [!NOTE]
> **보충**
>
> - **출처:** Microsoft Learn — D3D11_VIEWPORT
> TopLeftX/Y, Width, Height, MinDepth, MaxDepth.
> RS 단계 설정이다.
