# Selenium Demo: Ryde
This project demonstrates how to use Selenium WebDriver with Python to automate the process of logging into a web dashboard, navigating to a location creation page, and drawing a polygon on a map by simulating mouse clicks at random points.

## Features

- Automated login to the RydeApp admin dashboard
- Navigation to the "Add Location" page
- Automated interaction with a Leaflet map to draw a polygon using random points
- Uses Chrome WebDriver

## Prerequisites

- Python 3.x
- Google Chrome browser
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (make sure the version matches your Chrome browser)
- Required Python packages:
  - selenium

## Installation

1. **Clone this repository** or copy the files to your local machine.

2. **Install dependencies:**
   ```sh
   pip install selenium
   ```

3. **Download ChromeDriver** and place it in the specified path (default: `C:\chrome-driver\chromedriver.exe`). Update the path in `demo.py` if needed.

## Usage

1. Edit `demo.py` to update login credentials if necessary.

2. Run the script:
   ```sh
   python demo.py
   ```

3. The script will:
   - Open Chrome
   - Log in to the dashboard
   - Navigate to the location creation page
   - Click the "Draw Polygons" button
   - Simulate four random clicks on the map to draw a polygon

## File Structure

- `demo.py` - Main automation script
- `chromedriver.exe` - ChromeDriver binary (not included; download separately)
- `selenium-java/` - Java Selenium libraries (not used by the Python script)

## Notes

- The script uses `time.sleep()` for simplicity. For production use, consider replacing these with Selenium's `WebDriverWait` for more reliable waits.
- Make sure the ChromeDriver version matches your installed Chrome browser version.
- The script is tailored for the RydeApp admin dashboard and may require adjustments for other sites.

## License

See [selenium-java/LICENSE](selenium-java/LICENSE) for license information.

## Acknowledgements

- [Selenium WebDriver](https://www.selenium.dev/)
- [RydeApp Dashboard](http://dashboard.rydeapp.net/admin/login)
