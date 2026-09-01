# 레이저 반사

<p align="center">
  <img src="../Images/Math/Reflect.png" alt="Reflect" width="720" />
</p>

> 레이저가 표면에 닿으면, 표면 법선을 기준으로 입사각과 반사각이 동일하도록 반사 벡터를 계산한다.
>
> 수학적으로는 입사 방향 벡터에서 법선 방향의 2배 투영값을 빼서 반사 벡터를 구하는 공식을 사용하며, Unity에서는 Vector2.Reflect로 구현 가능.

룬트레이서: Reflect, WorldToViewportPoint. 입사각 반사각.

---

> [!NOTE]
> **보충**
>
> 반사 공식: r = v - 2 n (n·v)  (n이 단위 법선, v가 입사 방향. 부호 규약은 구현마다 v가 표면으로 들어가는지 나가는지 확인)
> - **출처:** 벡터 기하. DirectX/Unity Reflect 함수 문서도 같은 식이다.
