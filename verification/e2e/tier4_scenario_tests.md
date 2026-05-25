# Tier 4 Scenario E2E Tests

This file contains Tier 4 E2E tests for Real-World Application Scenarios.

> **Note**: These tests are requirement-driven for the target Docusaurus state and may fail on the current implementation. They assume that content from `drafts/` (like `part1.md`, `part2.md`) will be migrated to the standard Docusaurus content directory (e.g., `website/docs/`), and that URL paths follow Docusaurus conventions (e.g., `/docs/part1`).

## Tier 4: Real-World Application Scenarios

### Test ID: APP-T4-01
- **Title**: Comprehensive Study Session
- **Feature**: Website Availability, Sidebar Navigation, Theme Toggle, Content Accuracy, Math Formula Rendering, SVG Chart Integration
- **Tier**: 4
- **Description**: A user simulates a deep study session, changing themes, navigating, and verifying complex content.
- **Steps**:
  1. Access the home page.
  2. Toggle dark mode.
  3. Navigate to Part 1 via the sidebar.
  4. Read content and verify math formulas are legible.
  5. Navigate to Part 2 via the sidebar.
  6. Verify SVG charts are legible in dark mode.
  7. Toggle light mode while on Part 2.
  8. Verify charts are still legible.
- **Expected Results**: Smooth navigation, correct content loading, and all visual elements (formulas, charts) remain legible across theme changes.

### Test ID: APP-T4-02
- **Title**: Direct Reference Lookup
- **Feature**: Website Availability, Content Accuracy, Math Formula Rendering
- **Tier**: 4
- **Description**: A user follows a link directly to a specific section containing complex formulas.
- **Steps**:
  1. Access `/docs/part1` directly.
  2. Scroll to a specific math formula section.
  3. Verify the formula renders correctly on initial load.
- **Expected Results**: Direct access works, and formulas are rendered correctly without needing to navigate from the home page.

### Test ID: APP-T4-03
- **Title**: Navigation Stress Test / Quick Browsing
- **Feature**: Website Availability, Sidebar Navigation, Content Accuracy
- **Tier**: 4
- **Description**: A user quickly browses through the site, clicking links in rapid succession.
- **Steps**:
  1. Access the home page.
  2. Click Part 1 in the sidebar.
  3. Click Part 2 in the sidebar immediately after Part 1 starts loading or loads.
  4. Click Home in the sidebar.
- **Expected Results**: The site handles rapid navigation without crashing, display errors, or showing incorrect content.

### Test ID: APP-T4-04
- **Title**: Theme Preference Persistence
- **Feature**: Website Availability, Theme Toggle, Sidebar Navigation
- **Tier**: 4
- **Description**: A user sets a theme preference and expects it to be remembered during their session.
- **Steps**:
  1. Access the home page.
  2. Change the theme to dark mode.
  3. Navigate to Part 1 via the sidebar.
  4. Refresh the page (simulating a return or reload).
  5. Verify the theme is still dark mode.
- **Expected Results**: The theme preference is preserved across navigation and page reloads.

### Test ID: APP-T4-05
- **Title**: Content Verification Walkthrough
- **Feature**: Website Availability, Sidebar Navigation, Content Accuracy, SVG Chart Integration
- **Tier**: 4
- **Description**: A user reads through Part 2 specifically to verify the chart content against the text.
- **Steps**:
  1. Access the home page.
  2. Navigate to Part 2.
  3. Verify the presence and accuracy of the SVG chart.
  4. Ensure the chart details match any referencing text.
- **Expected Results**: The chart is visible and matches the content description provided in the text.
