# PE2 Long Case Cards

A flashcard and checklist web app for final-year long cases. It runs entirely in the browser and can be installed as a home-screen app on Windows, iPhone/iPad and Android.

## Put it online with GitHub Pages

1. Sign in at github.com and create a new **public** repository (for example `pe2-cards`).
2. On the repository page choose **Add file > Upload files**, drag in everything from this folder (including the `icons` folder), and commit.
3. Open **Settings > Pages**. Under "Build and deployment" set Source to **Deploy from a branch**, Branch to **main** and folder **/ (root)**, then Save.
4. After a minute or two the site is live at `https://YOUR-USERNAME.github.io/pe2-cards/`.

## Make the shortcut

- **Android (Chrome):** open the link, tap the three-dot menu, then "Add to Home screen" or "Install app".
- **iPhone/iPad (Safari):** open the link, tap Share, then "Add to Home Screen".
- **Windows (Chrome or Edge):** open the link, then use the install icon in the address bar, or menu > "Apps" / "Save and share" > "Install".

## Your data

Everything you tick, rate, edit or upload is stored in the browser on that device only. Nothing is sent to a server, so devices do not sync with each other.

To move your data to another device, use **Back up my data** on the home page, send the file to the other device, and choose **Restore from backup** there.

## Updating the app

Upload the changed files to the repository again (same names) and commit. Each device picks up the new version the next time it opens the app while online.

## Files

- `index.html` - the app
- `cards.js` - the flashcard answers
- `manifest.webmanifest`, `sw.js`, `icons/` - what makes it installable and usable offline

Study aid only. Check details against current MOH Malaysia CPGs and your lecture notes.
