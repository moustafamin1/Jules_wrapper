# AI Agent Instructions

This repository contains a Jules PWA wrapper. To improve the user experience, agents must notify the user via push notification when they have finished a task or require input.

## Notification Rules

1. **Read Configuration**: Before sending a notification, read the `ntfy_topic` and `app_url` from `notifications.json`.
2. **When to Notify (Strict Timing)**:
    - **Questions**: If you need to ask the user a question using `request_user_input`, send the notification in the **same turn**, immediately *before* calling the tool.
    - **Completion**: When you have finished all tasks and are about to call `submit`, send the notification as the **final tool call** before the submit.
    - **Avoid Noise**: Do not send notifications for intermediate steps, progress updates, or internal tests. Only notify when the user actually needs to take action or see a result.
3. **How to Notify**: Use the `run_in_bash_session` tool to send a POST request to ntfy.sh with specific headers.
    - **Command Template**:
      ```bash
      curl \
        -H "Title: Jules" \
        -H "Click: <app_url>" \
        -H "Icon: <app_url>/icon.png" \
        -d "<Your concise message here>" \
        https://ntfy.sh/<ntfy_topic>
      ```
    - **Example**:
      ```bash
      curl \
        -H "Title: Jules" \
        -H "Click: https://moustafamin1.github.io/Jules_wrapper/" \
        -H "Icon: https://moustafamin1.github.io/Jules_wrapper/icon.png" \
        -d "I have finished setting up your app. Please review the changes." \
        https://ntfy.sh/jules-notifs-mou-12347
      ```

By following these rules, the user will only be interrupted when there is something ready for them to see in the app.
