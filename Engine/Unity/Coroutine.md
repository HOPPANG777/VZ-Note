# 코루틴

<p align="center">
  <img src="../../Images/Engine/Unity/Coroutine.png" alt="Coroutine" width="720" />
</p>

> 유니티에서 코루틴은 프로그램을 일시 정지하고, 나중에 다시 실행할 수 있도록 하는 기능이다.
>
> 일시 중지 및 실행을 반복하는 작업을 구현하거나, 복잡한 작업을 분할하여 처리하는 데 쓴다.
>
> 예를 들자면 게임에 대기 시간을 주어 메시지를 표기하거나 초기화하는 등의 작업에 사용할 수 있다.

매 프레임 전부 막는 게 아니라 yield로 제어를 돌려준다.

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> IEnumerator, yield return WaitForSeconds, 실제로는 메인 스레드에서 재개된다는 점이 정리에 없다.
> 멀티스레드가 아니다. Unity 매뉴얼 Coroutines를 보고 그 한 줄만 추가하면 면접에서 안 헷갈린다.
