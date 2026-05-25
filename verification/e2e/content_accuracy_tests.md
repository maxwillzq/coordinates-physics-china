# Content Accuracy E2E Tests

This file contains Tier 1 and Tier 2 E2E tests for Feature 4: Content Accuracy.
Content Accuracy means verifying that the content in the migrated site matches the source content in `drafts/`.

## Tier 1: Feature Coverage

### Test ID: CA-T1-01
- **Title**: Verify Part 1 Top-Level Headings
- **Feature**: Content Accuracy
- **Tier**: 1
- **Description**: Verify that all top-level headings in `drafts/part1.md` are present in the migrated site.
- **Steps**:
  1. Open the migrated site page for Part 1.
  2. Compare the headings in the rendered page with the headings in `drafts/part1.md`.
- **Expected Results**: All headings (e.g., "世界轴 (World Axis)", "中国点 (China Point)", "坐标值 (Coordinate Value)") are present and match exactly.

### Test ID: CA-T1-02
- **Title**: Verify Part 1 Text Content Accuracy
- **Feature**: Content Accuracy
- **Tier**: 1
- **Description**: Verify that the text content of the first paragraph in "世界轴 (World Axis)" section of `part1.md` matches the migrated site.
- **Steps**:
  1. Open the migrated site page for Part 1.
  2. Locate the "世界轴 (World Axis)" section.
  3. Compare the text of the first paragraph with the corresponding text in `drafts/part1.md`.
- **Expected Results**: The text matches exactly, including punctuation and spacing.

### Test ID: CA-T1-03
- **Title**: Verify Part 1 References Section
- **Feature**: Content Accuracy
- **Tier**: 1
- **Description**: Verify that all references listed in `drafts/part1.md` are present in the migrated site.
- **Steps**:
  1. Open the migrated site page for Part 1.
  2. Scroll to the "References" section.
  3. Compare the list of references with `drafts/part1.md`.
- **Expected Results**: The list of references matches exactly.

### Test ID: CA-T1-04
- **Title**: Verify Small Post Content Accuracy
- **Feature**: Content Accuracy
- **Tier**: 1
- **Description**: Verify that the content of `test-post.md` is fully and accurately migrated.
- **Steps**:
  1. Open the migrated site page for Test Post.
  2. Compare the full content with `drafts/test-post.md` (excluding frontmatter).
- **Expected Results**: All text content, including headings and paragraphs, matches exactly.

### Test ID: CA-T1-05
- **Title**: Verify Part 2 Availability and Basic Content
- **Feature**: Content Accuracy
- **Tier**: 1
- **Description**: Verify that content from `drafts/part2.md` is accessible and accurate.
- **Steps**:
  1. Open the migrated site page for Part 2.
  2. Verify the main title and first paragraph match `drafts/part2.md`.
- **Expected Results**: The page loads and the content matches.

---

## Tier 2: Boundary & Corner Cases

### Test ID: CA-T2-01
- **Title**: Verify Mixed Language Rendering
- **Feature**: Content Accuracy
- **Tier**: 2
- **Description**: Verify that mixed language content (Chinese and English) in `part1.md` is rendered without encoding issues.
- **Steps**:
  1. Open the migrated site page for Part 1.
  2. Locate sections with mixed language (e.g., "世界轴 (World Axis)").
  3. Verify that both Chinese and English characters are displayed correctly.
- **Expected Results**: No garbled text or encoding errors are visible.

### Test ID: CA-T2-02
- **Title**: Verify Markdown List Preservation
- **Feature**: Content Accuracy
- **Tier**: 2
- **Description**: Verify that markdown list items in `part1.md` preserve their content and numbering order.
- **Steps**:
  1. Open the migrated site page for Part 1.
  2. Locate the list items under "第一节：《墨经》中的物理学曙光".
  3. Compare the content and order with `drafts/part1.md`.
- **Expected Results**: The list items are displayed in the correct order with accurate content.

### Test ID: CA-T2-03
- **Title**: Verify Handling of Special Characters
- **Feature**: Content Accuracy
- **Tier**: 2
- **Description**: Verify that special characters or punctuation in `part1.md` are preserved accurately.
- **Steps**:
  1. Open the migrated site page for Part 1.
  2. Look for specific punctuation like "《墨经》", "“以太”".
  3. Verify they are rendered correctly.
- **Expected Results**: Special characters are rendered correctly as in the source file.

### Test ID: CA-T2-04
- **Title**: Verify No Content Truncation
- **Feature**: Content Accuracy
- **Tier**: 2
- **Description**: Verify that the content of a file is not truncated at the end.
- **Steps**:
  1. Open the migrated site page for Part 1.
  2. Scroll to the very bottom.
  3. Verify that the "References" section is complete and matches the end of `drafts/part1.md`.
- **Expected Results**: All content up to the last line of the source file is visible.

### Test ID: CA-T2-05
- **Title**: Verify Content Accuracy with Frontmatter
- **Feature**: Content Accuracy
- **Tier**: 2
- **Description**: Verify that frontmatter in files like `test-post.md` is correctly handled (i.e., not displayed as raw text but used for metadata, and body content is accurate).
- **Steps**:
  1. Open the migrated site page for Test Post.
  2. Verify that the title from frontmatter is used as the page title or header.
  3. Verify that the body content starts after the frontmatter.
- **Expected Results**: Frontmatter is not visible as raw text, and body content is accurate.
