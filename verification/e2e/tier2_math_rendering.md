# Tier 2 E2E Tests for Feature 5: Math Formula Rendering

- Test ID: E2E_F5_T2_01
- Title: Formula with Special Characters
- Feature: Math Formula Rendering
- Tier: 2
- Description: Verify rendering of formulas with special characters and operations.
- Steps:
  1. Create a test post or navigate to one containing a formula with special characters like `\sqrt{x^2 + y^2}`, `\alpha \beta`, or `\sum_{i=1}^{n}`.
  2. Verify that these are rendered correctly by KaTeX.
- Expected Results: Special characters and operations are rendered correctly.

- Test ID: E2E_F5_T2_02
- Title: Very Long Formula (Overflow Test)
- Feature: Math Formula Rendering
- Tier: 2
- Description: Verify that a very long formula does not break the layout and handles overflow.
- Steps:
  1. Create a test post with a very long formula that exceeds the width of a standard mobile or desktop screen.
  2. View the post on the site.
- Expected Results: The formula does not overflow the container and break the layout. It should either be scrollable or wrapped gracefully.

- Test ID: E2E_F5_T2_03
- Title: Formula with Invalid Syntax
- Feature: Math Formula Rendering
- Tier: 2
- Description: Verify that invalid LaTeX syntax does not crash the page.
- Steps:
  1. Create a test post with invalid LaTeX syntax (e.g., `$E = mc^2` missing the closing `$`).
  2. Navigate to the post.
- Expected Results: The page renders without crashing. The invalid formula may be displayed as raw text or an error message, but the rest of the page should be functional.

- Test ID: E2E_F5_T2_04
- Title: Multiple Formulas in One Paragraph
- Feature: Math Formula Rendering
- Tier: 2
- Description: Verify that multiple inline formulas in the same paragraph are rendered correctly without interference.
- Steps:
  1. Create a test post with content like: "If $a=b$ and $b=c$, then $a=c$."
  2. Navigate to the post and verify all three formulas.
- Expected Results: All formulas are rendered correctly and independent of each other.

- Test ID: E2E_F5_T2_05
- Title: Formula in Headings
- Feature: Math Formula Rendering
- Tier: 2
- Description: Verify that formulas placed in headings are rendered correctly.
- Steps:
  1. Create a test post with a heading like: `# Theorem: $a^2 + b^2 = c^2$`.
  2. Navigate to the post.
- Expected Results: The formula in the heading is rendered correctly and retains the heading style (e.g., font size).
