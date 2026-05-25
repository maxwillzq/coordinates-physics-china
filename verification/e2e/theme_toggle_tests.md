# Theme Toggle E2E Tests

This file contains Tier 1 and Tier 2 E2E tests for Feature 3: Theme Toggle.
Note: The current Next.js implementation may lack this feature, but tests are written based on Docusaurus requirements.

## Tier 1: Feature Coverage

### Test ID: TT-T1-01
- **Title**: Verify Theme Toggle Button Presence
- **Feature**: Theme Toggle
- **Tier**: 1
- **Description**: Verify that the theme toggle button is visible on the page.
- **Steps**:
  1. Load the site home page or any document page.
  2. Locate the theme toggle button (usually in the header).
- **Expected Results**: The theme toggle button is visible and clickable.

### Test ID: TT-T1-02
- **Title**: Verify Switch to Dark Mode
- **Feature**: Theme Toggle
- **Tier**: 1
- **Description**: Verify that clicking the toggle switches the site to dark mode.
- **Steps**:
  1. Ensure the site is in light mode.
  2. Click the theme toggle button.
- **Expected Results**: The site background becomes dark, and text colors adjust for high contrast.

### Test ID: TT-T1-03
- **Title**: Verify Switch to Light Mode
- **Feature**: Theme Toggle
- **Tier**: 1
- **Description**: Verify that clicking the toggle switches the site back to light mode.
- **Steps**:
  1. Ensure the site is in dark mode.
  2. Click the theme toggle button.
- **Expected Results**: The site background becomes light, and text colors adjust for high contrast.

### Test ID: TT-T1-04
- **Title**: Verify CSS Variables for Light Mode
- **Feature**: Theme Toggle
- **Tier**: 1
- **Description**: Verify that correct CSS variables are applied when in light mode.
- **Steps**:
  1. Set theme to light mode.
  2. Inspect the `<html>` or `<body>` element for theme attributes or classes.
- **Expected Results**: The element has attributes or classes indicating light mode (e.g., `data-theme="light"`).

### Test ID: TT-T1-05
- **Title**: Verify CSS Variables for Dark Mode
- **Feature**: Theme Toggle
- **Tier**: 1
- **Description**: Verify that correct CSS variables are applied when in dark mode.
- **Steps**:
  1. Set theme to dark mode.
  2. Inspect the `<html>` or `<body>` element for theme attributes or classes.
- **Expected Results**: The element has attributes or classes indicating dark mode (e.g., `data-theme="dark"`).

---

## Tier 2: Boundary & Corner Cases

### Test ID: TT-T2-01
- **Title**: Verify Theme Persistence Across Reloads
- **Feature**: Theme Toggle
- **Tier**: 2
- **Description**: Verify that the selected theme persists after a page reload.
- **Steps**:
  1. Switch to dark mode.
  2. Reload the page.
- **Expected Results**: The site remains in dark mode after the reload.

### Test ID: TT-T2-02
- **Title**: Verify Theme Persistence Across Pages
- **Feature**: Theme Toggle
- **Tier**: 2
- **Description**: Verify that the selected theme persists when navigating to another page.
- **Steps**:
  1. Switch to dark mode on the home page.
  2. Navigate to `/posts/part1`.
- **Expected Results**: The Part 1 page also displays in dark mode.

### Test ID: TT-T2-03
- **Title**: Verify Default Theme Matches System Preference
- **Feature**: Theme Toggle
- **Tier**: 2
- **Description**: Verify that the site respects the user's system color scheme preference on first visit.
- **Steps**:
  1. Set system preference to dark mode.
  2. Open the site in a fresh browser session (no stored preference).
- **Expected Results**: The site loads in dark mode automatically.

### Test ID: TT-T2-04
- **Title**: Verify No Flash of Wrong Theme on Load
- **Feature**: Theme Toggle
- **Tier**: 2
- **Description**: Verify that there is no visible flash of the wrong theme during page load.
- **Steps**:
  1. Set theme to dark mode.
  2. Navigate to a new page or reload.
  3. Observe the initial render.
- **Expected Results**: The page renders directly in dark mode without flashing light mode first.

### Test ID: TT-T2-05
- **Title**: Verify Theme Toggle on Mobile View
- **Feature**: Theme Toggle
- **Tier**: 2
- **Description**: Verify that the theme toggle works correctly on mobile screens.
- **Steps**:
  1. Resize browser to mobile width.
  2. Open mobile menu if the toggle is hidden inside it.
  3. Click the theme toggle.
- **Expected Results**: The theme changes successfully on the mobile view.
