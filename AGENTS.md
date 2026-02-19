# AI Agent Instructions

This repository contains a Jules PWA wrapper. To improve the user experience, agents must notify the user when they have finished a task or require input.

## Notification Rules

1. **Read Configuration**: Before sending a notification, read the `ntfy_topic` and `app_url` from `notifications.json`.
2. **When to Notify**:
    - Right before or after using `message_user`.
    - Right before or after using `request_user_input`.
    - When you have completed all tasks and are about to call `submit`.
3. **How to Notify**: Use the `run_in_bash_session` tool to send a POST request to ntfy.sh with specific headers to ensure the notification looks good and opens the app when clicked.
    - **Command**:
      ```bash
      curl \
        -H "Title: Jules" \
        -H "Click: <app_url>" \
        -H "Icon: <app_url>/icon.png" \
        -H "Tags: robot" \
        -d "<Your message here>" \
        https://ntfy.sh/<ntfy_topic>
      ```
    - **Example**:
      ```bash
      curl \
        -H "Title: Jules" \
        -H "Click: https://moustafamin1.github.io/Jules_wrapper/" \
        -H "Icon: https://moustafamin1.github.io/Jules_wrapper/icon.png" \
        -H "Tags: robot" \
        -d "I have finished the task. Please review." \
        https://ntfy.sh/jules-notifs-mou-12347
      ```

By following these rules, the user will receive a styled push notification on their Android device that opens the Jules wrapper directly when tapped.
