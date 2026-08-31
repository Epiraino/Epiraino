# Gametime Draft Kit

Draft-night companion app for the Yahoo league **IT'S GAMETIME BABY!!!** (league 825159) —
12-team snake, full PPR, **6-pt passing TDs**, drafted live Fri Sep 4, 2026, 9:00pm EDT.

The kit is a single self-contained HTML app (`index.html`) published as a claude.ai Artifact.
The artifact URL stays stable across republishes, so the same link always has the latest data.

## Files

| File | Purpose |
|---|---|
| `index.html` | The whole app: board, roster tracker, slot strategy, cheat sheets, league notes. Player data is embedded between `/*__PLAYER_DATA_START__*/` and `/*__PLAYER_DATA_END__*/` markers. |
| `players.json` | Synthesized 2026 dataset (source of truth). Web-researched, multi-source cross-checked; `meta.dataAsOf` says how fresh. |
| `build.py` | Injects `players.json` into `index.html`. `python3 build.py --check` prints the embedded `dataAsOf`. |

## Refresh runbook (draft-day wakes follow this)

1. Re-research: current injuries/actives/news + Yahoo ADP movement (web sources dated within days; ≥2 sources per changed fact).
2. Edit `draft-kit/players.json` only — update `injury`, `note`, `yahooAdp`, ranks if warranted, and bump `meta.dataAsOf` (UTC ISO) and `meta.sources`.
3. `python3 draft-kit/build.py` to re-inject.
4. Smoke test in Chromium (no console errors, board renders, marks persist).
5. Republish the artifact to the SAME URL (publish `draft-kit/index.html` again from the session that owns it).
6. Commit `data(draft-kit): …` and push to `claude/fantasy-football-draft-kit-aorkq7`.
7. Message Emilio: top movers, new injury flags, confirmation the link is fresh.

**Hard rule:** no republish after ~8:45pm EDT on draft night — the open page must not be disturbed mid-draft. Live help goes through chat (the app's "Copy status" button pastes roster + drafted state for Claude).

## Notes

- 15 rounds (9 starters QB/2WR/2RB/TE/FLEX/K/DEF + 6 bench; IR isn't drafted), 180 picks.
- Rankings are re-scored for this league: 6-pt pass TDs (~QBs up 1–2 rounds vs default ADP), full PPR, −1 INT/−2 fum.
- Marks (drafted / mine) live in the viewer's browser localStorage — refreshing the data never wipes them.
