# 연산자 오버로딩

<p align="center">
  <img src="../../Images/Language/CPP/Operator-Overloading.png" alt="Operator-Overloading" width="720" />
</p>

> 이게 뭐냐면 쉽게 이야기해서 클래스에 연산자를 사용할 때 예) `MyClass = MyClass2;` | `MyClass1 = MyClass1 + 10;` 이런 식일 때 작동할 기능을 재정의하는 것이다.

`operator+`, `operator=` 같은 멤버 또는 비멤버 함수를 정의하는 거다.

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> 어떤 연산자는 오버로드가 안 된다. `.` `::` `?:` `sizeof` 같은 거.
> - **출처:** [over.oper]
> 대입은 멤버여야 한다는 규칙도 있다.
> 지금은 개념만 있고 규칙 목록이 없으니, 직접 오버로드를 작성할 때 [over.oper]을 보고 표만 추가하면 된다.
