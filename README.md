# Jules PWA Wrapper

A minimal Progressive Web App (PWA) wrapper designed to provide a native-like experience for `jules.google.com`.

## Features

- **PWA Experience:** Standalone display mode with offline caching via Service Workers.
- **Branding:** Custom icons and a splash screen optimized for a seamless launch.
- **Dark Mode:** Consistent `#131314` theme across the manifest and interface.
- **Push Notifications:** Integrated support for `ntfy.sh` to receive system alerts.

## Structure

- `index.html`: Entry point with redirection logic and splash screen.
- `sw.js`: Service Worker for asset caching and notification handling.
- `manifest.json`: Web app manifest for PWA installation.
- `AGENTS.md`: Technical instructions and protocols for AI agents.

## Setup

1. Host these files on a static web server (e.g., GitHub Pages).
2. Configure notifications by following the template in `notifications.example.json`.
3. Add to your home screen on iOS or Android to use as a standalone app.
