# Assignment 3 — Application Installation and Configuration

## Application Table

| Application | Version | Purpose | Configuration performed | Result |
| --- | --- | --- | --- | --- |
| Google Chrome | 157.0.8103.79 | Web browsing | Checked version, verified default search engine, download folder, startup behavior, privacy and security settings, configured user profile, and tested loading multiple websites (Google Classroom, GitHub, example.com, python.org). | Completed |
| Telegram Desktop | 7.4.4 x64 | Messaging, media sharing, and calls | Checked version and Windows 11 compatibility, reviewed notification settings, checked microphone/camera device settings, verified user profile, and tested messaging via Saved Messages. | Completed |
| SQLite (Python `sqlite3` & DBeaver) | SQLite 3.50.4 / DBeaver 26.1.5 | Embedded relational database and DB management | Verified environment, created test database `demo.sqlite3` with table `items` via `demo_database.py`, verified integrity, and opened table data in DBeaver. | Completed |

## Installation and Verification Summary

- **Environment:** Windows 11 Home x64 (build 10.0.26300), 32 GB RAM.
- **Google Chrome (Task 1):** Verified installed version (`157.0.8103.79`). Reviewed internal settings, search engine, download path, startup behavior, Privacy and security options, and user profile menu. Confirmed browsing functionality by opening multiple websites in separate tabs.
- **Telegram Desktop (Task 2):** Verified compatibility and version (`7.4.4 x64`) under **Settings → Advanced → Version and updates**. Inspected **Notifications and Sounds**, **My Account / Profile**, and **Speakers and Camera** device settings. Verified core messaging functionality by sending a test message in **Saved Messages**.
- **SQLite & DBeaver (Task 3):** SQLite (`3.50.4`) is bundled with Python and requires no separate server installation. Executed `demo_database.py` to generate `demo.sqlite3`, create the `items` table, insert the test record `(1, 'Sample')`, and pass `PRAGMA integrity_check`. Connected `demo.sqlite3` in **DBeaver 26.1.5** and confirmed direct access to the `items` table data.

## Task 4 — Configured Settings

Selected applications: **Google Chrome** and **Telegram Desktop**.

| Application | Setting | Configured State | Reason |
| --- | --- | --- | --- |
| Google Chrome | Default search engine | Google | Fast and reliable default search for study and development tasks. |
| Google Chrome | Download location | Default Downloads folder verified | Ensures predictable file organization for downloaded study materials. |
| Google Chrome | Privacy and security | Standard protection and site permissions reviewed | Balances site compatibility with safe browsing protection. |
| Google Chrome | User profile | Active personal profile with sync configured | Keeps bookmarks, extensions, and study platforms (Classroom, GitHub) separated and accessible. |
| Telegram Desktop | Notifications and Sounds | Desktop alerts and notification preferences configured | Prevents missing important messages while controlling alert noise. |
| Telegram Desktop | Speakers and Camera | Audio/video input and output devices verified | Prepares the app for voice/video calls and checks hardware selection. |

## Screenshots Included (`screenshots/`)

- **Google Chrome:** settings, search engine, downloads, startup, privacy and security, active user profile, and loaded websites (`Снимок экрана 2026-11-17 214855.png`, `215227.png`, `215302.png`, `215412.png`, `215554.png`, `215627.png`).
- **Telegram Desktop:** notifications, general settings, user profile, speakers and camera, version info (`Снимок экрана 2026-11-17 215114.png`, `215857.png`, `220001.png`, `220051.png`, `220139.png`, `220517.png`), and Saved Messages basic test (`telegram-test.png`).
- **Database (SQLite / DBeaver):** `demo.sqlite3` opened in DBeaver showing `items` table data `(1, 'Sample')` (`Снимок экрана 2026-11-17 221151.png`).

## Conclusion

All three categories of application software (web browser, communication app, and database tool) were verified, configured, and tested on Windows 11. Browser settings and user profile were reviewed and confirmed on live websites, Telegram Desktop settings and basic messaging were verified, and a local SQLite database was successfully created, checked for integrity, and accessed through DBeaver.