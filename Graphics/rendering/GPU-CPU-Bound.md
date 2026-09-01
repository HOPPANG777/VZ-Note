# GPU 바운드 / CPU 바운드

<p align="center">
  <img src="../../Images/Graphics/rendering/GPU-CPU-Bound.png" alt="GPU-CPU-Bound" width="720" />
</p>

> GPU 바운드는 GPU가, CPU 바운드는 CPU가 병목인 상황이고, 펜스나 더블·트리플 버퍼링으로 CPU와 GPU를 동기화해 병렬성을 유지한다.

드로우콜이 많으면 CPU 바운드가 되기 쉽다. 픽셀 셰이더가 무거우면 GPU 바운드.

---

> [!WARNING]
> **더 보충이 필요한 부분**
>
> 펜스/쿼리로 어떻게 대기하는지는 정리에 없다.
> D3D12 ID3D12Fence, D3D11 쿼리가 공식 API다. 동기화 구현을 물어보면 그 문서를 보고 적어야 한다.
