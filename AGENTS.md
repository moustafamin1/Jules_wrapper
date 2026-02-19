# AI Agent Instructions

This repository contains a Jules PWA wrapper. To improve the user experience, agents must notify the user via push notification when they have finished a task or require input.

## Notification Rules

1. **Read Configuration**: Before sending a notification, read the `ntfy_topic` and `app_url` from `notifications.json`.
2. **When to Notify (Zero Noise Policy)**:
    - **No Intermediate Pings**: Never send a notification for "internal testing", "verification", "code reviews", "pre-commit steps", or "progress updates".
    - **Final Turn Only**: Only send a notification in the turn where you are actually finishing your work or asking a question.
    - **The "Last Action" Rule**: The notification `curl` command must be the **absolute last tool call** you make in a turn.
    - **Completion**: Only notify when you are 100% finished and are about to call `submit`. Your final tool sequence in that turn must be: `[..., curl, submit]`.
    - **Questions/Blocked**: Only notify when you are waiting for the user. Your final tool sequence in that turn must be: `[..., curl, request_user_input]`.
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

By following these rules, you ensure that the user is only interrupted when their presence is actually required to move the task forward.
