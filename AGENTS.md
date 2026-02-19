# AI Agent Instructions

This repository contains a Jules PWA wrapper. To improve the user experience, agents must notify the user when they have finished a task or require input.

## Notification Rules

1. **Read Configuration**: Before sending a notification, read the `ntfy_topic` from `notifications.json`.
2. **When to Notify**:
    - Right before or after using `message_user`.
    - Right before or after using `request_user_input`.
    - When you have completed all tasks and are about to call `submit`.
3. **How to Notify**: Use the `run_in_bash_session` tool to send a POST request to ntfy.sh.
    - Command: `curl -d "<Your message here>" ntfy.sh/<ntfy_topic>`
    - Example: `curl -d "I have finished the task. Please review." ntfy.sh/jules-notifs-mou-12347`

By following these rules, the user will receive a push notification on their Android device via the ntfy app.
