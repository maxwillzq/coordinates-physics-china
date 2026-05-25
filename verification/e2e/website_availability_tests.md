# Website Availability E2E Tests

This file contains Tier 1 and Tier 2 E2E tests for Feature 1: Website Availability.

## Tier 1: Feature Coverage

### Test ID: WA-T1-01
- **Title**: Verify Home Page Availability
- **Feature**: Website Availability
- **Tier**: 1
- **Description**: Verify that the home page is accessible and returns a successful status code.
- **Steps**:
  1. Navigate to the base URL of the website (e.g., `/`).
- **Expected Results**: The page loads successfully with an HTTP status code of 200.

### Test ID: WA-T1-02
- **Title**: Verify Part 1 Page Availability
- **Feature**: Website Availability
- **Tier**: 1
- **Description**: Verify that the page for Part 1 is accessible.
- **Steps**:
  1. Navigate to `/posts/part1` (or the corresponding URL for Part 1).
- **Expected Results**: The page loads successfully with an HTTP status code of 200.

### Test ID: WA-T1-03
- **Title**: Verify Part 2 Page Availability
- **Feature**: Website Availability
- **Tier**: 1
- **Description**: Verify that the page for Part 2 is accessible.
- **Steps**:
  1. Navigate to `/posts/part2` (or the corresponding URL for Part 2).
- **Expected Results**: The page loads successfully with an HTTP status code of 200.

### Test ID: WA-T1-04
- **Title**: Verify Custom 404 Page
- **Feature**: Website Availability
- **Tier**: 1
- **Description**: Verify that navigating to a non-existent route returns a 404 page.
- **Steps**:
  1. Navigate to a non-existent URL (e.g., `/non-existent-page`).
- **Expected Results**: The site displays a custom 404 page with an HTTP status code of 404.

### Test ID: WA-T1-05
- **Title**: Verify Static Assets Availability
- **Feature**: Website Availability
- **Tier**: 1
- **Description**: Verify that static assets like the favicon are accessible.
- **Steps**:
  1. Navigate to `/favicon.ico` (or another known static asset path).
- **Expected Results**: The asset is returned successfully with an HTTP status code of 200.

---

## Tier 2: Boundary & Corner Cases

### Test ID: WA-T2-01
- **Title**: Verify Availability with Trailing Slashes
- **Feature**: Website Availability
- **Tier**: 2
- **Description**: Verify that the site handles URLs with and without trailing slashes consistently.
- **Steps**:
  1. Navigate to `/posts/part1/` (with trailing slash).
  2. Navigate to `/posts/part1` (without trailing slash).
- **Expected Results**: Both URLs resolve to the same content, either directly or via a redirect.

### Test ID: WA-T2-02
- **Title**: Verify Availability with Query Parameters
- **Feature**: Website Availability
- **Tier**: 2
- **Description**: Verify that adding query parameters does not break page availability.
- **Steps**:
  1. Navigate to `/posts/part1?ref=test`.
- **Expected Results**: The page loads successfully and displays the correct content, ignoring the query parameter if not used.

### Test ID: WA-T2-03
- **Title**: Verify Case Sensitivity in URLs
- **Feature**: Website Availability
- **Tier**: 2
- **Description**: Verify how the site handles case sensitivity in URLs.
- **Steps**:
  1. Navigate to `/POSTS/part1`.
- **Expected Results**: The site should either gracefully redirect to the lowercase version or return a 404 page, but not crash.

### Test ID: WA-T2-04
- **Title**: Verify Deep Link Availability
- **Feature**: Website Availability
- **Tier**: 2
- **Description**: Verify that navigating directly to a section anchor works.
- **Steps**:
  1. Navigate to `/posts/part1#section-id` (assuming section IDs exist).
- **Expected Results**: The page loads and scrolls to the specified section.

### Test ID: WA-T2-05
- **Title**: Verify Availability of Large Content Pages
- **Feature**: Website Availability
- **Tier**: 2
- **Description**: Verify that pages with large content load successfully without timing out.
- **Steps**:
  1. Navigate to a page known to have large content (e.g., a full compilation page if available).
- **Expected Results**: The page loads within an acceptable time frame.
