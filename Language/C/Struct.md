# 구조체 (Struct)

<p align="center">
  <img src="../../Images/Language/C/Struct.png" alt="Struct" width="720" />
</p>

> 구조체는 int와 float과 같은 동등한 타입이다, 라고 컴파일러가 해석한다.

C에서 struct는 필드들을 붙여 놓은 사용자 정의 타입이다.
컴파일러 입장에선 int랑 똑같이 "이 크기만큼 읽고, 이 레이아웃으로 해석한다"는 타입이다.

C++로 넘어가면 struct랑 class는 거의 같고, 기본 접근만 다르다. 그 내용은 Class.md에 있다.

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> 패딩, 정렬, 비트필드까지는 여기 정리에 없다.
> 구조체 크기가 필드 합이랑 안 맞는 이유가 면접에 나오니까 Memory-Padding.md랑 같이 봐야 한다.
> 이유는 CPU가 정렬된 주소에서 읽기를 원해서 컴파일러가 빈 칸을 넣기 때문이다.
