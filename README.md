# VZ-Note

공부하면서 적어 둔 노트들. 어떻게 둘지는 [CONVENTION](CONVENTION.md).

## 좀 더 만진 것

그림 있거나, 연습 코드가 붙어 있는 쪽.

| | |
| --- | --- |
| [그래픽스 연습](Projects/그래픽스%20연습/그래픽스%20연습.md) | 레이트레이싱 연습. 타입 / 교차 / 추적 |
| [레이트레이싱](Graphics/raytracing/Raytracing.md) | 이론. 1차·그림자·퐁 |
| [A*](Computer-Science/algorithm/AStar.md) | `f = g + h` |
| [스마트 포인터](Language/CPP/Smart-Pointer.md) | `unique_ptr` / `shared_ptr` |
| [렌더링 파이프라인](Graphics/rendering/Rendering-Pipeline.md) | 정점 → 픽셀 |
| [Device / Swapchain](Graphics/DirectX/Device-Swapchain-RTV-Viewport.md) | DirectX 뼈대 |

돌아가는 코드는 여기 없다. 정리만 있다.

## 어디 뭐 있는지

폴더만 봐도 대충 보인다. 파일은 다 안 적는다.

### Language

- [C](Language/C/Types.md) — 타입, 구조체, `malloc`
- [C++](Language/CPP/Class.md) — 클래스, 가상함수, 바인딩, UB, STL, OpenMP, ComPtr, …
- [C#](Language/CSharp/Boxing-Unboxing.md)

### Computer-Science

- [algorithm](Computer-Science/algorithm/Algorithm.md) — A*, DFS/BFS, JPS, 복잡도
- [data-structure](Computer-Science/data-structure/Data-Structure.md) — 배열·리스트, 해시, 쿼드트리, RBT
- [memory-structure](Computer-Science/memory-structure/Memory-Structure.md) — 스택·힙, 캐시, 풀, 가상메모리
- [os](Computer-Science/os/Operating-System.md) — 커널, 스레드, 메시지 루프, 시스템 콜
- [programming-concept](Computer-Science/programming-concept/OOP.md) — OOP, FSM, IoC, 플로트, JSON, …

### Graphics

- [rendering](Graphics/rendering/Rendering-Pipeline.md) — 카메라, VP, 드로우콜, 컬링, 노멀맵
- [DirectX](Graphics/DirectX/Device-Swapchain-RTV-Viewport.md) — 스왑체인, RTV, 버퍼, 뷰포트
- [raytracing](Graphics/raytracing/Raytracing.md) — 구·삼각형 교차, closest hit, 퐁

### 나머지

- [Engine / Unity](Engine/Unity/Lifecycle.md) — 라이프사이클, 프리팹, 코루틴, GC
- [Math](Math/Normalize.md) — 정규화, 반사, 베지어, AABB, 짐벌락
- [Windows](Windows/WinMain.md) — `WinMain`, COM

### Projects

게임이나 연습에서 잘라 둔 메모.

| | |
| --- | --- |
| [그래픽스 연습](Projects/그래픽스%20연습/그래픽스%20연습.md) | 레이트레이싱 연습 노트 |
| [Genre](Projects/Genre.md) | 왜 뱀서인가 |
| [Wave / GameMode](Projects/Wave-GameMode.md) | 웨이브·시간·킬 수 |
| [Pool Manager](Projects/Pool-Manager.md) | 오브젝트 풀 |
| [Weapons](Projects/Weapons.md) | 베지어, 원 배치, Overlap |
| [Aegis](Projects/Aegis.md) | sin/cos로 도는 방패 |
| [Treasure Box](Projects/Treasure-Box.md) | 슬롯 UI |
| [Player LevelUp](Projects/Player-LevelUp.md) | 경험치 → 패널 |
