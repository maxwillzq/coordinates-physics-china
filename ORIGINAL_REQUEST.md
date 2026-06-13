# Original User Request

## Initial Request — 2026-05-25T09:37:37-07:00

# Teamwork 项目提示词

创作一部学术型通俗历史著作《坐标：世界物理版图中的中国》，以世界物理学范式转移为主线，审视中国在不同历史时期的坐标定位、角色演变与科学融入。采用统一的“三维分析法”（世界轴、中国点、坐标值）。

工作目录：/Users/johnqiangzhang/Documents/projects/coordinates-physics-china

## 需求

### R1. 内容撰写
按照策划案大纲撰写全书六编的初稿，每编必须严格遵循“世界轴-中国点-坐标值”的三维框架。文字风格应兼具学术厚度与可读性。
- 第一编：平行的时空与错失的范式（17世纪前）
- 第二编：经典物理的巅峰与“西学东渐”的冲击（18—19世纪）
- 第三编：量子革命与肉身接轨的拓荒者（1900—1949）
- 第四编：冷战地缘下的国防物理与体制内聚（1949—1978）
- 第五编：全球化浪潮中的全面跟跑与大装置布局（1978—2010）
- 第六编：大科学与AI范式时代的新坐标（2010年至今）

### R2. 数据与史料准确性验证
实施策划案中指定的验证机制：
- **物理公式与量纲检查**：验证等式两端的物理量纲是否绝对对齐。
- **史料的三方交叉验证**：重大历史断言必须满足“当事人回忆 ∩ 同期官方原始档案 ∩ 国际独立第三方学术评价”。

### R3. 代码库与工具链搭建
按照推荐的目录结构初始化 GitHub 代码库：
- `drafts/`：存放手稿
- `sources/`：存放参考文献和档案链接
- `verification/`：存放验证脚本
- `assets/`：存放图表 and 图片
提供标准的 LaTeX/Markdown 模板和 `.gitignore` 文件。

### R4. 在线书籍显示网站
构建一个基于 Next.js 的网站来在线显示书籍内容，参考 `../alphajax/docs/website` 的结构和技术栈。
- **数学公式显示**：确保 Markdown 中的 LaTeX 数学公式能够完整、正确地渲染（例如使用 KaTeX 或 MathJax）。
- **设计美学**：遵循“Web 应用开发”指南，使用现代排版、渐变和微交互，营造高端的视觉体验。

### R5. 视觉图表与插图
全书插图采用极简现代风，重点突出物理原理和数据贡献。
- **图表实现**：优先使用代码生成（如 Mermaid、SVG 或前端图表库）以保证清晰度和可维护性。
- **示意图**：使用线框图、粒子轨迹示意图等，而非复杂照片。

## 验收标准

### 代码库搭建
- [ ] 目录结构与策划案推荐完全一致。
- [ ] `.gitignore` 文件包含指定的 LaTeX 构建临时文件。

### 内容质量
- [ ] 策划案中所有六编的初稿均已保存在 `drafts/` 目录中。
- [ ] 每章节均包含“世界轴”、“中国点”和“坐标值”三维分析。

### 数据验证
- [ ] `verification/` 目录中包含用于量纲检查的脚本或详细文档。
- [ ] 提供一份包含至少 3 项重大历史断言的“三方交叉验证”报告或记录。

### 网站功能
- [ ] 网站能够成功运行并展示书籍内容。
- [ ] Markdown 中的数学公式在网页上正常渲染，无代码残留。
- [ ] 网站风格现代，符合“精美设计”的要求。

### 视觉与插图
- [ ] 至少包含策划案中提到的“吴有训实验光谱强度分布图”的电子化版本（代码生成或 SVG）。
- [ ] 网站中包含相应的图表展示。

## 团队角色分配 (AI 侧)
为了高质量完成本项目，本项目将委派给 `teamwork` 系统，主要由以下专业背景的 AI 角色组成（您将作为总策划/主编进行最终审查）：
- **物理史撰稿人**：负责检索公开史料，按三维框架撰写各章节初稿。
- **科学数据验证员**：负责公式量纲检查和史料三方验证的脚本编写与执行。
- **视觉与全栈工程师**：负责搭建 Next.js 网站，配置公式渲染，实现精美 UI，并负责图表 and 插图的代码化生成。

## Follow-up — 2026-05-25T10:43:53-07:00

# Teamwork 项目提示词 (扩写阶段)

将《坐标：世界物理版图中的中国》现有的 6 编大纲式初稿，通过多智能体并行工作的模式，深度扩写为内容详实、具备学术厚度的完整章节。

工作目录：/Users/johnqiangzhang/Documents/projects/coordinates-physics-china

## 需求

### R1. 内容深度扩写
将 `drafts/` 目录下的 6 编初稿（part1.md 到 part6.md）进行大幅度扩写，填补占位符，增加具体的历史细节、科学原理阐述 and 人物故事。每编目标字数建议在 3000-5000 字。

### R2. 多智能体并行工作
`teamwork` 系统应指派多个撰稿/研究智能体，同时对不同的编（例如 Volume 1, 2, 3）进行并行扩写，以提高效率。

### R3. 保持三维框架与风格
扩写后的内容必须继续严格遵循“世界轴-中国点-坐标值”的三维框架，保持学术严谨性与通俗可读性的平衡。

## 验收标准

### 内容完整性
- [ ] 所有 6 编的占位符均已删除，替换为具体叙述。
- [ ] 每编字数达到 3000 字以上。

### 网站更新
- [ ] 扩写后的内容成功同步到 Next.js 网站上，且格式正确，公式渲染正常。

## Follow-up — 2026-05-25T11:08:53-07:00

# Teamwork 项目提示词 (网站重构阶段)

使用 **Docusaurus** 框架重构《坐标：世界物理版图中的中国》的展示网站，使其在美学、布局 and 交互上参考并达到 `https://www.hello-algo.com/` 的高水准。

工作目录：/Users/johnqiangzhang/Documents/projects/coordinates-physics-china

## 需求

### R1. 基于 Docusaurus 的框架搭建
- **技术选型**：使用 Docusaurus 初始化新的网站项目（可以替换原有的 `website` 目录或新建目录）。
- **开箱即用功能**：配置左侧树状章节导航、顶部搜索、亮暗色模式切换。

### R2. UI/UX 视觉重构 (参考 Hello Algo)
- **视觉风格**：采用极简、现代且极具质感的视觉设计，使用高级灰 and 柔和的色彩。
- **排版优化**：使用适合长文阅读的现代字体，优化行高 and 字间距，确保极佳的阅读体验。
- **内容区域**：居中显示，宽度适中，两侧留白，减少视觉疲劳。

### R3. 功能性与内容迁移
- **数学公式**：配置 Docusaurus 的数学公式插件（KaTeX 或 MathJax），确保 Markdown 中的 LaTeX 公式高质量渲染。
- **内容迁移**：将 `drafts/` 目录下的 6 编完整手稿迁移至 Docusaurus 的文档目录中。
- **图表集成**：将 SVG 图表无缝嵌入正文。

## 验收标准

### 基础搭建
- [ ] 新网站基于 Docusaurus 构建，能够成功运行。
- [ ] 具备左侧章节侧边栏 and 亮暗色切换功能。

### 视觉与体验
- [ ] 网站整体视觉风格与 Hello Algo 类似，呈现高端质感。
- [ ] 左侧包含可折叠/展开的章节目录侧边栏。
- [ ] 所有 6 编内容完整展示，数学公式渲染完美，无代码残留。

## Follow-up — 2026-05-25T12:24:41-07:00

# Teamwork 项目提示词 (内容修订阶段)

修订并扩写《坐标：世界物理版图中的中国》的内容，将海外华人、台湾地区以及大陆核心物理学家的贡献纳入其中，增加学术索引与章节名言，并设计中国传统风格的插图。

工作目录：/Users/johnqiangzhang/Documents/projects/coordinates-physics-china

## 需求

### R1. 纳入海外华人、台湾与大陆核心贡献
重点在第三编、第五编和第六编中，补充以下内容：
- **海外华人顶尖贡献**：详细阐述杨振宁、李政道（宇称不守恒）、吴健雄（实验验证）、丁肇中（J粒子）、崔琦（分数量子霍尔效应）、高锟（光纤）等人的里程碑式成就，并在正文中引用其代表性论文。
- **台湾地区物理贡献**：补充台湾在物理学界的研究成果、代表人物以及重要科研设施（如同步辐射研究中心）的贡献。
- **大陆核心贡献锚点**：确保重点突出叶企孙、吴有训、赵忠尧、钱学森、邓稼先、于敏、黄昆、赵忠贤、潘建伟、薛其坤、王贻芳等人的贡献。

### R2. 正文内嵌学术索引与名言导读
- **学术索引**：在阐述上述科学家贡献时，必须在正文中直接提及他们发表的**优秀论文或著作名称**，并结合物理学背景进行解读。
- **章节名言（Epigraph）**：为每一章开头添加一句**画龙点睛的名人名言**（不限国籍，如爱因斯坦、玻尔等），该名言必须与本章的物理学范式或历史背景有强关联，以更好地呼应“世界物理版图”的主题。

### R3. 中国传统风格插图
为每一章设计并生成具有**中国传统美学风格**（如水墨山水、写意、书法风格）的插图。
- **意境融合**：将古典艺术意境与现代物理概念（如微观粒子、时空弯曲、量子纠缠）进行跨界融合。
- 使用 AI 绘图工具（如 midjourney 风格提示或 DALL-E）生成高质量的章节导读图。

### R4. 保持三维框架
所有新增内容仍需有机地融入“世界轴-中国点-坐标值”的框架中。

## 验收标准

### 内容与索引
- [ ] 正文中成功补充了指定科学家的贡献及经典论文/著作引用。
- [ ] 每一章开头都包含一句与内容强关联的名人名言。

### 视觉与插图
- [ ] 每一章都包含一幅中国风意境的 AI 生成插图。
- [ ] 网站排版优美，图文与名言配合得当。

## Follow-up — 2026-05-25T15:38:24-07:00

# Teamwork 项目提示词 (深度打磨阶段)

从文本质量、数据支撑、科学哲学深度、全球物理学家关联以及科学教育价值五个维度，深度打磨和提升《坐标：世界物理版图中的中国》全书内容。

工作目录：/Users/johnqiangzhang/Documents/projects/coordinates-physics-china

## 需求

### R1. 科学哲学深度与教育启示
- **哲学深度**：结合“李约瑟难题”与库恩的“范式转移”理论，深度剖析中国在不同历史时期与西方物理学范式的错失、碰撞与融入。
- **教育启示**：在每编末尾增加一个独立小节“【科学思维与教育启示】”，总结该时期的科学方法论对现代科学教育的借鉴意义。

### R2. 全球物理学家的思想与互动关联
- **隔空对话**：在正文中增加中西方物理学家的思想对比（如墨子与亚里士多德，李善兰与麦克斯韦）。
- **真实互动**：深挖并详述中国物理学家与西方大师的真实互动细节（如吴有训与康普顿，杨振宁、李政道与奥本海默等），体现全球科学共同体的流动。

### R3. 坚实的数据与史料支撑
- **数据细化**：在描述重大发现时，尽量给出具体的实验数据、时间节点或历史关键数据。
- **权威文献**：确保引用的论文 and 著作名称准确，并在正文中以学术规范的方式提及。

### R4. 文本质量与叙事升级
- **文风打磨**：将目前的叙述进一步润色，使其兼具史书的厚重感与科普读物的流畅性，避免平铺直叙。

## 验收标准

### 内容深度
- [ ] 每编末尾都包含“【科学思维与教育启示】”小节。
- [ ] 正文中至少有 3 处深度的中西科学哲学对比分析。

### 数据与关联
- [ ] 增加了至少 5 处关于中外科学家具体互动或思想对比的细节描写。
- [ ] 补充了具体的实验数据或更详实的史料数据。

## Follow-up — 2026-05-25T22:42:16Z

User has manually edited website/docs/part4.md with deep improvements (Needham, Kuhn, Oppenheimer comparison, data, and education section). Please instruct the worker for Part 4 to not overwrite these changes, or use them as the new baseline.

## Follow-up — 2026-06-13T09:13:54-07:00

Refine and restructure Part 2 of the *Coordinates* book (both Chinese and English editions) following the project's style guide. This involves researching and documenting historical translations, updating the wiki, rewriting the Docusaurus files, and verifying page builds.

Working directory: /Users/johnqiangzhang/Documents/projects/coordinates-physics-china
Integrity mode: development

## Requirements

### R1. Wiki Database Ingestion (Wiki-First)
Prior to editing site articles, research and create Wiki pages under `/wiki/entities/` and `/wiki/concepts/` for relevant historical figures and physics paradigms introduced in Part 2. Update `/wiki/index.md` and log the actions in `/wiki/log.md`.

### R2. Restructure website/docs/part2.md (Chinese Edition)
Rewrite `website/docs/part2.md` following the symmetrical close-combat structure (discipline-specific sections comparing West vs. China) and text guidelines defined in `/wiki/drafts/style_template.md`. Deconstruct translations of Li Shanlan and Xu Shou using modern physical terms and introduce LaTeX-formatted alert boxes.

### R3. Synchronize and Refine English Translation
Fully translate the updated Part 2 Chinese content to `/website/i18n/en/.../part2.md`, keeping paragraph flow, LaTeX equations, alert boxes, and image references completely synchronized.

### R4. Compilation and Build Verification
Ensure the Docusaurus site compiles cleanly without broken links, broken markdown image paths, or KaTeX rendering syntax errors.

## Acceptance Criteria

### Wiki Quality
- [ ] New entity files (`li_shanlan.md`, `xu_shou.md`, `john_fryer.md`, `alexander_wylie.md`) exist under `/wiki/entities/`.
- [ ] New concept files (`chong_xue.md`, `ge_zhi_evolution.md`, `analytical_mechanics.md`, `maxwell_equations.md`, `carnot_cycle.md`) exist under `/wiki/concepts/`.
- [ ] All new files are linked in `/wiki/index.md` and operations are logged in `/wiki/log.md`.

### Document Structure & Style (Chinese & English)
- [ ] Both `part2.md` files (Chinese and English) use `pathname:///img/part2_illustration.png` as their header illustration.
- [ ] Chapter 1 has three symmetrical comparative sections matching analytical mechanics, thermodynamics, and electromagnetism.
- [ ] Chapter 2 has three comparative sections matching translation languages, translation mechanisms, and paradigm lag/parallax.
- [ ] High-temperature/low-temperature thermal engines and translation vocabularies are mapped into math-infused `[!IMPORTANT]` and `[!NOTE]` alert boxes with LaTeX formulas.
- [ ] All inline LaTeX formulas are padded with outer spaces (e.g. ` $...$ `) to ensure rendering.

### Build Verification
- [ ] Running `npm run build` inside `website/` finishes with success and outputs localized static HTML pages.

## Follow-up — 2026-06-13T10:32:41-07:00

Refine and restructure the remaining chapters (Parts 3, 4, 5, and 6, both Chinese and English editions) of the *Coordinates* book following the project's style guide. This involves researching historical contexts, updating the wiki database, rewriting the Docusaurus files under symmetrical comparisons, and validating page builds while strictly avoiding literature hallucinations.

Working directory: /Users/johnqiangzhang/Documents/projects/coordinates-physics-china
Integrity mode: development

## Requirements

### R1. Wiki Database Ingestion (Wiki-First)
For each chapter (Parts 3, 4, 5, and 6), research and create/update Wiki pages under `/wiki/entities/` and `/wiki/concepts/` for relevant historical figures and physics paradigms. Update `/wiki/index.md` and log the actions in `/wiki/log.md`.

### R2. Restructure and Rewrite Chinese Chapters (Part 3, 4, 5, 6)
Rewrite `website/docs/part3.md`, `part4.md`, `part5.md`, and `part6.md` following the symmetrical close-combat structure (comparing West vs. China) and text guidelines defined in `/wiki/drafts/style_template.md`. Deconstruct translations and historical physics paradigms using modern physical terms and introduce LaTeX-formatted math alert boxes.

### R3. Synchronize and Refine English Translations
Fully translate and synchronize all rewritten content to the corresponding English editions (`website/i18n/en/.../part3.md`, `part4.md`, `part5.md`, `part6.md`), keeping paragraph flow, LaTeX equations, alert boxes, and image references completely aligned.

### R4. Compilation and Build Verification
Ensure the Docusaurus site compiles cleanly without broken links, broken markdown image paths, or KaTeX rendering syntax errors.

### R5. Strict Reference Verification (Anti-Hallucination)
Every citation added to the "References/参考文献" section of any chapter must undergo strict verification. Only fully real, verifiable academic papers, books, or official reports with correct titles, authors, publishers, and publication years may be listed. Fake or unconfirmed references are strictly prohibited.

## Acceptance Criteria

### Wiki Quality
- [ ] New entity and concept files for Parts 3-6 exist under `/wiki/entities/` and `/wiki/concepts/`.
- [ ] All new files are linked in `/wiki/index.md` and logged in `/wiki/log.md`.

### Document Structure & Style (Chinese & English)
- [ ] All chapters (Parts 3-6) use `pathname:///img/partX_illustration.png` as their header illustration.
- [ ] Chapters have symmetrical comparative sections matching the historical scientific developments of their respective eras.
- [ ] Relevant physics concepts and calculations are mapped into math-infused alert boxes (`[!IMPORTANT]`, `[!NOTE]`, or `[!TIP]`) with LaTeX formulas.
- [ ] All inline LaTeX formulas are padded with outer spaces (e.g. ` $...$ `) to ensure rendering.

### Reference Integrity
- [ ] Every reference listed in all chapters is verified as authentic and correct. No fake titles or synthesized metadata exist.

### Build Verification
- [ ] Running `npm run build` inside `website/` finishes with success and outputs localized static HTML pages for all chapters.

## Follow-up — 2026-06-13T18:04:57Z

Add matplotlib-based scientific plots (PNGs) in Parts 3 and 5.

Guidelines:
1. Generate the following plots:
   - **compton_scattering_fit.py**: For Part 3, plotting X-ray wavelength shift $\Delta \lambda$ vs scattering angle $\theta$ for different targets showing target-independence.
   - **superconductor_transition.py**: For Part 5, plotting resistivity vs temperature curves comparing conventional BCS superconductors (McMillan limit ~30-40K) and YBCO (~93K, liquid nitrogen limit 77K).
   - **fractional_quantum_hall.py**: For Part 5, plotting Hall resistance $R_{xy}$ plateaus ($\nu = 1, 2/3, 1/3$) and longitudinal resistance $R_{xx} \to 0$ vs magnetic field $B$.

2. Maintainability Constraint:
   - Create the python scripts under a new directory: `/Users/johnqiangzhang/Documents/projects/coordinates-physics-china/scripts/plots/` (e.g., `compton_scattering_fit.py`, `superconductor_transition.py`, `fractional_quantum_hall.py`).
   - The scripts, when run, should save their output PNG images directly into `/Users/johnqiangzhang/Documents/projects/coordinates-physics-china/website/static/img/`.
   - Embed these PNG images in the respective Chinese and English chapters (`part3.md`, `part5.md`) using Docusaurus path resolution: `![caption](pathname:///img/filename.png)`.

