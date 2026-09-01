# 컨텍스트 스위칭

<p align="center">
  <img src="../../Images/Computer-Science/os/Context-Switching.png" alt="Context-Switching" width="720" />
</p>

> 원 정리에 내용이 없다. 예상 질문에 "(어려움)"으로만 있다.

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> 무엇: CPU가 한 스레드 실행 맥락을 저장하고 다른 스레드 맥락을 복원하는 과정.
> 왜 필요: 스레드/프로세스 질문 다음에 바로 나온다. "전환 비용"을 말하려면 이게 뭔지 있어야 한다.
>
> 보충할 내용:
> - 저장하는 것: 레지스터, 프로그램 카운터, 스택 포인터, (프로세스 전환이면) 주소 공간/페이지 테이블
> - 스레드 전환 vs 프로세스 전환 비용 차이
> - Windows: Microsoft Learn Thread Context (`GetThreadContext`가 보여주는 그 컨텍스트)
>
> 출처는 OS 교과서의 context switch 절, Intel SDM의 레지스터 상태, Windows Thread Context 문서.
> 지금은 추측으로 안 채운다.
