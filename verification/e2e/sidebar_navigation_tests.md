# Sidebar Navigation E2E Tests

This file contains Tier 1 and Tier 2 E2E tests for Feature 2: Sidebar Navigation.
Note: The current Next.js implementation may lack this feature, but tests are written based on Docusaurus requirements.

## Tier 1: Feature Coverage

### Test ID: SN-T1-01
- **Title**: Verify Sidebar Presence
- **Feature**: Sidebar Navigation
- **Tier**: 1
- **Description**: Verify that the sidebar is visible on document pages.
- **Steps**:
  1. Navigate to a document page (e.g., `/posts/part1`).
- **Expected Results**: A sidebar is visible on the left side of the page.

### Test ID: SN-T1-02
- **Title**: Verify Sidebar Contains All Parts
- **Feature**: Sidebar Navigation
- **Tier**: 1
- **Description**: Verify that the sidebar lists all 6 parts of the book.
- **Steps**:
  1. Open the sidebar on any document page.
  2. Check the list of items.
- **Expected Results**: The sidebar contains links for Part 1 through Part 6.

### Test ID: SN-T1-03
- **Title**: Verify Sidebar Navigation
- **Feature**: Sidebar Navigation
- **Tier**: 1
- **Description**: Verify that clicking a sidebar item navigates to the correct page.
- **Steps**:
  1. Click on "Part 2" in the sidebar.
- **Expected Results**: The browser navigates to the URL for Part 2 and the content updates.

### Test ID: SN-T1-04
- **Title**: Verify Active Item Highlighting
- **Feature**: Sidebar Navigation
- **Tier**: 1
- **Description**: Verify that the sidebar highlights the currently active page.
- **Steps**:
  1. Navigate to `/posts/part1`.
  2. Observe the sidebar.
- **Expected Results**: The item corresponding to Part 1 is visually highlighted in the sidebar.

### Test ID: SN-T1-05
- **Title**: Verify Sidebar Collapse/Expand
- **Feature**: Sidebar Navigation
- **Tier**: 1
- **Description**: Verify that the sidebar can be collapsed and expanded if applicable.
- **Steps**:
  1. Click the collapse button on the sidebar.
  2. Click the expand button.
- **Expected Results**: The sidebar collapses to save space and expands back to full width.

---

## Tier 2: Boundary & Corner Cases

### Test ID: SN-T2-01
- **Title**: Verify Sidebar on Mobile View
- **Feature**: Sidebar Navigation
- **Tier**: 2
- **Description**: Verify sidebar behavior on small screens.
- **Steps**:
  1. Resize the browser window to mobile width (e.g., 375px).
- **Expected Results**: The sidebar becomes hidden and accessible via a hamburger menu button.

### Test ID: SN-T2-02
- **Title**: Verify Sidebar State Persistence
- **Feature**: Sidebar Navigation
- **Tier**: 2
- **Description**: Verify that the expanded/collapsed state of sidebar categories persists across page reloads.
- **Steps**:
  1. Expand a category in the sidebar.
  2. Refresh the page.
- **Expected Results**: The category remains expanded after the refresh.

### Test ID: SN-T2-03
- **Title**: Verify Handling of Long Titles in Sidebar
- **Feature**: Sidebar Navigation
- **Tier**: 2
- **Description**: Verify that long chapter titles do not break the sidebar layout.
- **Steps**:
  1. Insert a test item with a very long title into the sidebar (simulated or actual).
- **Expected Results**: The title wraps to the next line or is truncated gracefully, without overlapping other elements.

### Test ID: SN-T2-04
- **Title**: Verify Keyboard Navigation in Sidebar
- **Feature**: Sidebar Navigation
- **Tier**: 2
- **Description**: Verify that users can navigate the sidebar using a keyboard.
- **Steps**:
  1. Use the `Tab` key to focus on sidebar items.
  2. Use `Enter` to select an item.
- **Expected Results**: Focus moves correctly through the items, and selection works as expected.

### Test ID: SN-T2-05
- **Title**: Verify Sidebar Sync with Content Navigation
- **Feature**: Sidebar Navigation
- **Tier**: 2
- **Description**: Verify that navigating via content links updates the sidebar active state.
- **Steps**:
  1. Navigate to Part 1.
  2. Click a link in the content area that goes to Part 2.
- **Expected Results**: The browser navigates to Part 2, and the sidebar updates to highlight Part 2.
