# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, etc.) when working with code in this repository. CLAUDE.md is a symlink to this file.

Ultralytics SANDD (AGPL-3.0) holds experimental waveform-processing scripts for the SANDD segmented antineutrino directional detector: pedestal subtraction, pulse timing, charge integration, and pulse-shape candidate selection over raw SiPM waveform dumps. It is a research sandbox — two standalone scripts, no package, no tests.

## Core Principles (CRITICAL)

**Less is more. The simplest solution is the best solution.** The action hierarchy for every change: **Delete > Replace > Add**.

1. **Solve at the owner**: Put behavior in the code path that owns or observes it. For fixes, never guard a symptom with a staleness check, initialization flag, skip-first-call branch, or `try/except` around broken logic; relocate the trigger and delete the wrong path. For features, extend the existing owner rather than creating a parallel abstraction.
2. **Search and reuse first**: Search the whole repository before creating a feature, component, helper, workflow, or utility. Reuse or adapt what exists, consolidate in-scope duplication in the shared owner, and delete duplicate paths. Three similar lines beat a helper nobody else calls.
3. **Delete and modify existing code before creating new code**: Bugfixes are net-negative by default unless deletion and relocation are demonstrably impossible. A new file must first prove it cannot fit cleanly in an existing owner.
4. **Keep scope minimal**: Implement only the simplest complete solution. Avoid impossible-state handling, speculative flags, compatibility shims, policy scaffolding, and unrelated cleanup. Tests are out of scope by default — rely on existing coverage and focused validation; only an uncovered, high-risk regression path justifies minimal new test code.
5. **Ship zero-regression, production-ready changes**: Understand what you remove instead of retaining broken code as insurance. Remove unused imports, functions, types, files, and comments; run relevant cleanup checks; and thoroughly debug and validate the changed owner. Do not break existing features or workflows unless the PR intentionally removes them with evidence.

**Review gate:** for every addition, the reviewer decides whether deleting or changing existing code would have fixed the problem instead — if it would, that is a blocking finding. A missing or thin PR description is never itself a finding.

NEVER push to `main`. NEVER force push. Always start work in a new git worktree (`git worktree add`) on a feature branch and open a PR — never edit the primary checkout directly, it may hold in-flight work.

## PR Workflow

After opening a PR:

1. Wait for the automated PR review and auto-format commit from Ultralytics Actions (`format.yml`), then pull and address every finding.
2. Review the full diff in-session against the Core Principles, performance, and the review gate above, then batch the fixes into one commit and push. After each round of bot or human commits, pull and resume the same reviewer on `<last-reviewed-sha>..HEAD` plus anything that delta could have invalidated. Repeat until the local head matches the live head.
3. Hand off or merge only on a clean final pass: one cold full-diff review returning LGTM with no findings, on a head that is still live at merge time.
4. Never fight other commits: Ultralytics Actions pushes auto-format and header commits, and multiple users may work on the same PR. `git pull --rebase` before pushing; never reset or revert commits you did not author.
5. After the PR merges, clean up: remove local worktrees and branches for it, then `git checkout main && git pull`.

## Commands

```bash
pip3 install -U -r requirements.txt # numpy, scipy, torch, matplotlib
python train.py                     # waveform processing, writes results.png
python waveform_plot.py             # single-waveform figure, writes sample_waveform.pdf (needs ROOT + root_numpy)
```

There is no test suite and no CI beyond `.github/workflows/format.yml` (Ruff, docformatter, Prettier, codespell auto-applied to PR branches) and `cla.yml`.

## Architecture

- `train.py` is the main script. It reads a `.glenn` text dump (one event per row: timestamp, digitizer ID/channel, SiPM ID/channel, sample count, then 400 voltage samples), subtracts the pedestal estimated from the first 60 samples, times each pulse at its maximum derivative, integrates `Q_total` over 220 samples from 5 samples before the leading edge and `Q_tail` over the same window offset by 28 samples, applies amplitude and baseline-noise cuts, and saves a four-panel `results.png` including the `Q_tail/Q_total` pulse-shape-discrimination plot.
- `waveform_plot.py` is an independent figure script that reads the `Waveforms` tree of a ROOT file with `root_numpy` and annotates the integration windows used by `train.py`.
- Both scripts hardcode input paths and filenames near the top and expect local detector data that is not in the repository; neither runs unmodified on a clean checkout. Despite the name, `train.py` trains nothing — the neural-network work lives in [ultralytics/wave](https://github.com/ultralytics/wave).

## Conventions

- Every Python file starts with `# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license` — Ultralytics Actions adds headers automatically; don't add or revert them manually.
- Keep the two scripts standalone; there is no shared package to grow here.
- ROOT and `root_numpy` are optional and must be installed by hand (`root_numpy` is intentionally commented out in `requirements.txt`) — do not make `train.py` depend on them.
