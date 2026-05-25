# E2E Tests for Feature 6: SVG Chart Integration

This file contains Tier 1 and Tier 2 E2E tests for Feature 6: SVG Chart Integration.
SVG Chart Integration means verifying that SVG charts are correctly embedded and rendered on the site.

## Tier 1: Feature Coverage

- Test ID: E2E_F6_T1_01
- Title: Verify SVG Chart Rendering on Page
- Feature: SVG Chart Integration
- Tier: 1
- Description: Verify that the SVG chart is correctly embedded in the page and exists in the DOM.
- Steps:
  1. Navigate to a page containing an SVG chart (e.g., a post referencing `wu_youxun_spectrum.svg`).
  2. Inspect the DOM to locate the `<svg>` element.
- Expected Results: The `<svg>` element exists in the DOM and is not empty.

- Test ID: E2E_F6_T1_02
- Title: Verify SVG Chart Dimensions and ViewBox
- Feature: SVG Chart Integration
- Tier: 1
- Description: Verify that the SVG chart has valid width, height, or viewBox attributes.
- Steps:
  1. Navigate to the page containing the SVG chart.
  2. Inspect the `<svg>` element's attributes.
- Expected Results: The `<svg>` element has `viewBox` or `width` and `height` attributes with valid positive values.

- Test ID: E2E_F6_T1_03
- Title: Verify SVG Chart Visibility
- Feature: SVG Chart Integration
- Tier: 1
- Description: Verify that the SVG chart is visible to the user and not hidden by CSS.
- Steps:
  1. Navigate to the page containing the SVG chart.
  2. Check the computed style of the `<svg>` element for `display`, `visibility`, and `opacity`.
- Expected Results: The SVG is visible (e.g., `display` is not `none`, `visibility` is `visible`, and `opacity` is greater than 0).

- Test ID: E2E_F6_T1_04
- Title: Verify SVG Chart Accessibility
- Feature: SVG Chart Integration
- Tier: 1
- Description: Verify that the SVG chart has accessibility labels such as `aria-label` or a `<title>` element.
- Steps:
  1. Navigate to the page containing the SVG chart.
  2. Inspect the `<svg>` element for `aria-label`, `aria-labelledby`, or a child `<title>` element.
- Expected Results: At least one accessibility attribute or element is present to describe the chart.

- Test ID: E2E_F6_T1_05
- Title: Verify SVG Chart Content Rendering
- Feature: SVG Chart Integration
- Tier: 1
- Description: Verify that the internal elements of the SVG (paths, text) are rendered.
- Steps:
  1. Navigate to the page containing the SVG chart.
  2. Inspect the child elements of the `<svg>`.
- Expected Results: The SVG contains rendered elements like `<path>`, `<text>`, or `<rect>`, indicating it is not a blank canvas.

## Tier 2: Boundary & Corner Cases

- Test ID: E2E_F6_T2_01
- Title: Verify SVG Chart Responsiveness on Mobile
- Feature: SVG Chart Integration
- Tier: 2
- Description: Verify that the SVG chart scales correctly on small screens without breaking layout.
- Steps:
  1. Navigate to the page containing the SVG chart.
  2. Resize the browser viewport to mobile width (e.g., 375px).
  3. Verify the rendering and layout of the chart.
- Expected Results: The SVG chart scales down proportionally and does not overflow the screen horizontally.

- Test ID: E2E_F6_T2_02
- Title: Verify SVG Chart in Dark Mode
- Feature: SVG Chart Integration
- Tier: 2
- Description: Verify that the SVG chart remains legible and has adequate contrast in dark mode.
- Steps:
  1. Navigate to the page containing the SVG chart.
  2. Toggle the site to dark mode.
  3. Verify the visibility and legibility of the chart content.
- Expected Results: The chart content (lines, text) is legible against the dark background.

- Test ID: E2E_F6_T2_03
- Title: Verify Behavior When SVG Asset is Missing
- Feature: SVG Chart Integration
- Tier: 2
- Description: Verify that the site handles a missing SVG asset gracefully.
- Steps:
  1. Simulate a missing SVG asset (e.g., block the network request for the SVG or use a non-existent path).
  2. Load the page that references the SVG.
- Expected Results: The page does not crash; a broken image icon or fallback text is displayed.

- Test ID: E2E_F6_T2_04
- Title: Verify SVG Chart with Invalid Content
- Feature: SVG Chart Integration
- Tier: 2
- Description: Verify that the site handles invalid or malformed SVG content gracefully.
- Steps:
  1. Navigate to a page with an invalid SVG file (e.g., corrupted XML).
  2. Observe the rendering behavior.
- Expected Results: The site does not crash; the browser may show an error indicator or nothing, but the rest of the page is functional.

- Test ID: E2E_F6_T2_05
- Title: Verify SVG Chart at Extreme Viewport Sizes
- Feature: SVG Chart Integration
- Tier: 2
- Description: Verify that the SVG chart renders correctly at extreme viewport sizes (e.g., 4K resolution).
- Steps:
  1. Navigate to the page containing the SVG chart.
  2. Set the viewport width to 3840px (4K).
  3. Verify the rendering of the chart.
- Expected Results: The SVG chart renders without pixelation and maintains its aspect ratio.
