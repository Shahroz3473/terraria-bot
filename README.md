# Terraria AFK Bot

Python project for a scheduled Terraria server client.

## Features

- Reads server settings from `config.json`
- Runs from GitHub Actions
- Connection logging and error handling
- Designed for a real Terraria protocol implementation

## Important

A Terraria 1.4.5.6 player client requires the complete binary networking protocol implementation. This repository currently contains the client foundation and connection layer. Fake TCP pings are intentionally not used.
