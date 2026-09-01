# constexpr

<p align="center">
  <img src="../../Images/Language/CPP/Constexpr.png" alt="constexpr" width="720" />
</p>

> 컴파일 타임에 값을 계산할 수 있다. (가능하다)

```cpp
constexpr int x = 10;       // 리터럴
constexpr int y = x + 5;    // constexpr끼리 계산
const int z = rand();       // const는 런타임에 값이 결정될 수 있다
constexpr int w = rand();   // 안 됨. constexpr은 컴파일 타임
```

```cpp
constexpr int square(int n)
{
    return n * n;
}

constexpr int result = square(5); // 25. 컴파일 때 결정
```

## 제한

| 버전 | |
| --- | --- |
| **C++11** | 단일 리턴문. if 안 됨. 리터럴 타입. 재귀는 되는데 복잡한 로직은 제한 |
| **C++14~** | if, for 가능. 제한 대부분 해제 |

그래도 컴파일타임 함수라서 런타임 함수가 들어가면 당연히 터진다.

쓰는 이유: 런타임 계산을 컴파일 타임으로 옮기니까 부하가 줄어든다. 타입 검증에도 쓴다.

---

> [!NOTE]
> **보충**
>
> - **출처:** C++11 `[dcl.constexpr]`, 이후 완화, 현재 draft `[dcl.constexpr]`, `[expr.const]`
>
> constexpr 변수는 핵심 상수 표현식으로 초기화돼야 한다.
> `rand()`는 상수 표현식이 아니라서 `constexpr int w = rand();`는 잘못된 프로그램이다. "터진다"가 그 말이다.
>
> `const`는 상수성이지 컴파일 타임 계산 보장이 아니다. `const int z = rand();`가 그 차이다.

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> C++20 `constexpr` virtual, `consteval`, `constinit`는 정리에 없다.
> 최신 컴파일러 쓰면 면접에 나올 수 있어서, 필요하면 `[dcl.constexpr]`을 보고 한 줄씩만 추가하면 된다.
