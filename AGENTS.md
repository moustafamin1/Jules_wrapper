# AI Agent Instructions

This repository contains a Jules PWA wrapper. The following instructions apply specifically to agents working within this repository. To improve the user experience, agents must notify the user via push notification when they have finished a task or require input.

## Notification Rules

1. **Read Configuration**: Before sending a notification, read the `ntfy_topic` and `app_url` from `notifications.json`.
2. **When to Notify (Strict Timing)**:
    - **The "Last Action" Rule**: The notification `curl` command must be the **absolute last tool call** you make in a turn. This ensures the user is notified only after the state-changing tool (like `submit` or `request_user_input`) has been called.
    - **Task Completion (PR Ready)**: When you have finished all tasks and have called `submit`. Your final tool sequence must be: `[submit, curl]`.
    - **Questions/Blocked**: When you are waiting for the user to respond to a question or clarification. Your final tool sequence must be: `[request_user_input, curl]`.
    - **Plan Approval**: When you have set or revised a plan and are waiting for user approval. Your final tool sequence must be: `[set_plan, request_user_input, curl]`.
    - **Zero Noise Policy**: Never notify for intermediate steps, tests, code reviews, or if you intend to continue working in the next turn. Only notify when you are genuinely handing control back to the user and require their attention.
3. **How to Notify**: Use the `run_in_bash_session` tool to send a POST request to ntfy.sh. If `notifications.json` is missing, ask the user to provide the configuration.
    - **Command Template**:
      ```bash
      curl \
        -H "Title: Jules" \
        -H "Click: <app_url>" \
        -H "Icon: <app_url>/icon.png" \
        -d "<Your concise message here>" \
        https://ntfy.sh/<ntfy_topic>
      ```

By following these rules, the user will receive a push notification the moment you have a Pull Request ready for their review, a question that needs answering, or a plan that needs approval.
