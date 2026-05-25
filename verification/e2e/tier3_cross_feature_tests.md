# Tier 3 Cross-Feature E2E Tests

This file contains Tier 3 E2E tests for Cross-Feature Combinations.

> **Note**: These tests are requirement-driven for the target Docusaurus state and may fail on the current implementation. They assume that content from `drafts/` (like `part1.md`, `part2.md`) will be migrated to the standard Docusaurus content directory (e.g., `website/docs/`), and that URL paths follow Docusaurus conventions (e.g., `/docs/part1`).

## Tier 3: Cross-Feature Combinations

### Test ID: CFC-T3-01
- **Title**: Theme Toggle and SVG Chart Interaction
- **Feature**: Theme Toggle, SVG Chart Integration
- **Tier**: 3
- **Description**: Verify that SVG charts are legible and correctly rendered when toggling between light and dark themes.
- **Steps**:
  1. Navigate to a page containing an SVG chart (e.g., Part 2).
  2. Observe the chart in light mode.
  3. Toggle the theme to dark mode.
  4. Observe the chart again.
- **Expected Results**: The chart should be legible in both modes. Colors should adapt or contrast well enough to remain visible.

### Test ID: CFC-T3-02
- **Title**: Theme Toggle and Math Formula Rendering
- **Feature**: Theme Toggle, Math Formula Rendering
- **Tier**: 3
- **Description**: Verify that MathJax formulas are legible and correctly rendered when toggling between light and dark themes.
- **Steps**:
  1. Navigate to a page containing math formulas (e.g., Part 1).
  2. Observe the formulas in light mode.
  3. Toggle the theme to dark mode.
  4. Observe the formulas again.
- **Expected Results**: The formulas should be legible in both modes. Text color should adjust to contrast with the background.

### Test ID: CFC-T3-03
- **Title**: Sidebar Navigation and Content Accuracy
- **Feature**: Sidebar Navigation, Content Accuracy
- **Tier**: 3
- **Description**: Verify that navigating via the sidebar loads the correct content for the selected page.
- **Steps**:
  1. On the home page, use the sidebar to navigate to Part 1.
  2. Verify the content matches Part 1.
  3. Use the sidebar to navigate to Part 2.
  4. Verify the content matches Part 2.
- **Expected Results**: The content should update correctly and match the expected content for each page.

### Test ID: CFC-T3-04
- **Title**: Theme Toggle Persistence Across Navigation
- **Feature**: Theme Toggle, Sidebar Navigation
- **Tier**: 3
- **Description**: Verify that the selected theme persists when navigating to another page via the sidebar.
- **Steps**:
  1. On the home page, toggle the theme to dark mode.
  2. Use the sidebar to navigate to Part 1.
  3. Observe the theme on the Part 1 page.
- **Expected Results**: The Part 1 page should also be in dark mode.

### Test ID: CFC-T3-05
- **Title**: Sidebar Navigation and SVG Chart Rendering
- **Feature**: Sidebar Navigation, SVG Chart Integration
- **Tier**: 3
- **Description**: Verify that SVG charts render correctly after navigating to a page via the sidebar.
- **Steps**:
  1. Navigate to the home page.
  2. Use the sidebar to navigate to a page with an SVG chart (e.g., Part 2).
  3. Verify that the chart renders correctly.
- **Expected Results**: The chart should be fully rendered and interactive if applicable.
