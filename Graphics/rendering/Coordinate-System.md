# 좌표계 (왼손 / 오른손)

<p align="center">
  <img src="../../Images/Graphics/rendering/Coordinate-System.png" alt="Coordinate-System" width="720" />
</p>

> 오른손 좌표계는 Z축이 뒤로 향하고, 왼손 좌표계는 앞으로 향한다. DirectX는 기본적으로 왼손 좌표계를 쓴다.

엄지 X, 검지 Y일 때 중지가 Z. 오른손이면 카메라 앞으로가 -Z인 그림이 많고, DirectX LH는 +Z가 앞이다.

---

> [!NOTE]
> **보충**
>
> - **출처:** Microsoft Learn Direct3D 좌표계 문서. Direct3D는 왼손 기본.
> OpenGL은 오른손 클립 공간이 전통이다.
> 같은 메시를 옮길 때 Z 부호/와인딩이 뒤집히는 이유가 이거다.
