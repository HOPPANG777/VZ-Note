# 심볼릭 참조

<p align="center">
  <img src="../../Images/Language/CPP/Symbolic-Reference.png" alt="Symbolic-Reference" width="720" />
</p>

> 심볼릭 참조란 실제 메모리 주소가 아니라 이름을 통해 대상에 접근하는 방식이다.
>
> 그러니까 컴파일될 때 클래스나 변수 같은 식별자는 심볼, 그러니까 이름으로 심볼 테이블에 기록된다.
>
> 이 기록된 심볼들로 해당 클래스에 접근하게 된다면 이 심볼을 통해 대상에 접근하게 된다는 소리다.

쉽게 말하면 "이 이름 어디 있는지 찾아라"다.
실제 주소는 링크/로드 때 붙는다.

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> 링커가 relocation을 어떻게 고치는지는 정리에 없다.
> ELF/PE 심볼 테이블, relocation entry 같은 건 오브젝트 파일 포맷 문서가 필요하다.
> 이유는 심볼릭 참조라는 말이 컴파일러/링커/Java constant pool에서 조금씩 다르게 쓰여서다.
> C++ 기준으로는 링커 문서(PE: Microsoft PE Format, ELF: System V ABI)를 보고 한 단계만 더 적으면 된다.
