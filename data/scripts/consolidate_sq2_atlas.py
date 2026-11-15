"""Consolidate already-committed SQ-2 tier rows (no network, tiers copied verbatim)."""
import re, glob, csv, hashlib, os, collections
rows = {}; dups = []; flagged = []
for f in sorted(glob.glob("logs/*sq2*.md")):
    for ln in open(f, encoding="utf-8"):
        if not re.match(r"^\|\s*(\*\*)?AB\d+", ln): continue
        c = [x.strip().strip("*").strip() for x in ln.strip().strip("|").split("|")]
        code, val = c[0], c[1]
        tier = c[-1] if c[-1] in ("A", "B", "C") else None
        base = os.path.basename(f)
        if tier is None:
            flagged.append((code, val, base, c[-1])); continue
        if code in rows:
            dups.append((code, rows[code][:2] == (val, tier), base)); continue
        rows[code] = (val, tier, base)
os.makedirs("data/derived", exist_ok=True)
out = "data/derived/sq2-sign-confidence-table.csv"
with open(out, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["ab_code", "value", "tier", "source_log", "rubric"])
    for k in sorted(rows, key=lambda s: int(s[2:])):
        w.writerow([k, *rows[k], "logs/2026-09-28-sq2-confidence-rubric-freeze.md"])
print("classified rows:", len(rows), dict(collections.Counter(v[1] for v in rows.values())))
print("flagged:", flagged); print("dups:", dups)
print("sha256", hashlib.sha256(open(out, "rb").read()).hexdigest())
