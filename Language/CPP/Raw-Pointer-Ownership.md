# raw 포인터 메모리 관리

<p align="center">
  <img src="../../Images/Language/CPP/Raw-Pointer-Ownership.png" alt="Raw-Pointer-Ownership" width="720" />
</p>

> 예상 질문: 성능상의 이유로 스마트포인터가 아닌 일반 포인터를 사용한다면 어떻게 메모리 관리를 하는 것이 비교적 안전하겠는가? 원 정리에 답이 비어 있다.

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> 무엇: 소유권을 타입/규칙으로 남기는 방법.
> 왜 필요: 본인이 빈칸으로 남겨 둠. 게임 루프에서 unique_ptr 오버헤드를 이유로 raw를 쓸 때 면접이 파고든다.
>
> 보충할 방향 (C++ 표준의 unique_ptr 설계가 말하는 소유권 모델, C++ Core Guidelines R.* 는 가이드라인이라 표준은 아님):
> - new/delete를 한 RAII 클래스 안에만 둔다
> - 함수가 소유권을 받을 때만 unique_ptr을 받고, 관찰만 하면 T* / T&
> - 배열은 컨테이너나 한 곳에서 delete[]
> - 소유자 없이 new를 여기저기 뿌리지 않는다
>
> Core Guidelines는 표준은 아니다. 공식에 가깝게 가려면 unique_ptr [unique.ptr] 의도(유일 소유)를 raw에 수동으로 지키는 이야기를 적으면 된다.
> 지금은 빈칸 유지하고 위 항목만 숙제다.
