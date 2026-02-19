# AI Agent Instructions

This repository contains a Jules PWA wrapper. To improve the user experience, agents must notify the user via push notification when they have finished a task or require input.

## Notification Rules

1. **Read Configuration**: Before sending a notification, read the `ntfy_topic` and `app_url` from `notifications.json`.
    - **Note**: `notifications.json` is ignored by git for security. If it is missing, check `notifications.example.json` to see how to create it.
2. **When to Notify (Strict Timing)**:
    - **The "Last Action" Rule**: The notification `curl` command must be the **absolute last tool call** you make in a turn. Do not perform any other work, read any more files, or run any more tests after sending the notification.
    - **Completion**: Only notify when you are 100% finished and are about to call `submit`. Your final tool sequence should be: `[curl, submit]`.
    - **Questions/Blocked**: Only notify when you are waiting for the user. Your final tool sequence should be: `[curl, request_user_input]`.
    - **No Intermediate Pings**: Never send a notification if you intend to continue working in the next turn. The user should never open the app and see "Jules is thinking" or see work in progress.
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
    - **Example**:
      ```bash
      curl \
        -H "Title: Jules" \
        -H "Click: https://moustafamin1.github.io/Jules_wrapper/" \
        -H "Icon: https://moustafamin1.github.io/Jules_wrapper/icon.png" \
        -d "Task complete! You can now check the results." \
        https://ntfy.sh/your-private-topic
      ```

By following these rules, you ensure that when the user taps the notification, the app is ready for their immediate review or response.
