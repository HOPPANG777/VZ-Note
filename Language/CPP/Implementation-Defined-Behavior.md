# Implementation-Defined Behavior (구현체 정의 행동)

<p align="center">
  <img src="../../Images/Language/CPP/Implementation-Defined-Behavior.png" alt="Implementation-Defined-Behavior" width="720" />
</p>

> 각 컴파일러 구현체(implementation)가 특정 동작 방식을 문서화하도록 요구되는 경우.

### 결과

컴파일러마다 결과가 다를 수 있지만, 각 컴파일러의 문서에 명확하게 정의되어 있다.

### 예시

char 자료형의 부호 여부 (signed/unsigned).

---

> [!NOTE]
> **보충**
>
> - **출처:** C++ working draft [defns.impl.defined]
> implementation-defined behavior = well-formed 프로그램과 올바른 데이터에 대해, 구현에 따라 달라지고, 각 구현이 문서화해야 하는 행동.
>
> unspecified랑 차이는 "문서화 의무가 있다"는 점이다.
> char가 signed인지 unsigned인지는 구현체 정의가 맞다.
