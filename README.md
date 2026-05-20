# Cloud9 JetStream

A dark theme for JetBrains IDEs. Deep navy-black backgrounds, restrained Cloud9-blue accents, and a palette tuned for long coding sessions.

## Install

### From the JetBrains Marketplace (recommended)

Search for **Cloud9 JetStream** in **Settings → Plugins → Marketplace**, install, and activate via **Settings → Appearance & Behavior → Appearance → Theme**.

### From source

Requires Python 3 to package the JAR.

```bash
py create_jar.py
```

This produces `cloud9-jetstream-1.0.0.jar` at the project root. Install it via **Settings → Plugins → ⚙ → Install Plugin from Disk** and select the JAR.

## What's covered

- 90+ syntax tokens with language-specific tuning for Kotlin, Java, Python, JS/TS, SQL, CSS, and Shell/Bash
- Every IDE surface: main menu, tool windows, completion popup, run widget, terminal, debugger, VCS log
- Tuned console ANSI palette
- File-status colors that make VCS changes legible at a glance
- Rainbow brackets cascade through the blue/purple spectrum
- Compatible with JetBrains IDEs from 2023.1 onwards

## Repository layout

```
resources/
  META-INF/
    plugin.xml              Plugin manifest
    pluginIcon.svg          Plugin icon (light contexts)
    pluginIcon_dark.svg     Plugin icon (dark contexts)
  theme/
    cloud9theme.theme.json  UI theme definition
    cloud9-scheme.xml       Editor color scheme
create_jar.py               Build script
```

## License

This project is licensed under the BSD 3-Clause License. See [LICENSE](./LICENSE) for the full text.

---

## Trademark & Branding Notice

The permissions granted under this BSD 3-Clause License apply solely to the source code configuration of the theme. This license does NOT grant any rights or permission to use the "Cloud9" name, logos, trademarks, or associated brand assets. All proprietary branding remains the exclusive property of Cloud9 and cannot be used in derivative works without prior written consent.
