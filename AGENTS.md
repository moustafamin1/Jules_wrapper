# AI Agent Instructions

This repository contains a Jules PWA wrapper. Agents should follow the global Jules notification protocols.

## Notification Configuration
When completing a task, requesting user input, or hitting a blocker, you MUST send a push notification via `curl` as the **absolute last action** of your turn. Do not notify if you are continuing work autonomously in the next turn (Zero Noise Policy).

- **Notification Topic:** `https://ntfy.sh/jules-notifs-mou-12347`
- **App URL:** `https://moustafamin1.github.io/Jules_wrapper/`

Example:
```bash
curl -d "Jules: Task Completed" "https://ntfy.sh/jules-notifs-mou-12347?click=https://moustafamin1.github.io/Jules_wrapper/"
```

Note: Do not rely on `notifications.json` as it may not exist in all environments. Use the values above.
