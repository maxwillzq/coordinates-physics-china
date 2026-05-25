# Tier 1 E2E Tests for Feature 5: Math Formula Rendering

- Test ID: E2E_F5_T1_01
- Title: Render Inline LaTeX Formula
- Feature: Math Formula Rendering
- Tier: 1
- Description: Verify that simple inline LaTeX formulas are rendered correctly.
- Steps:
  1. Navigate to a post containing inline math (e.g., `/docs/test-post`).
  2. Locate the text containing `$E = mc^2$`.
- Expected Results: The formula is rendered as a formatted math expression, not as plain text `$E = mc^2$`.

- Test ID: E2E_F5_T1_02
- Title: Render Block LaTeX Formula
- Feature: Math Formula Rendering
- Tier: 1
- Description: Verify that block LaTeX formulas are rendered correctly.
- Steps:
  1. Navigate to a post containing block math (e.g., `/docs/test-post`).
  2. Locate the block formula containing the integral.
- Expected Results: The formula is rendered as a centered, formatted math expression.

- Test ID: E2E_F5_T1_03
- Title: Render Greek Letters
- Feature: Math Formula Rendering
- Tier: 1
- Description: Verify that formulas with Greek letters are rendered correctly.
- Steps:
  1. Navigate to a post containing Greek letters (e.g., `/docs/part3`).
  2. Locate the formula `$E = h\nu$`.
- Expected Results: The Greek letter `\nu` is rendered correctly.

- Test ID: E2E_F5_T1_04
- Title: Render Subscripts and Superscripts
- Feature: Math Formula Rendering
- Tier: 1
- Description: Verify that subscripts and superscripts are rendered correctly.
- Steps:
  1. Navigate to a post containing subscripts/superscripts (e.g., `/docs/part6`).
  2. Locate the formula `$10^{15}$`.
- Expected Results: The superscript is rendered correctly.

- Test ID: E2E_F5_T1_05
- Title: Render Complex Formula (Integral/Fraction)
- Feature: Math Formula Rendering
- Tier: 1
- Description: Verify that complex formulas with integrals and fractions are rendered correctly.
- Steps:
  1. Navigate to a post containing a complex formula (e.g., `/docs/test-post`).
  2. Locate the formula `$$\int_{a}^{b} x^2 dx = \frac{b^3 - a^3}{3}$$`.
- Expected Results: The integral and fraction are rendered correctly with appropriate symbols.
