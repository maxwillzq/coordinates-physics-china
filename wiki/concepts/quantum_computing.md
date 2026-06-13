# 量子计算优越性与多技术路线 (Quantum Computational Advantage)

## 核心物理概念
**量子计算优越性（Quantum Computational Advantage，即“量子霸权”）** 指的是量子计算原型机在特定物理数学问题上的计算速度，以无可争议的优势超越世界上最强大的经典超级计算机。目前主要通过两大物理技术路线实现：

### 1. 超导量子计算技术路线（Google Sycamore vs. 祖冲之号）
超导量子计算利用超导约瑟夫森结（Josephson junctions）作为人工二能级原子，构建超导量子比特。
- **随机线路取样（Random Circuit Sampling, RCS）**：在其希尔伯特空间（Hilbert space）内进行极深层次的量子纠缠演化，最后读取各量子比特的二进制输出分布。
- **Google Sycamore**（2019年）：利用 53 个可控超导比特，率先宣称实现了量子霸权。
- **“祖冲之二号”**（2021年）：潘建伟团队研制出 66 比特（56 比特参与取样）的可编程超导量子计算原型机，其在高复杂度随机线路取样问题上的速度比 Sycamore 进一步提升，计算复杂度随比特数呈指数增长，确立了超导路线的绝对优势。

### 2. 光量子计算技术路线与高斯玻色取样（九章系列）
由于光子之间不直接发生相互作用，且具有极高的相干时间，光量子计算采用不同的取样机制：
- **高斯玻色取样（Gaussian Boson Sampling, GBS）**：在输入端注入单模压缩真空态（Squeezed States），经过包含多个分束器和相位调制器的巨型多模干涉干涉索网（线性光学网络）进行散射，最后在输出端利用超导纳米线单光子探测器（SNSPD）读取多光子符合计数。
- **“九章”**（2020年）：潘建伟、陆朝阳团队研制出 76 个光子 100 模式的高斯玻色取样机，在不需要极低温冷却比特的条件下实现了光量子优越性。
- **“九章三号”**（2023年）：探测到的光子事例数达到 255 个，相比最强超算，取样速度领先了百万亿倍，使中国成为唯一在光量子路线实现此优越性的国家。

## 物理范式的转变
量子优越性的物理实现证明了量子力学的叠加态与纠缠态具有真实的、可转化为计算力的物理资源属性。它打破了传统计算科学的强丘奇-图灵论题（Extended Church-Turing Thesis），表明量子系统能有效模拟经典计算机无法多项式时间模拟的物理过程。当前物理学界正全力从“喧嚣时代（NISQ, 中等规模有噪声量子时代）”迈向具有纠错能力的通用量子计算阶段。

## 参考文献
1. Arute, F., et al. (Google AI Quantum). (2019). "Quantum supremacy using a programmable superconducting processor". *Nature*, 574(7779), 505-510.
2. Zhong, H. S., et al. (including C. Y. Lu & J. W. Pan). (2020). "Quantum computational advantage using photons". *Science*, 370(6523), 1460-1463.
3. Wu, Y., et al. (2021). "Strong Quantum Computational Advantage using a Programmable Superconducting Processor". *Physical Review Letters*, 127(18), 180503.

---
*记录时间：2026-06-13*
