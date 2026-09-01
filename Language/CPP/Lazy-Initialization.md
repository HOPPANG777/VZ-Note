# 게으른 초기화 (Lazy Initialization)

<p align="center">
  <img src="../../Images/Language/CPP/Lazy-Initialization.png" alt="Lazy-Initialization" width="720" />
</p>

> 리소스를 필요로 할 때까지 초기화를 미루는 전략이다.
>
> 객체나 리소스를 처음 사용할 때 초기화해서 불필요한 초기화 비용을 줄인다.
>
> 사용 빈도가 낮거나 무거운 객체를 필요할 때만 초기화해서 초기 로딩 시간을 줄이고 메모리 사용을 줄일 수 있다.
>
> 주로 싱글톤이나 캐시 처리에서 쓴다.

C++에선 함수 안 static 지역 변수가 이 패턴이랑 잘 맞는다. 처음 그 줄을 지날 때 만들어진다.
