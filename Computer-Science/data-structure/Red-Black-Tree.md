# 레드블랙트리

<p align="center">
  <img src="../../Images/Computer-Science/data-structure/Red-Black-Tree.png" alt="Red-Black-Tree" width="720" />
</p>

> 원 정리에 본문이 없다. 예상 질문에 "AVL이랑 같이 숙지"만 있다.

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> 무엇:
> - BST에 색(빨강/검정) 규칙을 붙여 높이를 대략 균형 맞추는 트리
> - 삽입/삭제/검색이 최악 O(log n)
> - C++ map/set이 보통 이걸로 구현된다 (표준은 연관 컨테이너 복잡도만 요구, 구현이 RB인 경우가 많음)
>
> 왜 필요: 개발자 기술면접 단골이라고 본인이 적어 둠.
>
> 보충할 내용:
> - 5개 속성(루트 검정, 빨강 연속 금지, 모든 경로 black-height 동일 등)
> - 삽입 시 rotate + recolor
> - AVL이랑 비교: AVL이 더 빡세게 균형, RB는 삽입/삭제가 상대적으로 덜 무거움
>
> - **출처:** CLRS (Cormen et al.) Red-Black Trees 챕터. 표준 정의에 가까운 교과서다.
> 지금은 추측으로 회전 케이스를 안 적는다. 그 책을 보고 다시 적어야 한다.
