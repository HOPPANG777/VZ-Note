# ComPtr

<p align="center">
  <img src="../../Images/Language/CPP/ComPtr.png" alt="ComPtr" width="720" />
</p>

> ComPtr은 스마트 포인터로, COM 객체의 메모리 관리를 자동으로 처리해 주는 기능이다.
>
> DirectX 같은 COM 기반 API에서는 참조 횟수를 관리해야 하는데, 수동으로 하면 누수나 해제 오류가 난다.
>
> ComPtr을 쓰면 AddRef/Release를 자동으로 맞춰 준다.

COM 자체는 Windows/COM.md에 있다.

---

> [!NOTE]
> **보충**
>
> - **출처:** Microsoft Learn — `Microsoft::WRL::ComPtr` 및 ATL `CComPtr`
> COM 객체의 수명은 `IUnknown::AddRef` / `IUnknown::Release`다.
> ComPtr은 소멸 때 Release를 호출하는 RAII 래퍼다.
> 표준 unique_ptr이랑 비슷하게 보이지만, 삭제기가 delete가 아니라 Release다.
