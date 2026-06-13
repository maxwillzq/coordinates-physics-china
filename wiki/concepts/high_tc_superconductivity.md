# 高温超导与麦克米兰极限 (High Tc Superconductivity & McMillan Limit)

## 核心物理概念

### 1. 传统 BCS 超导与麦克米兰极限
1957年提出的巴丁-库珀-施里弗（BCS）理论成功解释了常规金属和合金的超导电性。该理论指出，带负电的电子通过晶格畸变（交换声子）产生吸引力，克服库仑排斥力，两两配对成**库珀对（Cooper pair）**，并在超导临界温度 $T_c$ 以下发生相干凝聚。

1968年，麦克米兰（William L. McMillan）基于强耦合超导理论，推导出了超导临界温度 $T_c$ 的半经验公式（**麦克米兰公式**）：

$$ T_c = \frac{\theta_D}{1.45} \exp \left[ -\frac{1.04(1 + \lambda)}{\lambda - \mu^*(1 + 0.62\lambda)} \right] $$

其中：
- $\theta_D$ 为声子德拜温度（代表晶格振动的特征能量尺度）。
- $\lambda$ 为无量纲的电子-声子耦合常数。
- $\mu^*$ 为库仑赝势（代表电子间的库仑排斥作用）。

根据经典理论，对于常规金属和合金，电子-声子相互作用强度 $\lambda$ 很难超过 2。如果强行增大耦合，会导致晶格不稳定性，进而发生晶格相变。在 $\lambda \le 2$ 这一物理约束下，将常规参数带入公式，科学家预测常规声子介导的超导电性存在一个上限，即**麦克米兰极限（McMillan Limit）**：

$$ T_c^{\text{max}} \approx 30\text{ K} - 40\text{ K} $$

这一极限导致物理学界在数十年内普遍认为无法实现液氮温区（ $77\text{ K}$ 以上）的超导电性。

### 2. 铜氧化物高温超导的发现与突破
1986年，瑞士 IBM 苏黎世研究实验室的 Bednorz 与 Müller 发现钡镧铜氧（ $\text{Ba-La-Cu-O}$ ）体系存在 $35\text{ K}$ 的超导迹象，拉开了高温超导革命的序幕。这一工作突破了传统金属超导的藩篱，但仍未击穿麦克米兰极限。

1987年初，全球多个研究小组展开了激烈的竞赛。中国中科院物理所赵忠贤团队与美国休斯敦大学朱经武团队独立发现了临界转变温度达到 $93\text{ K}$ 的钇钡铜氧（YBCO， $\text{Y-Ba-Cu-O}$ ）体系超导体。

钇钡铜氧超导转变温度高达 $93\text{ K}$ ，彻底击穿了常规声子介导的麦克米兰极限。这也意味着铜氧化物超导体的配对机制必须引入全新的物理图像：
- **强关联电子系统（Strongly Correlated Electron Systems）**：铜氧化物的基态是非超导态时的莫特绝缘体（Mott Insulator），强烈的电子库仑排斥主导了物态行为。
- **非常规配对对称性**：其超导库珀对的波函数表现出 $d$ 波配对对称性，而非传统超导的 $s$ 波对称性。
- **共振价键理论（RVB）**：安德森（P. W. Anderson）等人提出，其超导电性可能来源于无序自旋单态（Resonating Valence Bond）在掺杂后的电荷流动。

## 中西独立竞争的科学社会学
1986-1987年的超导热潮是现代科学史上典型的“多重独立发现”（multiple independent discovery）。在信息传递尚不发达的时代，北京的赵忠贤团队在液氮供应紧张、烧结炉等实验设备极为简陋的情况下，凭借敏锐的物理直觉，选择钇（Y）作为非磁性稀土元素替代镧，成功合成出了转变温度达 $93\text{ K}$ 的单相超导样品。这表明在基础材料物理探索中，实验洞察力与物理直觉可以在一定程度上弥补物质装备的不足。

## 参考文献
1. Bednorz, J. G., & Müller, K. A. (1986). "Possible $T_c$ Superconductivity in the Ba-La-Cu-O System". *Zeitschrift für Physik B Condensed Matter*, 64(2), 189-193.
2. Wu, M. K., Ashburn, J. R., Torng, C. J., Hor, P. H., Meng, R. L., Gao, L., Huang, Z. J., Wang, Y. Q., & Chu, C. W. (1987). "Superconductivity at 93 K in a New Mixed-Phase Y-Ba-Cu-O Compound System at Ambient Pressure". *Physical Review Letters*, 58(9), 908-910.
3. Zhao, Z. X., Chen, L. Q., Yang, Q. S., Huang, Y. Z., Chen, G. H., Tang, R. M., Liu, G. R., Cui, C. G., Chen, L., Wang, L. Z., Guo, S. Q., Li, S. L., & Bi, J. Q. (1987). "Superconductivity Above Liquid Nitrogen Temperature in Ba-Y-Cu-O System". *Kexue Tongbao (Foreign Language Edition)*, 32(8), 522-524.
4. 赵忠贤 (2016). 《神州寻梦记：超导的故事》. 北京: 科学出版社.

---
*记录时间：2026-06-13*
