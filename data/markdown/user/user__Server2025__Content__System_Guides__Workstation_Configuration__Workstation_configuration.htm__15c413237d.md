---
title: "Workstation configuration"
url: https://help.relativity.com/Server2025/Content/System_Guides/Workstation_Configuration/Workstation_configuration.htm
collection: user
fetched_at: 2026-06-22T06:04:51+00:00
sha256: 7ab9ab4b7f720390e939b40d5333aa59a28031d0ea363afd69463ec8294f42e7
---

Workstation configuration

# Workstation configuration

Before using Relativity for document review, it's important to consider workstation configuration properties potentially required in your environment. This document outlines those workstation components that ensure Relativity’s accessibility and functionality.

## Considerations for all browsers

Relativity does not support the following:

- Accessing the same Relativity instance with multiple tabs at the same time.

- Accessing the same Relativity instance with multiple browsers at the same time.

## Google Chrome (Mac and PC) considerations

### Disable pop-up blocker

Relativity opens new windows where you can perform specific actions. Your web browser's pop-up blocker may block new windows from opening by default. Refer to Manage pop-ups for instructions to disable the pop-up blocker in Google Chrome. For instructions to disable pop-up blocker using a wildcard in Chrome, open a Chrome web browser and follow the instructions below:

- Click the three vertical dots in the upper right-hand corner in Chrome

- Click Settings. Scroll down to the bottom

- Click Advanced .

- Click Content Settings .

- Click Pop-ups and redirects .

- Underneath Allow, click Add .

- Enter in “https://[*.]relativity.one”

- Click Add .

- Close Settings in Chrome.

### Additional settings

Refer to Browser specific considerations for information on additional settings for Chrome.

## Safari (Mac only) considerations

### Disable Pop-up blocker

Relativity opens new windows where you can perform specific actions. Your web browser's pop-up blocker may block new windows from opening by default. Make sure to disable the pop-up blocker when you're working in Safari.

### Additional settings

Refer to Browser specific considerations for information on additional settings for Safari.

### Disable Pop-up blocker

Relativity opens new windows where you can perform specific actions. Your web browser's pop-up blocker may block new windows from opening by default . Refer to your browser's privacy and security settings for instructions to disable the pop-up blocker.

### Network considerations

- The viewer uses the RelativityWebAPI as well as the Relativity.Distributed components.

Inside the viewer, the Distributed piece is called from within the application, as indicated by the URL referenced in the bottom left corner of the viewer pane.

- The files retrieved in the viewer are HTTPS.

If a user does not have the latest Microsoft updates to add 3rd Party Certificate authorities as trusted certificates, an error message could occur, even if the user is using the correct website.
