# 📝 Data Entry Automation

A Python script that scrapes property data from a website and automatically fills a Google Form using Selenium and BeautifulSoup. Demonstrates practical web automation and scraping skills.

---

## ✨ Features

- Scrapes property addresses, prices, and links from a website using **BeautifulSoup**
- Automatically fills a Google Form using **Selenium**
- Saves responses in Google Sheets via form submission
- Optional **.env support** to configure URLs

---

## 📸 Screenshot

Site- – Zillow Clone

<img width="1470" height="956" alt="site" src="https://github.com/user-attachments/assets/5bde40d7-c259-41ed-8f38-2264eb0bec22" /><br>

Google Form- Input fields filled automatically

<img width="1419" height="909" alt="form" src="https://github.com/user-attachments/assets/3bffd253-b348-4573-a299-09a53ac2fdaa" /><br>

<img width="1429" height="903" alt="form1" src="https://github.com/user-attachments/assets/23310c9f-b20e-4a05-a32d-984cf632a23d" /> <br>

Google Sheet – Responses saved automatically

<img width="1113" height="824" alt="google sheet" src="https://github.com/user-attachments/assets/e49b42ab-1417-4d4c-86eb-7184e03d35f1" /><br>


---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/bhavikakeswani/data-entry-automation.git
cd data-entry-automation
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a .env file in the project root:
```bash
SITE_URL=<your SITE_URL>
GOOGLE_FORM_URL=<your GOOGLE_FORM_URL>
```
4.  Run the script:
```bash
python main.py
```
- The script scrapes property data from the specified website.
- Automatically fills the Google Form and submits each response.

---

## 📦 Requirements
- Python 3.x
- See [requirements.txt](requirements.txt). 

---

## 🚀 Future Enhancements
- Save a local backup CSV of scraped data
- Add logging for successful and failed submissions
- Add notifications (e.g., email) after each run

---

### License 
This project is licensed under the [MIT License](LICENSE). 

---
