# 🕶️ PhantomTrace v1.3.0

<p align="center">
  <img src="https://forthebadge.com/images/badges/built-with-love.svg">
</p>

<p align="center">
  <b>PhantomTrace</b><br>
  Precise Location & Device Intelligence Framework
</p>

<p align="center">
  <i>Silent. Precise. Unseen.</i>
</p>

---

## ⚠️ DISCLAIMER

PhantomTrace is a **Proof of Concept (PoC)**.

This project is intended strictly for **educational, research, and security awareness purposes**.  
Any unauthorized use against individuals or systems without **explicit consent** is illegal.

The author assumes **no responsibility** for misuse.

---

## 🧠 What is PhantomTrace?

PhantomTrace is a lightweight location intelligence framework that demonstrates how modern browsers and devices can expose precise GPS and device metadata when permissions are granted — often without users fully understanding the implications.

Unlike traditional IP-based geolocation tools, PhantomTrace leverages **HTML5 Geolocation APIs** to extract **real GPS coordinates directly from the device**.

If the user clicks the link and explicitly allows location access — the trace is real.

---

## 🎯 Data Collected (When Permissions Are Granted)

### 📍 Location Intelligence
- Latitude
- Longitude
- Accuracy (meters)
- Altitude (if supported)
- Direction (only if the device is moving)
- Speed (only if the device is moving)

Accuracy can reach **~10–30 meters** on mobile devices with high-accuracy GPS enabled.

---

### 🧬 Device Fingerprinting (No Extra Permissions Required)
- Operating System
- Platform / Architecture
- CPU Cores (approximate)
- RAM (approximate)
- Screen Resolution
- GPU Vendor & Renderer
- Browser Name & Version
- Public IP Address

Automatic IP-based enrichment is performed after data capture.

---

## 🧪 Why PhantomTrace Is Different

| Feature | IP Geolocation | PhantomTrace |
|------|---------------|-------------|
| Accuracy | ISP-based (km-level) | GPS-level (meters) |
| Requires User Permission | ❌ | ✅ |
| Mobile Optimized | ❌ | ✅ |
| Real Coordinates | ❌ | ✅ |
| Browser-Based | ❌ | ✅ |

PhantomTrace exposes the **security risks of blind permission approval**.

---

## 🧩 Templates Available

- NearYou  
- Google Drive  
- WhatsApp  
- Telegram  

Each template mimics realistic interfaces to demonstrate permission-based tracking scenarios.

---

## 🧪 Tested On

- Kali Linux
- Parrot OS
- BlackArch
- Ubuntu
- Kali NetHunter
- Termux (Android)

---

## ⚙️ Installation

### 🔹 Basic (Manual Tunnel)

```bash
git clone https://github.com/ch3ckm8/PhantomTrace-v1.3.0.git
cd PhantomTrace-v1.3.0
python3 phantomtrace.py -t manual -k session_location
🔹 Dependencies
bash
Copiar código
apt update
apt install python3 python3-pip php
pip3 install requests
🔹 Termux
bash
Copiar código
pkg update
pkg install python php
pip install requests
🚀 Usage
bash
Copiar código
python3 phantomtrace.py -h
Common Examples
bash
Copiar código
# Manual tunnel mode
python3 phantomtrace.py -t manual

# Custom port
python3 phantomtrace.py -t manual -p 4242

# Generate KML for Google Earth
python3 phantomtrace.py -t manual -k session_location
Expose the port using ngrok, cloudflared, or any tunnel of your choice.

🗺️ Output
Real-time terminal output

CSV logging (db/results.csv)

Optional KML file (Google Earth)

Google Maps direct link

🧷 Operational Notes
Accuracy depends on:

GPS hardware

Browser implementation

User permissions

Location mode (High Accuracy recommended)

Desktop systems may fallback to network-based approximation.

🧠 Philosophy
“The most dangerous exploits are not zero-days —
they are permissions given willingly.”

👤 Author
ch3ckm8
Independent Researcher / Offensive Security

Silent execution. Clean traces.

🕶️ Final Note
If you’re reading this —
remember: the browser is already a sensor.

Stay sharp.
