# Pool_Manager (오브젝트 풀링)

<p align="center">
  <img src="../Images/Projects/Pool-Manager.png" alt="Pool-Manager" width="720" />
</p>

> Pool Manager 아래에 유닛 타입별로 풀을 생성하고, 각 풀에 미리 유닛 오브젝트를 생성하여 자식으로 추가하였다.

GC/new를 매 소환마다 안 나가게 하려는 거다. Memory-Pool.md랑 같은 생각, 오브젝트 단위다.
