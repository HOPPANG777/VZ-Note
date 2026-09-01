# 캐시 메모리

<p align="center">
  <img src="../../Images/Computer-Science/memory-structure/Cache.png" alt="Cache" width="720" />
</p>

> 캐시 메모리는 CPU와 RAM 사이의 고속 메모리로, 자주 쓰는 데이터를 저장해 처리 속도를 높인다.

배열이 연속 메모리라 캐시 효율이 좋다는 이야기가 여기서 나온다.
한 번 가져올 때 캐시 라인 단위로 가져오니까, 옆에 있는 다음 원소가 같이 온다.

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> L1/L2/L3, 캐시 라인 크기(흔히 64바이트), false sharing은 정리에 없다.
> 멀티스레드 최적화 질문이 나오면 false sharing이 필요하다.
> 출처는 Intel SDM Volume 3의 cache 절, 또는 CPU 벤더 최적화 매뉴얼이다.
> 지금은 "CPU랑 RAM 사이 고속 버퍼" 정도만 있다.
