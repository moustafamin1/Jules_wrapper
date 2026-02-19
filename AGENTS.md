# AI Agent Instructions

This repository contains a Jules PWA wrapper. To improve the user experience, notifications are sent to the user when tasks are completed or input is required.

## Notification Strategy

1. **Automated Completion Notifications**:
    - **Do NOT** send a manual notification when you call `submit`.
    - A GitHub Action is configured to automatically send a "Task Complete" notification once your code is pushed. This ensures the user only gets notified *after* the work is truly finished.

2. **Manual Input Notifications**:
    - **DO** send a manual notification when you use `request_user_input`.
    - **Timing**: Send the notification as the **absolute last action** before calling `request_user_input`.
    - **Rule**: No other tool calls or work should follow the notification in that turn.

## Manual Notification Instructions

- **Read Configuration**: Read the `ntfy_topic` and `app_url` from `notifications.json`.
- **Command Template**:
  ```bash
  curl \
    -H "Title: Jules" \
    -H "Click: <app_url>" \
    -H "Icon: <app_url>/icon.png" \
    -d "<Your concise question or reason for being blocked>" \
    https://ntfy.sh/<ntfy_topic>
  ```

By following these rules, the user only receives manual pings when their immediate action is required, while task completions are handled reliably by the system.
