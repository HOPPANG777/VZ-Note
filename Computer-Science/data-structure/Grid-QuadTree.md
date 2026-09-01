# 공간분할 Grid vs Quad-tree

<p align="center">
  <img src="../../Images/Computer-Science/data-structure/Grid-QuadTree.png" alt="Grid-QuadTree" width="720" />
</p>

> 공부는 완벽하게 끝난 단계라고 하기 어렵다.
>
> 프로젝트에서 최적화를 목표로 Grid와 Quad-tree를 비교 분석하며 학습했다.
>
> Grid 방식은 단순하지만 직관적으로 적용할 수 있어서 프로젝트에서 실제로 구현해 보았고, 이 과정에서 장단점을 체감할 수 있었다.
>
> Quad-tree는 복잡한 동적 환경에서 더 유리하다는 것을 이해했지만, 시간 제약 때문에 직접 구현하지는 못했다.

Grid는 정적 환경에서 단순하고 효율적이며, Quad-tree는 객체 밀도 변화에 적응적이다.
Quad-tree는 구현 난이도가 더 높아 현재 프로젝트의 요구 사항과 시간 안에서는 Grid 기반으로 충분히 해결할 수 있었다.

공간 분할 외에 오브젝트 풀링이나 Update 호출 수를 줄이는 방식으로도 최적화를 시도했다.

Spatial-Hash.md가 격자 쪽 상세다.

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> Quad-tree 분할 조건, 재삽입, 동적 객체 처리는 구현을 안 해서 노트에 없다.
> 다음에 자료 보고 채울 부분이다. 출처는 Finkel & Bentley, "Quad Trees", Acta Informatica 1974 또는 그래픽스 교과서 공간분할 챕터.
