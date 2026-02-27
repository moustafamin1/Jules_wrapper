# Jules PWA Wrapper

A minimal Progressive Web App (PWA) wrapper for [Jules](https://jules.google.com).

This project provides a standalone experience for Jules, including a dark-themed UI, offline caching, and push notification support.

## Features

- **Standalone Mode**: Configured as a minimal-ui standalone app via `manifest.json`.
- **Dark Theme**: Consistent dark aesthetic (`#171718`) across the app and status bar.
- **Offline Caching**: Uses a service worker (`sw.js`) to cache assets and provide faster loading.
- **Push Notifications**: Integrated notification handling via `ntfy.sh`.

## Maintenance

To ensure updates (such as icon or manifest changes) propagate to users, you must bump the cache versions:

1. **Update `index.html`**: Increment the `v` query parameter on the manifest link (e.g., `<link rel="manifest" href="manifest.json?v=8">`).
2. **Update `sw.js`**: Increment the `CACHE_NAME` variable (e.g., `const CACHE_NAME = 'jules-pwa-v8';`) and update any query parameters in the `ASSETS` array.
