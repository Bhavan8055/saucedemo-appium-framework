# Movie App Automation Framework

This project is an Appium automation framework for an Android movie mobile application using Python and Pytest.

## Architecture Overview

- `pages/`: Page Object Model classes for each screen in the app.
- `tests/`: Pytest test cases covering login, registration, search, movie details, favorites, watchlist, profile update, and logout.
- `utilities/`: Helpers for Appium driver creation, logging, screenshot capture, and data loading.
- `config/`: Global configuration values for Appium, timeouts, and filesystem paths.
- `reports/`: HTML report output location.
- `screenshots/`: Screenshots captured on test failure.
- `testdata/`: Data-driven test inputs.

## Setup Instructions

### 1. Install Python and packages

1. Install Python 3.11 or newer.
2. Open a terminal in `d:\Python\Py\App_test`.
3. Run:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 2. Install Appium

- Install Node.js from https://nodejs.org.
- Install Appium globally:

```powershell
npm install -g appium
```

- Verify installation:

```powershell
appium --version
```

### 3. Configure Android Studio

1. Install Android Studio.
2. Open SDK Manager and install Android SDK Platform, Platform Tools, and SDK Tools.
3. Open AVD Manager and create an Android emulator matching `DEVICE_NAME` and `PLATFORM_VERSION`.
4. Make sure `adb` is in your PATH.

### 4. Start Emulator

```powershell
aadb devices
```

If no emulator is listed, run Android Studio AVD Manager or:

```powershell
emulator -avd <AVD_NAME>
```

### 5. Connect a Real Device

1. Enable Developer Options and USB debugging on the Android device.
2. Connect via USB.
3. Verify with:

```powershell
adb devices
```

### 6. Start Appium Server

```powershell
appium
```

By default Appium listens at `http://127.0.0.1:4723/wd/hub`.

### 7. Run Tests

```powershell
pytest
```

To run a single test file:

```powershell
pytest tests/test_login.py
```

### 8. HTML Reports

After test execution, open `reports/report.html` in a browser.

## CI/CD Integration

### Jenkins

Create a `Jenkinsfile` in the project root and configure a Jenkins pipeline job. Example pipeline steps:

- Checkout repository
- Install Python dependencies
- Start Appium server or connect to a running instance
- Run `pytest`
- Archive `reports/report.html` and `screenshots/`

### GitHub Actions

Add a workflow file in `.github/workflows/appium-android.yml` to run tests on push or pull requests.

## Notes for Beginners

- Update `config/config.py` values for your app package and activity.
- Use the actual accessibility ids or resource IDs from your app inside page objects.
- `testdata/test_data.json` holds data for data-driven tests.
- Add new page object methods when app screens change.
