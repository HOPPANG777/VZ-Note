# -*- coding: utf-8 -*-
"""각 학습 일지용 도식 스펙."""

# key: repo-relative posix path of md
# value: (kind, title, data)

SPECS = {
    "Computer-Science/memory-structure/Stack-Frame.md": (
        "stack",
        "Stack Frame",
        [
            "지역 변수(Local Variables)",
            "반환 주소값(Return Address)",
            "(있다면) 이전 함수 포인터(Old Base Pointer)",
            "매개변수(Parameters)",
        ],
    ),
    "Computer-Science/memory-structure/Memory-Structure.md": (
        "memory",
        "Process Memory",
        [
            "Kernel",
            "Stack Space : 지역 변수, 리턴 정보",
            "Unused Space",
            "Heap Space : 동적 할당",
            "BSS : 미초기화 전역",
            "Data : 초기화 전역",
            "Text : 코드, 상수",
        ],
    ),
    "Computer-Science/memory-structure/Virtual-Memory.md": (
        "hflow",
        "Virtual Memory",
        ["가상 주소", "페이지 테이블", "TLB", "물리 주소(RAM)"],
    ),
    "Computer-Science/memory-structure/Stack.md": (
        "stack",
        "Stack Memory",
        ["함수 진입 시 자동 할당", "지역 변수 / 반환 주소", "함수 종료 시 프레임 소멸", "빠르고 크기 제한 있음"],
    ),
    "Computer-Science/memory-structure/Heap.md": (
        "stack",
        "Heap Memory",
        ["new / malloc", "런타임에 크기 결정", "수동 해제 필요", "누수 / 단편화 가능"],
    ),
    "Computer-Science/memory-structure/Memory-Fragmentation.md": (
        "two",
        "Fragmentation",
        [
            ("내부 단편화", ["할당 칸 > 실제 데이터", "페이징에서 남음"]),
            ("외부 단편화", ["중간중간 구멍", "세그멘테이션에서 남음"]),
        ],
    ),
    "Computer-Science/memory-structure/Memory-Pool.md": (
        "hflow",
        "Memory Pool",
        ["미리 큰 덩어리 할당", "같은 크기 블록으로 쪼갬", "빌려쓰기", "반납"],
    ),
    "Computer-Science/memory-structure/Memory-Padding.md": (
        "stack",
        "Padding",
        ["char 1바이트", "패딩 3바이트", "int 4바이트", "sizeof > 필드 합"],
    ),
    "Computer-Science/memory-structure/Cache.md": (
        "vflow",
        "CPU Cache",
        ["CPU", "Cache (자주 쓰는 데이터)", "RAM"],
    ),
    "Computer-Science/programming-concept/Library.md": (
        "vflow",
        "Library",
        ["내 main / 루프", "필요할 때 라이브러리 호출", "제어권은 내 코드"],
    ),
    "Computer-Science/programming-concept/Framework.md": (
        "vflow",
        "Framework",
        ["프레임워크 메인 루프", "Update / Render 호출", "내가 끼워 넣은 코드"],
    ),
    "Computer-Science/programming-concept/API.md": (
        "hflow",
        "API",
        ["내 프로그램", "규칙/명령 집합", "OS / GPU / 엔진"],
    ),
    "Computer-Science/programming-concept/IoC.md": (
        "two",
        "Inversion of Control",
        [
            ("라이브러리", ["내가 호출한다", "제어 흐름 = 나"]),
            ("프레임워크", ["프레임워크가 나를 호출", "Update에 끼워 넣기"]),
        ],
    ),
    "Computer-Science/programming-concept/Parsing.md": (
        "hflow",
        "Parsing",
        ["읽기", "토큰화(렉서)", "구문 분석", "의미 분석", "변환/AST"],
    ),
    "Computer-Science/programming-concept/Serialization.md": (
        "hflow",
        "Serialize",
        ["객체", "연속 데이터(JSON 등)", "저장/전송", "역직렬화 → 객체"],
    ),
    "Computer-Science/programming-concept/Procedural.md": (
        "hflow",
        "Procedural",
        ["데이터(struct)", "함수", "다음 함수", "순차 실행"],
    ),
    "Computer-Science/programming-concept/OOP.md": (
        "three",
        "OOP",
        [
            ("캡슐화", ["숨기기", "private"]),
            ("상속", ["기능 확장"]),
            ("다형성", ["같은 호출", "다른 동작"]),
        ],
    ),
    "Computer-Science/programming-concept/Design-Pattern.md": (
        "three",
        "Design Patterns",
        [
            ("Singleton", ["인스턴스 하나", "전역 접근"]),
            ("Factory", ["생성 캡슐화"]),
            ("Observer", ["상태 변화 알림"]),
        ],
    ),
    "Computer-Science/programming-concept/FSM.md": (
        "hflow",
        "FSM",
        ["Idle", "Jump", "Fall", "Idle"],
    ),
    "Computer-Science/programming-concept/Component.md": (
        "stack",
        "Component",
        ["Entity / Object", "Move 컴포넌트", "Render 컴포넌트", "Collision 컴포넌트"],
    ),
    "Computer-Science/programming-concept/JSON.md": (
        "stack",
        "JSON",
        ['{ "hp": 10 }', "키-값 텍스트", "RFC 8259 / ECMA-404", "XML보다 가볍다"],
    ),
    "Computer-Science/programming-concept/Unicode.md": (
        "three",
        "Unicode / Encoding",
        [
            ("UTF-8", ["1~4바이트", "ASCII 호환"]),
            ("UTF-16", ["2 또는 4바이트", "Windows WCHAR"]),
            ("ANSI", ["코드 페이지", "유니코드 아님"]),
        ],
    ),
    "Computer-Science/programming-concept/Floating-Point.md": (
        "formula",
        "IEEE 754",
        ["0.1 은 2진으로 정확히 못 담음", "0.1 + 1.1  !=  1.2 일 수 있음", "같음 비교 대신 오차 범위"],
    ),
    "Computer-Science/os/Operating-System.md": (
        "vflow",
        "OS",
        ["응용 프로그램", "운영체제", "하드웨어"],
    ),
    "Computer-Science/os/Shell.md": (
        "hflow",
        "Shell",
        ["사용자 입력", "셸(명령 해석)", "커널", "결과 출력"],
    ),
    "Computer-Science/os/Kernel.md": (
        "vflow",
        "Kernel",
        ["응용 프로그램", "커널 (자원 제어)", "CPU / 메모리 / I/O"],
    ),
    "Computer-Science/os/System-Call.md": (
        "hflow",
        "System Call",
        ["유저 모드", "시스템 콜", "커널 모드", "서비스 수행"],
    ),
    "Computer-Science/os/Thread-Process.md": (
        "two",
        "Process / Thread",
        [
            ("프로세스", ["실행 중인 프로그램", "독립 주소 공간"]),
            ("스레드", ["프로세스 안 실행 단위", "메모리 공유", "동기화 필요"]),
        ],
    ),
    "Computer-Science/os/Message-Loop.md": (
        "hflow",
        "Message Loop",
        ["OS 메시지 큐", "Get/PeekMessage", "Dispatch", "윈도우 프로시저"],
    ),
    "Computer-Science/os/Event-Driven.md": (
        "vflow",
        "Event Driven",
        ["이벤트 발생 (입력/메시지)", "등록된 핸들러 실행", "다시 대기"],
    ),
    "Computer-Science/os/Handle.md": (
        "hflow",
        "Handle",
        ["유저 코드", "핸들 값", "핸들 테이블", "커널 객체"],
    ),
    "Computer-Science/os/CRT-Main.md": (
        "vflow",
        "Who calls main?",
        ["OS 로더", "CRT 시작 코드", "main()", "종료 루틴"],
    ),
    "Computer-Science/os/Context-Switching.md": (
        "hflow",
        "Context Switch",
        ["스레드 A 레지스터 저장", "스케줄러", "스레드 B 레지스터 복원"],
    ),
    "Computer-Science/os/Process-Scheduling.md": (
        "hflow",
        "Scheduling",
        ["준비 큐", "스케줄러가 하나 선택", "CPU 실행", "대기/종료"],
    ),
    "Computer-Science/os/User-vs-Kernel.md": (
        "two",
        "User / Kernel Mode",
        [
            ("유저 모드", ["응용 프로그램", "특권 명령 불가"]),
            ("커널 모드", ["OS", "하드웨어 직접 제어"]),
        ],
    ),
    "Computer-Science/data-structure/Data-Structure.md": (
        "stack",
        "Data Structure",
        ["배열 / 리스트", "스택 / 큐", "트리 / 그래프", "데이터를 어떻게 담느냐"],
    ),
    "Computer-Science/data-structure/Array.md": (
        "linked",
        "Array",
        (["[0]", "[1]", "[2]", "[3]"], "plain"),
    ),
    "Computer-Science/data-structure/Array-List.md": (
        "vflow",
        "Array List",
        ["capacity 남음 → 끝에 삽입 O(1)", "꽉 참 → 더 큰 배열 할당", "기존 원소 복사"],
    ),
    "Computer-Science/data-structure/Linked-List.md": (
        "linked",
        "Linked List",
        (["A", "B", "C", "D"], "single"),
    ),
    "Computer-Science/data-structure/Stack.md": (
        "stack",
        "Stack (LIFO)",
        ["push 3", "push 2", "push 1  ← top", "pop → 1 먼저 나옴"],
    ),
    "Computer-Science/data-structure/Queue.md": (
        "hflow",
        "Queue (FIFO)",
        ["enqueue", "앞쪽 데이터", "뒤쪽 데이터", "dequeue"],
    ),
    "Computer-Science/data-structure/Table.md": (
        "stack",
        "Table",
        ["행/열로 정리한 구조", "vtable = 함수 포인터 1차원 배열", "페이지 테이블 = 주소 맵", "해시 테이블 = 버킷 배열"],
    ),
    "Computer-Science/data-structure/List-Dictionary.md": (
        "two",
        "List / Dictionary",
        [
            ("List", ["동적 배열", "인덱스 순회"]),
            ("Dictionary", ["키 → 값", "해시 검색"]),
        ],
    ),
    "Computer-Science/data-structure/Spatial-Hash.md": (
        "grid",
        "Spatial Hash",
        [
            ["(0,1)", "(1,1)", "(2,1)"],
            ["(0,0) 오브젝트", "(1,0)", "(2,0)"],
        ],
    ),
    "Computer-Science/data-structure/Red-Black-Tree.md": (
        "vflow",
        "Red-Black Tree",
        ["BST + 색 규칙", "삽입/삭제 시 rotate", "최악 O(log n)"],
    ),
    "Computer-Science/data-structure/Grid-QuadTree.md": (
        "two",
        "Grid / Quad-tree",
        [
            ("Grid", ["칸 크기 고정", "구현 단순"]),
            ("Quad-tree", ["밀도에 따라 분할", "구현 더 복잡"]),
        ],
    ),
    "Computer-Science/algorithm/Algorithm.md": (
        "hflow",
        "Algorithm",
        ["문제", "절차(알고리즘)", "데이터 담는 법(자료구조)", "결과"],
    ),
    "Computer-Science/algorithm/AStar.md": (
        "formula",
        "A*",
        ["f = g + h", "g : 지금까지 실제 비용", "h : 목표까지 추정(휴리스틱)", "오픈리스트에서 f 최소 선택"],
    ),
    "Computer-Science/algorithm/JPS.md": (
        "hflow",
        "JPS",
        ["그리드 A*", "대칭 경로 점프", "점프 포인트만 남김", "후보 감소"],
    ),
    "Computer-Science/algorithm/DFS-BFS.md": (
        "two",
        "DFS / BFS",
        [
            ("DFS", ["스택", "깊이 우선"]),
            ("BFS", ["큐", "너비 우선", "비가중 최단"]),
        ],
    ),
    "Computer-Science/algorithm/Time-Complexity.md": (
        "stack",
        "Time Complexity",
        ["배열 접근 O(1)", "리스트 탐색 O(n)", "중간 삽입 O(n)", "입력 n이 커질 때 증가율"],
    ),
    "Computer-Science/algorithm/Manhattan-Euclidean.md": (
        "two",
        "Distance",
        [
            ("맨해튼", ["|dx| + |dy|", "축을 따라 이동"]),
            ("유클리드", ["sqrt(dx² + dy²)", "직선 거리"]),
        ],
    ),
    "Language/C/Types.md": (
        "two",
        "C Type",
        [
            ("크기", ["몇 바이트인가", "int / float ..."]),
            ("해석", ["그 비트를 어떻게 읽나", "signed / unsigned / float"]),
        ],
    ),
    "Language/C/Struct.md": (
        "stack",
        "Struct",
        ["필드들을 붙여 놓은 타입", "컴파일러에겐 int와 동등한 타입", "크기 + 레이아웃으로 해석"],
    ),
    "Language/C/Malloc-Free.md": (
        "two",
        "malloc vs new",
        [
            ("malloc / free", ["C", "바이트만", "생성자 없음"]),
            ("new / delete", ["C++", "생성자/소멸자", "배열은 new[] / delete[]"]),
        ],
    ),
    "Language/CPP/Class.md": (
        "three",
        "Class",
        [
            ("캡슐화", ["숨기기 private"]),
            ("수명", ["생성자/소멸자 RAII"]),
            ("다형성", ["virtual"]),
        ],
    ),
    "Language/CPP/Undefined-Behavior.md": (
        "stack",
        "Undefined Behavior",
        ["표준이 결과를 안 정함", "미초기화 읽기 / 범위 밖", "부호 있는 정수 오버플로", "컴파일러는 UB 없다고 가정하고 최적화"],
    ),
    "Language/CPP/Implementation-Defined-Behavior.md": (
        "stack",
        "Implementation-Defined",
        ["구현마다 다를 수 있음", "문서화 의무 있음", "예: char signed / unsigned"],
    ),
    "Language/CPP/Unspecified-Behavior.md": (
        "stack",
        "Unspecified",
        ["가능한 동작 중 하나", "문서화 의무 없음", "예: 함수 인자 평가 순서"],
    ),
    "Language/CPP/Compiler.md": (
        "hflow",
        "Compiler",
        ["소스", "가상호출 → 머신코드", "vtable 레이아웃", "심볼릭 참조"],
    ),
    "Language/CPP/Symbolic-Reference.md": (
        "hflow",
        "Symbolic Reference",
        ["이름(심볼)", "심볼 테이블", "링크/로드", "실제 주소"],
    ),
    "Language/CPP/Direct-Reference.md": (
        "hflow",
        "Direct Reference",
        ["이미 아는 주소", "중간 이름 찾기 없음", "그 번지로 접근"],
    ),
    "Language/CPP/Reference.md": (
        "stack",
        "Reference",
        ["이미 있는 객체의 별칭", "반드시 초기화", "다른 대상으로 못 바꿈", "nullptr 없음"],
    ),
    "Language/CPP/Pointer-vs-Reference.md": (
        "two",
        "Pointer / Reference",
        [
            ("포인터", ["주소 저장", "재할당 가능", "nullptr"]),
            ("레퍼런스", ["별칭", "초기화 필수", "대상 변경 불가"]),
        ],
    ),
    "Language/CPP/Overloading-Override.md": (
        "two",
        "Overload / Override",
        [
            ("오버로딩", ["같은 이름 다른 시그니처", "컴파일 타임", "네임 맹글링"]),
            ("오버라이딩", ["상속, 같은 시그니처", "런타임", "virtual"]),
        ],
    ),
    "Language/CPP/Virtual-Function.md": (
        "vflow",
        "Virtual Function",
        ["부모 포인터/참조로 호출", "객체의 실제 타입 확인", "자식 함수 실행"],
    ),
    "Language/CPP/VTable.md": ("vtable", "VTable", None),
    "Language/CPP/Dynamic-Binding.md": (
        "hflow",
        "Dynamic Binding",
        ["호출 코드", "vptr", "vtable[n]", "실제 함수"],
    ),
    "Language/CPP/Static-Binding.md": (
        "hflow",
        "Static Binding",
        ["컴파일 시점", "호출 대상 확정", "일반 멤버 함수"],
    ),
    "Language/CPP/Access-Modifier.md": (
        "three",
        "Access",
        [
            ("public", ["외부 가능"]),
            ("protected", ["파생까지"]),
            ("private", ["클래스(+friend)"]),
        ],
    ),
    "Language/CPP/Singleton.md": (
        "vflow",
        "Singleton",
        ["생성자 private", "정적 인스턴스 하나", "전역에서 그거만 씀"],
    ),
    "Language/CPP/Smart-Pointer.md": (
        "three",
        "Smart Pointer",
        [
            ("unique_ptr", ["소유권 1개", "이동만"]),
            ("shared_ptr", ["공유 + ref count"]),
            ("weak_ptr", ["관찰", "카운트 안 올림"]),
        ],
    ),
    "Language/CPP/Lazy-Initialization.md": (
        "hflow",
        "Lazy Init",
        ["아직 안 만듦", "처음 사용", "그때 초기화"],
    ),
    "Language/CPP/Function.md": (
        "stack",
        "std::function",
        ["호출 테이블", "타입 이레이져 메타데이터", "저장 버퍼 / 힙 포인터", "빈/유효 플래그", "동시 할당+호출 = 레이스"],
    ),
    "Language/CPP/Constexpr.md": (
        "two",
        "constexpr / const",
        [
            ("constexpr", ["컴파일 타임 계산", "rand() 못 넣음"]),
            ("const", ["상수성", "런타임 값 가능"]),
        ],
    ),
    "Language/CPP/Pure-Virtual-Abstract-Interface.md": (
        "vflow",
        "Abstract",
        ["virtual f() = 0", "추상 클래스 (객체 생성 불가)", "파생이 구현", "인터페이스 = 순수가상만"],
    ),
    "Language/CPP/STL.md": (
        "three",
        "STL",
        [
            ("컨테이너", ["vector list map"]),
            ("이터레이터", ["순회"]),
            ("알고리즘", ["sort find"]),
        ],
    ),
    "Language/CPP/Call-By-Value-Reference.md": (
        "two",
        "Call by",
        [
            ("Value", ["복사본 전달", "원본 안 바뀜"]),
            ("Reference", ["별칭/주소", "원본 바뀜"]),
        ],
    ),
    "Language/CPP/Lambda.md": (
        "stack",
        "Lambda",
        ["이름 없는 함수", "작은 구조체 + operator()", "캡처로 바깥 변수", "인자로 넘김"],
    ),
    "Language/CPP/Operator-Overloading.md": (
        "formula",
        "Operator Overload",
        ["a + b  →  a.operator+(b)", "클래스에 연산 의미 재정의"],
    ),
    "Language/CPP/This.md": (
        "stack",
        "this",
        ["현재 인스턴스 포인터", "멤버 vs 매개변수 구분", "메서드 체이닝"],
    ),
    "Language/CPP/Cast.md": (
        "stack",
        "C++ Cast",
        ["static_cast", "dynamic_cast", "const_cast", "reinterpret_cast"],
    ),
    "Language/CPP/Increment-Operator.md": (
        "two",
        "++ / --",
        [
            ("전위 ++x", ["먼저 변경", "그 값 반환"]),
            ("후위 x++", ["원래 값 반환", "그다음 변경"]),
        ],
    ),
    "Language/CPP/Build.md": (
        "hflow",
        "Build",
        ["전처리기", "컴파일러", "어셈블러", "링커", "실행 파일"],
    ),
    "Language/CPP/Chrono.md": (
        "three",
        "std::chrono",
        [
            ("duration", ["간격"]),
            ("time_point", ["시점"]),
            ("clock", ["steady / system"]),
        ],
    ),
    "Language/CPP/Vcpkg.md": (
        "hflow",
        "vcpkg",
        ["라이브러리 목록", "설치", "프로젝트에 연결"],
    ),
    "Language/CPP/ComPtr.md": (
        "hflow",
        "ComPtr",
        ["COM 객체", "AddRef", "사용", "소멸 시 Release"],
    ),
    "Language/CPP/OpenMP.md": (
        "hflow",
        "OpenMP",
        ["#pragma omp parallel for", "스레드에 루프 분배", "CPU 코어 사용"],
    ),
    "Language/CPP/Raw-Pointer-Ownership.md": (
        "vflow",
        "Raw Pointer",
        ["new/delete를 한 곳에만", "소유자 한 명", "관찰은 T*"],
    ),
    "Language/CSharp/Boxing-Unboxing.md": (
        "hflow",
        "Boxing",
        ["값 타입(스택)", "박싱 → 힙 객체", "언박싱 → 값 타입"],
    ),
    "Graphics/rendering/Double-Buffering.md": (
        "two",
        "Double Buffering",
        [
            ("Front", ["화면이 보는 버퍼"]),
            ("Back", ["그리는 버퍼", "완성되면 교체"]),
        ],
    ),
    "Graphics/DirectX/Swapchain.md": (
        "hflow",
        "Swap Chain",
        ["Back buffer 그리기", "Present", "Front에 표시"],
    ),
    "Graphics/rendering/Rendering-Pipeline.md": (
        "hflow",
        "Pipeline",
        ["IA 정점조립", "VS 정점변환", "RS 픽셀생성", "PS 색계산", "OM 출력병합"],
    ),
    "Graphics/DirectX/DXGI-Surface.md": (
        "stack",
        "DXGI Surface",
        ["2D 픽셀 버퍼", "스왑체인 백버퍼", "Direct2D 연동"],
    ),
    "Graphics/DirectX/Render-Target.md": (
        "two",
        "Render Target",
        [
            ("백버퍼 RTV", ["화면에 나감"]),
            ("오프스크린", ["그림자/포스트", "텍스처에 그림"]),
        ],
    ),
    "Graphics/DirectX/Device-Swapchain-RTV-Viewport.md": (
        "vflow",
        "DX Setup",
        ["Device + SwapChain", "Render Target View", "Viewport"],
    ),
    "Graphics/DirectX/Viewport.md": (
        "stack",
        "Viewport",
        ["화면에 그릴 사각형", "TopLeft / Width / Height", "RS 단계 설정"],
    ),
    "Graphics/rendering/View-Projection.md": (
        "hflow",
        "View / Projection",
        ["월드 좌표", "View (카메라)", "Projection (클립)", "화면"],
    ),
    "Graphics/rendering/Camera.md": (
        "hflow",
        "Camera",
        ["Eye / Focus / Up", "LookAtLH → View", "Ortho/Perspective"],
    ),
    "Graphics/rendering/Input.md": (
        "hflow",
        "Input per Frame",
        ["이전 프레임 키 상태", "현재 상태", "Down / Held / Up"],
    ),
    "Graphics/rendering/DeltaTime.md": (
        "formula",
        "deltaTime",
        ["이번 프레임 - 이전 프레임 (초)", "이동 = 속도 × dt", "30fps / 60fps 이동거리 맞춤"],
    ),
    "Graphics/rendering/Culling-Clipping.md": (
        "two",
        "Culling / Clipping",
        [
            ("Culling", ["안 보이는 도형 통째 제거"]),
            ("Clipping", ["화면 밖 일부 절단"]),
        ],
    ),
    "Graphics/rendering/Coordinate-System.md": (
        "two",
        "Handedness",
        [
            ("왼손 (DirectX)", ["Z가 앞"]),
            ("오른손", ["Z가 뒤"]),
        ],
    ),
    "Graphics/rendering/Draw-Call.md": (
        "vflow",
        "Draw Call",
        ["CPU가 GPU에 그리기 명령", "상태 바뀌면 비용", "배칭/인스턴싱으로 줄임"],
    ),
    "Graphics/DirectX/Vertex-Index-Buffer.md": (
        "two",
        "GPU Buffers",
        [
            ("Vertex Buffer", ["정점 위치/법선/UV"]),
            ("Index Buffer", ["정점 재사용", "사각형 = 4정점+6인덱스"]),
        ],
    ),
    "Graphics/rendering/GPU-CPU-Bound.md": (
        "two",
        "Bottleneck",
        [
            ("CPU bound", ["드로우콜 많음"]),
            ("GPU bound", ["픽셀 셰이더 무거움"]),
        ],
    ),
    "Graphics/rendering/DirectX-vs-OpenGL.md": (
        "two",
        "DX / GL",
        [
            ("DirectX", ["주로 Windows"]),
            ("OpenGL", ["여러 플랫폼"]),
        ],
    ),
    "Graphics/rendering/Normal-Map.md": (
        "stack",
        "Normal Map",
        ["가짜 법선을 텍스처에 저장", "평평한 면 = (0,0,1)", "RGB로 넣으면 파랗게 보임"],
    ),
    "Graphics/raytracing/Raytracing.md": ("rays", "Raytracing", None),
    "Graphics/raytracing/Phong-Shading.md": (
        "formula",
        "Phong",
        ["Ambient + Diffuse + Specular", "Diffuse : n · l", "Specular : (r · v)^n"],
    ),
    "Graphics/raytracing/Closest-Hit.md": (
        "hflow",
        "Closest hit",
        ["Ray", "every Object", "CheckRayCollision", "smallest t", "Hit"],
    ),
    "Graphics/raytracing/Ray-Sphere.md": (
        "formula",
        "Ray-Sphere",
        ["p(t) = o + t d", "|p - c|² = r²", "quadratic in t"],
    ),
    "Graphics/raytracing/Ray-Triangle.md": (
        "vflow",
        "Ray-Triangle",
        ["face normal", "t to plane", "point in triangle?", "barycentric UV"],
    ),
    "Projects/그래픽스 연습/그래픽스 연습.md": (
        "three",
        "그래픽스 연습",
        [
            ("타입", ["Ray", "Hit", "Object"]),
            ("교차", ["FindClosestCollision", "Sphere / Triangle / Square"]),
            ("추적", ["Render", "TraceRay"]),
        ],
    ),
    "Projects/그래픽스 연습/타입/Ray.md": (
        "stack",
        "Ray",
        ["start 시작점", "dir 방향"],
    ),
    "Projects/그래픽스 연습/타입/Hit.md": (
        "stack",
        "Hit",
        ["distance", "point / normal / uv", "obj"],
    ),
    "Projects/그래픽스 연습/타입/Object.md": (
        "stack",
        "Object",
        ["amb / diff / spec", "CheckRayCollision = 0"],
    ),
    "Projects/그래픽스 연습/교차/FindClosestCollision.md": (
        "vflow",
        "가장 가까운 Hit",
        [
            "closestD = 1000, distance = -1",
            "objects 전부 검사",
            "distance >= 0 이고 더 짧으면 갱신",
            "closestHit 반환",
        ],
    ),
    "Projects/그래픽스 연습/교차/Sphere.md": (
        "formula",
        "광선-구",
        ["p(t) = start + t * dir", "이차방정식 → d1, d2", "가까운 거리"],
    ),
    "Projects/그래픽스 연습/교차/Triangle.md": (
        "vflow",
        "광선-삼각형",
        ["면 법선", "평면까지 t", "점이 삼각형 안인지", "무게중심으로 UV"],
    ),
    "Projects/그래픽스 연습/교차/Square.md": (
        "hflow",
        "Square",
        ["삼각형 2개", "각각 CheckRayCollision", "맞은 쪽 중 가까운 것"],
    ),
    "Projects/그래픽스 연습/추적/Render.md": (
        "hflow",
        "Render",
        ["픽셀 (x, y)", "월드 좌표", "Ray", "TraceRay"],
    ),
    "Projects/그래픽스 연습/추적/TraceRay.md": (
        "two",
        "TraceRay",
        [
            ("1차", ["pixelRay", "FindClosestCollision", "가장 가까운 Hit"]),
            ("그림자", ["hit.point + 1e-4", "FindClosestCollision", "가리는 물체 있나"]),
        ],
    ),
    "Engine/Unity/Delegate.md": (
        "hflow",
        "Delegate",
        ["이벤트 발생", "등록된 메서드들", "한꺼번에 호출"],
    ),
    "Engine/Unity/Prefab.md": (
        "hflow",
        "Prefab",
        ["템플릿 에셋", "인스턴스 생성", "씬에 배치"],
    ),
    "Engine/Unity/Coroutine.md": (
        "hflow",
        "Coroutine",
        ["실행", "yield 대기", "다시 실행"],
    ),
    "Engine/Unity/Collider-Rigidbody.md": (
        "two",
        "Physics Components",
        [
            ("Collider", ["겹침/충돌 감지"]),
            ("Rigidbody", ["물리 엔진이 움직임"]),
        ],
    ),
    "Engine/Unity/Material.md": (
        "hflow",
        "Material",
        ["Shader", "텍스처/색 파라미터", "오브젝트 표면에 적용"],
    ),
    "Engine/Unity/Shader.md": (
        "hflow",
        "Shader",
        ["정점 처리", "픽셀 색/빛 계산", "GPU에서 실행"],
    ),
    "Engine/Unity/ScriptableObject.md": (
        "vflow",
        "ScriptableObject",
        ["데이터 에셋", "여러 오브젝트가 참조", "하나 고치면 전부 반영"],
    ),
    "Engine/Unity/OnGUI.md": (
        "vflow",
        "OnGUI (IMGUI)",
        ["매 프레임 다시 그림", "즉시 모드", "디버그 UI용"],
    ),
    "Engine/Unity/Garbage-Collector.md": (
        "hflow",
        "GC",
        ["참조 끊김", "쓰레기 표시", "수거 (비용 있음)"],
    ),
    "Engine/Unity/Lifecycle.md": (
        "hflow",
        "Unity Loop",
        ["Awake", "Start", "FixedUpdate", "Update", "LateUpdate"],
    ),
    "Windows/COM.md": (
        "vflow",
        "COM",
        ["바이너리 표준", "인터페이스 포인터만 접근", "IUnknown: QI / AddRef / Release"],
    ),
    "Windows/WinMain.md": (
        "three",
        "Entry",
        [
            ("WinMain", ["ANSI"]),
            ("wWinMain", ["Unicode"]),
            ("_tWinMain", ["TCHAR 매크로"]),
        ],
    ),
    "Math/BoundingBox.md": ("aabb", "AABB / OBB", None),
    "Math/Normalize.md": ("norm", "Normalize", None),
    "Math/Normal.md": (
        "stack",
        "Normal",
        ["표면에 수직인 벡터", "조명 n · l", "충돌 반사 방향"],
    ),
    "Math/Bezier.md": ("bezier", "3차 베지어", None),
    "Math/Reflect.md": (
        "formula",
        "Reflect",
        ["입사각 = 반사각", "r = v - 2 n (n·v)"],
    ),
    "Math/Gimbal-Lock.md": (
        "stack",
        "Gimbal Lock",
        ["오일러 각으로 회전", "두 축이 겹침", "자유도 감소", "해결: 쿼터니언"],
    ),
    "Projects/Pool-Manager.md": (
        "vflow",
        "Object Pool",
        ["타입별 풀", "미리 생성해서 자식으로", "빌려쓰기 / 반납"],
    ),
    "Projects/Player-LevelUp.md": (
        "hflow",
        "Level Up",
        ["XP 획득", "최대 XP 도달", "레벨 +1", "패널 호출"],
    ),
    "Projects/Aegis.md": (
        "formula",
        "Aegis Orbit",
        ["θ = 시간 × 회전속도", "x = r cosθ", "y = r sinθ"],
    ),
    "Projects/Wave-GameMode.md": (
        "vflow",
        "Wave",
        ["시간 / 킬수 기록", "STO 값과 비교", "패턴 + 몬스터 소환"],
    ),
    "Projects/Treasure-Box.md": (
        "hflow",
        "Treasure Box",
        ["이미지 2장 스크롤", "당첨 번호", "해당 아이템 업그레이드"],
    ),
    "Projects/Weapons.md": (
        "stack",
        "Weapons",
        ["베지어: 도끼/부메랑", "SinCos: 성경/화염구", "Overlap: 마늘/함정", "List 랜덤: 번개"],
    ),
    "Projects/Genre.md": (
        "stack",
        "Genre",
        ["뱀파이어 서바이벌", "시간 가는 줄 모르고 함", "그래서 만들어 보고 싶었음"],
    ),
}
