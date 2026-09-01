# JPS (Jump Point Search)

<p align="center">
  <img src="../../Images/Computer-Science/algorithm/JPS.png" alt="JPS" width="720" />
</p>

> AStar를 개량한 알고리즘이다. 같이 숙지하는 것이 좋다고만 적혀 있고, 원리 본문은 없다.

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> 무엇: 균일 비용 그리드에서 A*가 대칭으로 허비하는 이웃 확장을 줄이기 위해, 특정 점프 포인트만 남기는 최적화.
> 왜 필요: 본인이 예상 질문에 적어 둠. A*랑 세트로 나온다.
>
> 보충할 내용:
> - 강제 이웃(forced neighbor)
> - jump point를 찾는 가로/세로 점프
> - 언제 A*보다 이득인지(빈 공간이 많은 그리드)
>
> - **출처:** Harabor, Grastien, "Online Graph Pruning for Pathfinding on Grid Maps", AAAI 2011. (JPS 원 논문)
> 지금은 논문 안 읽고 추측으로 안 채운다.
