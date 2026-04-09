---
date: 2026-04-09
project: product-os + unfry
topics: [product-os, github, unfry, brain-fry, daemon, linkedin]
duration: long
---

# /unfry — 2026-04-09 — product-os + Unfry

## Summary
- סקרנו את מצב Product OS: framework בנוי, GitHub repo מעורב (ערבוב framework + data), קשר ל-remote אבד
- יצרנו שני repos חדשים: `product-os-framework` (public) + `unfry` (public, שמוקדם היה claude-session-log)
- הגדרנו מחדש את רעיון ה-session log: לא skill ידני — daemon שמנטר Claude Code אוטומטית
- מצאנו שהנתונים כבר קיימים: `~/.claude/projects/*/session.jsonl` — הכל שמור, אף אחד לא עושה איתם כלום
- ה-pivot: Brain Fry מגיע מ**פיקוח** על AI, לא משימוש. זה שינה את ה-positioning לגמרי
- בנינו PITCH.md + PRD-Strategic.md + LinkedIn post + `/unfry` skill — והתקנת אותו

## Key Decisions
- **Unfry, לא Offload/Defrag**: הקהל הוא PM builders — Unfry מדבר ישר לשיחה שהם כבר מנהלים
- **שני tiers**: `/unfry` slash command (zero friction, 30 שניות) + daemon (אוטומטי, למתקדמים)
- **כל project repos = private, product-os-framework = public**: הפרדה ברורה framework vs data
- **Daemon, לא skill**: מה שרצית זה process-level monitoring — לא משהו שרץ בתוך Claude

## Insights
- הנתונים כבר שם — Claude Code שומר הכל ב-JSONL. אף אחד לא בנה מעליהם עדיין. זה ה-window
- "Unfry" עובד כי הוא מגיע מתוך הנרטיב של הקהל עצמו — לא תיאור פונקציונלי
- ה-`/unfry` slash command כ-entry point חכם יותר מהdaemon — מאמת demand לפני שבונים את הקשה

## Next Steps
1. לעלות את ה-`/unfry` skill ל-GitHub (עדיין לא push)
2. לעדכן README עם installation instructions
3. לבנות את ה-daemon (V2)
4. לפרסם את ה-LinkedIn post
5. להחליט מה עם ה-repo הישן `rinatwe1/product-os`
