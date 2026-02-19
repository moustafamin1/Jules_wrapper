# AI Agent Instructions

This repository contains a Jules PWA wrapper. To improve the user experience, agents must notify the user via push notification when they have finished a task or require input.

## Notification Rules

1. **Read Configuration**: Before sending a notification, read the `ntfy_topic` and `app_url` from `notifications.json`.
2. **When to Notify (Strict Timing)**:
    - **The "Last Action" Rule**: The notification `curl` command must be the **absolute last tool call** you make in a turn.
    - **Task Completion (PR Ready)**: When you have finished all tasks and are about to call `submit` (which creates a pull request), send a manual notification. Your final tool sequence must be: `[curl, submit]`.
    - **Questions/Blocked**: When you are waiting for the user to respond to a question. Your final tool sequence must be: `[curl, request_user_input]`.
    - **Avoid Noise**: Never send a notification if you intend to continue working in the next turn.
3. **How to Notify**: Use the `run_in_bash_session` tool to send a POST request to ntfy.sh.
    - **Command Template**:
      ```bash
      curl \
        -H "Title: Jules" \
        -H "Click: <app_url>" \
        -H "Icon: <app_url>/icon.png" \
        -d "<Your concise message here>" \
        https://ntfy.sh/<ntfy_topic>
      ```

By following these rules, the user will receive a push notification the moment you have a Pull Request ready for their review or a question that needs answering.
