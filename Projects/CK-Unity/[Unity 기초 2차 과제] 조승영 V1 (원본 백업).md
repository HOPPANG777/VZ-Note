## 코드가 엉킬 때 꺼내 쓰는 Unity 디자인 패턴 3가지

> 한 줄 소개 : 싱글톤, 의존성 주입, 전략 패턴을 하나의 미니 게임으로 배워봅시다!

### 0. 이 글에서 다루는 내용
- 대상 독자 : 디자인 패턴을 처음 접하는 분
- 개발 환경 : Unity 6, C#
- 예제 프로젝트 한 줄 설명 :
- 목차 :
	- 디자인 패턴이란?
	- 싱글톤
	- 의존성 주입
	- 전략 패턴
	- 세 패턴 한눈에 비교
	- 마무리

### 1. 디자인 패턴이란?
#### 왜 필요할까?
디자인 패턴은 프로그래밍에서 흔히 발생하는 문제에 대한 
일반적이고 재사용 가능한 해결책 입니다.

또한 디자인 패턴은 소스 코드에 직접 이식하는 엄격한 구조가 아닌
특정 문제를 해결하기 위한 설명 또는 템플릿으로 
공식화된 모범 사례 들을 뜻합니다.

... 라고 하면 뭐라는지 모르겠죠? 

비유를 들자면, 논문이나 보고서를 쓸 때를 떠올려 보세요!

백지에서 시작하면 무엇부터 써야 할지 막막하지만,
"서론 → 본론 → 결론" 같은 모범 양식을 가져다 쓰면 훨씬 수월합니다.
양식이 내용을 대신 써주지는 않지만, 뼈대를 잡아주기 때문이죠.

디자인 패턴도 똑같아요.
코드를 짜다 반복해서 마주치는 문제에는, 먼저 겪은 사람들이 다듬어 둔 모범 구조가 있어요.

게임을 만들다 보면 이런 일이 생길거에요.
점수를 관리하는 ScoreManager가 씬을 옮길 때마다 하나 더 생겨서 점수가 꼬이거나
점수 계산 방식이 늘어날 때마다 `if (모드 == 기본) ... else if (모드 == 하드) ...`가 끝없이 길어지는 등
혼자 끙끙대며 고치기도 하지만, 사실 이런 문제는 
**이미 수많은 개발자가 겪었고, 잘 정리된 해법**이 있습니다.

이 해법에 이름을 붙여 둔 것이 바로 디자인 패턴입니다.

#### 이 글의 흐름
싱글톤 -> 의존성 주입 -> 전략 패턴

1. **싱글톤** : 어디서든 접근할 수 있는 "하나뿐인 객체"를 만든다. 편하다.

2. **의존성 주입** : 그런데 너무 편하게 쓰면 코드가 서로 단단히 엮인다. 그 엮임을 푸는 방법이다.

3. **전략 패턴** : 엮임이 풀리면, 동작(점수 계산 방식 등)을 부품처럼 갈아 끼울 수 있다.

앞 패턴의 아쉬운 점을 다음 패턴이 해결하는 순서라, 이어서 읽으면 이야기처럼 이해될꺼에요!

자, 그럼... 이제 시작해볼까요!

### 2. 싱글톤 (Singleton)
#### 2-1. 이런 문제 겪어본 적 있나요?
앞에서 이런 예시를 보셨을 거예요.

> 점수를 관리하는 ScoreManager가 씬 을 옮길 때마다 하나 더 생겨서 점수가 꼬인다

아마 여러분도 이런 문제를 한 번쯤은 겪어 보셨을 거라고 생각해요.
이처럼 공통적이고 한꺼번에 관리해야 하는 무언가를 다룰 때,
"아, 이거 또 생기면 안 되는데... 하나만 있어야 하는데..." 하고 생각했던 관리자나 로직이 있을 거예요!
GameManager, AudioManager, SaveManager 같은 것들이 대표적인 예시죠!

#### 2-2. 개념 한 줄 요약
싱글톤은 객체가 하나만 있도록 강제하고, 어디서든 그 객체를 부를 수 있게 하는 패턴이에요!

비유를 들자면, 마을의 공동 우물을 생각해 봐요!
우물을 만드는 데는 비용이 많이 들고, 집마다 하나씩 만들기엔 너무 번거롭죠.
그래서 마을에 우물을 딱 하나만 만들고, 마을 사람들이 모두 그 우물을 같이 쓰는 거예요!

#### 2-3. 구조
```
ScoreManager
 ㄴ static instance; 
 ㄴ Awake();
 ㄴ AddScore(int score); 
```

#### 2-4. 예제 코드
```csharp
using UnityEngine;

// 전역적으로 점수를 관리해요.
public class ScoreManager : MonoBehaviour
{
    public static ScoreManager instance { get; private set; }
    public int Score { get; private set; }

    private void Awake()
    {
        // 이미 다른 인스턴스가 있다면 나는 필요 없으니 제거해요
        if (instance != null && instance != this)
        {
            Destroy(gameObject);
            return;
        }

        instance = this;
        DontDestroyOnLoad(gameObject); // 씬이 바뀌어도 유지
    }

    public void AddScore(int amount)
    {
        Score += amount;
    }
}
```


사용하는 쪽에서는 이렇게 쓰면 돼요.

```csharp
ScoreManager.instance.AddScore(10);
```

알아두면 좋은 것은 세 가지예요.
1.  `static Instance` : 어디서든 접근하는 통로
2. `Awake()`에서 중복 제거 : "하나만" 보장하는 부분
3. `DontDestroyOnLoad` : 씬이 바뀌어도 유지

#### 2-5. 실행 결과
![[Pasted image 20261024193354.png]]
씬 이동

![[스크린샷 2026-10-24 193335.png]]
씬 이동해도 그대로 있죠?
아이 좋아~
#### 2-6. 장단점과 주의점
우물 비유를 이어서 장단점을 살펴볼게요!

마을 사람 누구나 우물에서 물을 길어 올 수 있듯이, 싱글톤의 가장 큰 장점은 접근이 쉽다는 거예요. 코드에서도 `ScoreManager.Instance.AddScore(10)` 한 줄이면 어디서든 점수를 올릴 수 있고, 우물이 하나뿐이라 헷갈릴 일이 없는 것처럼 점수도 한 곳에만 쌓여서 꼬일 일이 없어요!

하지만 단점도 있어요. 누구나 쓰는 우물이라 누가 얼마나 쓰는지 알기 어려운 것처럼, 싱글톤도 어디서든 접근할 수 있다 보니 누가 값을 바꿨는지 추적하기가 힘들어요. 또 우물이 고장 나면 마을 전체가 곤란해지듯이, ScoreManager에 문제가 생기면 이걸 쓰는 모든 코드가 영향을 받아요.

그래서 편하다고 우물을 여기저기 파면 의미가 없듯이, 정말 하나만 필요한 곳에만 쓰는 게 좋아요. 마지막으로 우물이 완성되기 전이나 사라진 뒤에는 물을 길을 수 없는 것처럼, `Awake()` 순서나 게임 종료 시점에 `Instance`를 부르면 오류가 날 수 있으니 조심하세요!

#### 2-7. 정리
- 싱글톤 : 객체를 하나만 두고, 어디서든 접근할 수 있게 하는 패턴
- 장점 : 접근이 쉽고, 객체가 하나뿐이라 혼란이 없음
- 단점 : 누가 쓰는지 추적하기 어렵고, 코드끼리 단단히 엮임
- 사용처 : 정말 하나만 필요한 객체 (오디오, 세이브, 게임 전체 상태 등)
- 주의점 : 남발하지 말 것, 초기화 순서와 종료 시점 주의
- 다음 장 : 이 단단한 엮임을 푸는 방법 → 의존성 주입

### 3. 의존성 주입 (Dependency Injection)
#### 3-1. 이런 문제 겪어본 적 있나요?
앞에서 만든 ScoreManager를 플레이어가 이렇게 쓰고 있다고 해봐요.

```csharp
public class Player : MonoBehaviour
{
    public void GetCoin()
    {
        ScoreManager.instance.AddScore(10);
    }
}
```

잘 돌아가요! 그런데 이런 일이 생겨요.

- 플레이어만 따로 테스트하려고 빈 씬에서 실행했더니, ScoreManager가 없다며 오류가 나요.
- 연습 모드에서는 점수를 쌓고 싶지 않은데, 그러려면 Player 코드를 고쳐야 해요.
- ScoreManager의 이름이나 사용법이 바뀌면, 이걸 부르는 모든 클래스를 찾아다니며 고쳐야 해요.

"점수를 올린다는 일은 똑같은데, 왜 Player가 ScoreManager를 이렇게 속속들이 알아야 하지?"
이건 Player가 ScoreManager.instance에 직접 매달려 있기 때문이에요!

#### 3-2. 개념 한 줄 요약
의존성 주입은 필요한 것을 스스로 찾아가지 않고, 밖에서 넣어 받는 패턴이에요!

다시 마을 우물 이야기예요!
지금까지는 마을 사람(Player)들이 우물(ScoreManager)까지 직접 걸어가서 물을 길어 왔어요.
그런데 우물이 다른 곳으로 옮겨지거나 수도관으로 바뀌면 어떻게 될까요? 사람들이 전부 새 길을 익혀야 해요.

대신 물을 집 앞까지 배달해 주면 어떨까요?
사람들은 수도꼭지만 틀면 돼요. 물이 우물에서 오든 수도관에서 오든 신경 쓸 필요가 없죠!
여기서 수도꼭지가 바로 코드에서의 '인터페이스'예요.
우물(싱글톤)은 그대로 마을에 하나만 있어요. 달라진 건 사람들이 우물을 찾아가는 방식뿐이에요!

#### 3-3. 구조
```
Player ──> IScoreService <── ScoreManager
                         <── PracticeScoreService
```
- IScoreService : "점수를 올려 준다"는 약속
- ScoreManager, PracticeScoreService : 약속을 지키는 쪽
- Player : 약속만 알고, 누가 점수를 관리하는지는 몰라요

#### 3-4. 예제 코드
```csharp
using UnityEngine;

// 점수를 올려 줄 수 있는 존재라면 누구나 이 약속(인터페이스)만 지키면 돼요.
public interface IScoreService
{
    void AddScore(int amount);
}

// 2장의 ScoreManager예요. 싱글톤은 그대로고, 약속만 하나 더 지켜요.
public class ScoreManager : MonoBehaviour, IScoreService
{
    public static ScoreManager instance { get; private set; }
    public int Score { get; private set; }

    private void Awake()
    {
        if (instance != null && instance != this)
        {
            Destroy(gameObject);
            return;
        }

        instance = this;
        DontDestroyOnLoad(gameObject);
    }

    public void AddScore(int amount)
    {
        Score += amount;
    }
}

// 연습 모드용이에요. 같은 약속을 지키지만 점수를 쌓지 않아요.
public class PracticeScoreService : MonoBehaviour, IScoreService
{
    public void AddScore(int amount)
    {
        Debug.Log($"연습 모드라 {amount}점은 기록하지 않아요.");
    }
}

// 플레이어는 누가 점수를 관리하는지 몰라요. IScoreService만 알아요.
public class Player : MonoBehaviour
{
    // 점수를 누가 관리할지는 인스펙터에서 밖에서 넣어 줘요. (주입)
    [SerializeField] private GameObject scoreTarget;

    private IScoreService scoreService;

    private void Start()
    {
        // scoreTarget에서 IScoreService를 꺼내요.
        if (!scoreTarget.TryGetComponent(out scoreService))
        {
            Debug.LogError($"{scoreTarget.name}에 IScoreService가 없어요!");
        }
    }

    public void GetCoin()
    {
        // 상대가 누구든 AddScore()만 부르면 돼요. (연결이 안 됐어도 게임이 멈추지 않게 ?. 를 썼어요)
        scoreService?.AddScore(10);
    }
}
```

알아두면 좋은 것은 세 가지예요.
1. `IScoreService` : Player와 점수 관리자 사이의 약속
2. `[SerializeField] scoreTarget` : 누가 점수를 관리할지 밖에서 넣어 주는 부분 (주입)
3. `TryGetComponent` : 넣어 준 오브젝트에서 약속을 지키는 컴포넌트를 꺼내는 부분

#### 3-5. 실행 결과
`scoreTarget`에 ScoreManager를 넣고 코인을 먹었을 때예요.

![[Pasted image 20261026200827.png]]

`scoreTarget`을 PracticeScoreService로 바꿔서 코인을 먹었을 때예요.

![[Pasted image 20261026200908.png]]

Player 코드는 한 줄도 안 바꿨는데 점수 처리가 바뀌었죠?

#### 3-6. 장단점과 주의점
우물 비유를 이어서 장단점을 살펴볼게요!

수도꼭지만 틀면 물이 나오니까 물이 어디서 오는지 신경 쓰지 않아도 되듯이, 의존성 주입의 가장 큰 장점은 교체가 쉽다는 거예요. 우물이 수도관으로 바뀌어도 사람들은 그대로 수도꼭지만 틀면 되는 것처럼, 점수 관리 방식이 바뀌어도 Player는 고칠 필요가 없어요! 또 진짜 우물이 없어도 임시 물탱크로 연습해 볼 수 있듯이, 가짜 점수 관리자를 끼워서 Player만 따로 테스트하기도 쉬워져요.

하지만 단점도 있어요. 수도꼭지를 설치하려면 배관 공사가 필요한 것처럼, 인터페이스와 클래스가 늘어나서 코드가 처음엔 복잡해 보여요. 작은 프로젝트에서는 오히려 과한 설계일 수 있고요. 또 수도관을 연결하는 걸 깜빡하면 물이 안 나오듯이, 인스펙터에 scoreTarget을 넣는 걸 빼먹거나 IScoreService가 없는 오브젝트를 넣으면 실행해 봐야 오류를 알 수 있어요.

그래서 모든 곳에 수도관을 깔 필요는 없고, 앞으로 바뀔 가능성이 있거나 여러 대상이 같은 약속을 지키는 곳에 쓰는 게 좋아요!

참고로 "상속으로도 되지 않나요?" 하는 분도 있을 거예요. 맞아요, 단순한 구조라면 부모 클래스 하나로도 풀려요. 다만 C#은 부모를 하나만 가질 수 있고, 상속은 "~는 ~이다" 관계인 것끼리만 묶이는 반면, 인터페이스는 서로 관련 없는 클래스도 "~할 수 있다"는 약속만 지키면 묶을 수 있어요. 그래서 이런 경우엔 인터페이스가 더 유연해요.

#### 3-7. 정리
- 의존성 주입 : 필요한 것을 스스로 찾지 않고, 밖에서 넣어 받는 패턴
- 핵심 : 구체적인 클래스가 아닌 인터페이스(약속)에만 의존함
- 장점 : 교체가 쉽고, 코드 수정이 줄고, 테스트가 쉬움
- 단점 : 인터페이스와 클래스가 늘어 처음엔 복잡함, 연결 실수는 실행해 봐야 알 수 있음
- 사용처 : 바뀔 가능성이 있거나, 여러 대상이 같은 동작을 하는 곳
- 싱글톤과의 관계 : 싱글톤을 없애는 게 아니라, 싱글톤에 직접 매달리지 않게 하는 것
- 다음 장 : 이 "약속"을 이용해 동작 자체를 갈아 끼우는 방법 → 전략 패턴


### 4. 전략 패턴 (Strategy)
#### 4-1. 이런 문제 겪어본 적 있나요?
앞에서 만든 ScoreManager에 새 요구사항이 생겼다고 해봐요!
"기본 모드에서는 점수를 그대로, 하드 모드에서는 절반만 주세요!"

그래서 이렇게 고쳤어요.

```csharp
public void AddScore(int amount)
{
    if (mode == Mode.Basic)
        Score += amount;
    else if (mode == Mode.Hard)
        Score += amount / 2;
}
```

잘 돌아가요! 그런데 곧 "콤보 모드는 2배로 주세요!", "이벤트 모드는요?" 같은 요청이 계속 들어와요.
else if가 끝없이 붙고, 계산 방법 하나를 고칠 때마다 ScoreManager를 열어서 건드려야 해요.
다른 기능까지 망가뜨릴까 봐 불안하기도 하고요.

"점수를 올린다는 일은 똑같은데, 계산 방법만 바뀌는데 왜 매번 ScoreManager를 고쳐야 하지?"
이건 ScoreManager가 계산 방법을 전부 직접 알고 있기 때문이에요!

#### 4-2. 개념 한 줄 요약
전략 패턴은 하는 일은 같고 방법만 다른 동작들을 따로따로 만들어 두고, 필요할 때 갈아 끼우는 패턴이에요!

다시 마을 우물 이야기예요!
같은 우물에서 물을 긷는 일이라도 양동이, 두레박, 펌프처럼 쓸 수 있는 도구가 여러 가지예요.
마을 사람은 "물을 긷는다"는 일은 그대로 하고, 상황에 맞는 도구만 바꿔 들고 가면 돼요.
도구를 바꾼다고 우물을 새로 지을 필요는 없죠!

여기서 우물이 ScoreManager, 도구가 '전략'이에요.
3장에서 배운 수도꼭지(인터페이스)처럼 "물을 긷는 도구"라는 약속만 지키면, 어떤 도구든 끼울 수 있어요.

#### 4-3. 구조
```
ScoreManager ──> IScoreStrategy <── BasicScoreStrategy
                                <── HardScoreStrategy
```
- IScoreStrategy : "점수를 계산한다"는 약속
- BasicScoreStrategy, HardScoreStrategy : 계산 방법 하나씩
- ScoreManager : 약속만 알고, 어떤 방법인지는 몰라요 (필요할 때 SetStrategy로 교체)

#### 4-4. 예제 코드
```csharp
using UnityEngine;

// 점수를 계산하는 방법의 약속이에요.
public interface IScoreStrategy
{
    int Calculate(int amount);
}

// 기본 : 받은 점수를 그대로 줘요.
public class BasicScoreStrategy : IScoreStrategy
{
    public int Calculate(int amount) => amount;
}

// 하드 : 점수를 절반만 줘요.
public class HardScoreStrategy : IScoreStrategy
{
    public int Calculate(int amount) => amount / 2;
}

// 2장의 ScoreManager예요. 계산 방법을 갈아 끼울 수 있게 바뀌었어요.
public class ScoreManager : MonoBehaviour
{
    public static ScoreManager instance { get; private set; }
    public int Score { get; private set; }

    // 지금 쓰는 점수 계산 방법이에요. 처음에는 기본(Basic)!
    private IScoreStrategy strategy = new BasicScoreStrategy();

    // Awake()는 2장과 같아요.

    // 계산 방법을 밖에서 갈아 끼워요.
    public void SetStrategy(IScoreStrategy newStrategy)
    {
        strategy = newStrategy;
    }

    public void AddScore(int amount)
    {
        // 어떤 방법인지 몰라도 Calculate()만 부르면 돼요.
        Score += strategy.Calculate(amount);
    }
}
```

사용하는 쪽에서는 이렇게 갈아 끼우면 돼요.

```csharp
ScoreManager.instance.SetStrategy(new HardScoreStrategy());
```

알아두면 좋은 것은 세 가지예요.
1. `IScoreStrategy` : 점수 계산 방법의 약속
2. `SetStrategy()` : 계산 방법을 밖에서 갈아 끼우는 부분
3. `strategy.Calculate()` : 어떤 방법인지 몰라도 그냥 부르면 되는 부분

#### 4-5. 실행 결과
Basic 전략일 때 Get Coin을 눌렀어요.

![[Pasted image 20261026203017.png]]

Hard 전략으로 바꾸고 Get Coin을 눌렀어요.

![[Pasted image 20261026203056.png]]

ScoreManager의 AddScore() 코드는 한 줄도 안 바꿨는데 점수 계산 방법이 바뀌었죠?

#### 4-6. 장단점과 주의점
우물 비유를 이어서 장단점을 살펴볼게요!

새로운 도구가 필요하면 도구만 하나 새로 만들어서 갖다 쓰면 되듯이, 전략 패턴의 가장 큰 장점은 추가가 쉽다는 거예요. 콤보 모드가 필요하면 `ComboScoreStrategy` 클래스 하나만 만들면 되고, ScoreManager는 건드릴 필요가 없어요! 끝없이 길어지던 else if도 사라져서 코드가 읽기 쉬워지고요. 또 게임을 실행하는 도중에도 도구를 바꿔 들 수 있듯이, 실행 중에 전략을 교체할 수도 있어요.

하지만 단점도 있어요. 도구마다 창고에 보관할 자리가 필요한 것처럼, 전략마다 클래스가 하나씩 생겨서 파일이 늘어나요. 방법이 두세 가지로 끝나고 앞으로도 안 바뀐다면 오히려 else if가 더 간단할 수 있고요. 또 어떤 도구를 들고 갈지 정하는 사람은 어딘가에 따로 있어야 해요. 위 예제에서는 버튼이 그 역할을 했어요.

참고로 3장 의존성 주입과 비슷해 보일 수 있어요. 의존성 주입은 필요한 것을 밖에서 건네주는 연결 방식에 가깝고, 전략 패턴은 같은 일을 하는 방법을 갈아 끼우는 목적에 가까워요. 그래서 둘은 함께 쓰이는 경우가 많아요!

#### 4-7. 정리
- 전략 패턴 : 하는 일은 같고 방법만 다른 동작을 따로 만들어 두고, 필요할 때 갈아 끼우는 패턴
- 핵심 : 동작을 인터페이스(약속) 뒤로 빼서 교체 가능하게 함
- 장점 : 새 방법 추가가 쉽고, if-else가 사라지고, 실행 중에도 교체 가능
- 단점 : 전략마다 클래스가 늘어남, 단순한 경우엔 과한 설계일 수 있음
- 사용처 : 같은 일을 하는 방법이 여러 가지이고, 앞으로 더 늘어날 가능성이 있는 곳
- 의존성 주입과의 관계 : 의존성 주입은 건네주는 방식, 전략 패턴은 방법을 갈아 끼우는 목적
- 다음 장 : 세 패턴을 한눈에 비교해 보기



### 5. 세 패턴 한눈에 비교
| 패턴     | 해결하는 문제 | 장점  | 단점  | 내가 쓴 곳 |
| ------ | ------- | --- | --- | ------ |
| 싱글톤    | 하나만 있어야 하는 객체가 여러 개 생기고, 어디서든 접근이 필요함 | 접근이 쉽고, 객체가 하나뿐이라 혼란이 없음 | 누가 쓰는지 추적하기 어렵고, 코드끼리 단단히 엮임 | GameManager |
| 의존성 주입 | 구체적인 클래스에 직접 매달려서 교체와 테스트가 어려움 | 교체가 쉽고, 코드 수정이 줄고, 테스트가 쉬움 | 인터페이스와 클래스가 늘어 처음엔 복잡함 | 유닛/캐릭터 동작 |
| 전략 패턴  | 같은 일을 하는 방법이 늘어날 때마다 if-else가 길어짐 | 새 방법 추가가 쉽고, 실행 중에도 교체 가능 | 전략마다 클래스가 늘어남 | 공격/무기 방식 |


### 6. 마무리
#### 배운 점
평소에 자주 쓰던 패턴들이라 다 안다고 생각했어요.
그런데 처음 보는 사람에게 설명하려고 글로 쓰다 보니, "왜 쓰는지"를 제대로 말로 풀지 못하는 부분이 많았어요.

- **비유를 찾으며 더 이해했어요.** 싱글톤은 공동 우물, 의존성 주입은 수도꼭지, 전략 패턴은 물 긷는 도구로 풀어 보니 각 패턴이 해결하는 문제가 또렷해졌어요.
- **세 패턴은 따로 노는 게 아니었어요.** 싱글톤의 편리함이 엮임을 만들고, 그 엮임을 의존성 주입으로 풀고, 풀린 구조 위에서 전략 패턴으로 동작을 갈아 끼우는 하나의 흐름이었어요.
- **패턴은 정답이 아니라 양식이에요.** 논문 양식이 내용을 대신 써주지 않듯이, 패턴도 코드를 대신 짜주지 않아요. 문제 상황에 맞는 양식을 고르는 게 중요하고, 필요 없는 곳에 쓰면 오히려 복잡해진다는 것도 알게 됐어요.

이 글처럼 앞으로도 쓰던 패턴을 누군가에게 설명한다고 생각하고 정리해 보려고 해요!


#### 참고 자료
- Unity Design Patterns : https://www.unitydesignpatterns.com
- Refactoring.Guru : https://refactoring.guru/ko/design-patterns
- 나무위키 : https://namu.wiki/w/소프트웨어%20디자인%20패턴
- 위키피디아 : https://en.wikipedia.org/wiki/Design_Patterns