# 🕶️ PhantomTrace v1.3.0
**Precise Location & Device Intelligence Framework**

*Silent. Precise. Unseen.*

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

If the user clicks the link and explicitly allows location access — **the trace is real**.

---

## 🧬 Project Lineage & Maintenance Status

PhantomTrace is a **maintained and corrected fork** of the original **MapEye** project.

MapEye is currently **unmaintained and partially broken**, with multiple issues affecting:

- Execution flow  
- Data parsing  
- Dependency compatibility  
- API reliability  
- Runtime stability  

PhantomTrace was created to **restore full functionality**, improve robustness, and modernize the framework while preserving its original educational purpose.

---

## 🔧 Key Improvements Over MapEye

- ✅ Rewritten and hardened core execution logic (`main()`)
- ✅ Fixed crashes caused by empty or missing runtime files
- ✅ Improved JSON parsing and error handling
- ✅ Replaced deprecated IP geolocation APIs
- ✅ Improved permission handling and location accuracy validation
- ✅ Cleaned runtime artifacts and logging flow
- ✅ Updated banner, naming, and project structure
- ✅ Improved Termux and Linux compatibility
- ✅ Updated documentation and usage flow

 **PhantomTrace is not a simple rename** — it is a functional repair and stabilization of a broken PoC.

---

## ⚠️ Attribution

Original concept and early implementation based on **MapEye**  
Maintained, corrected, refactored, and documented by **ch3ckm8**

This project remains a **Proof of Concept (PoC)** for educational and research purposes.

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
```
🔹 Dependencies (Linux)
```bash   
   apt update
   apt install python3 python3-pip php
   pip3 install requests
```
🔹 Termux (Android)
```bash
   pkg update
   pkg install python php
   pip install requests
```
 🚀 Usage
```bash
   python3 phantomtrace.py -h
   Common Examples
 ```
 Manual tunnel
```bash  
  python3 phantomtrace.py -t manual

## Custom port
  
  python3 phantomtrace.py -t manual -p 4242

# Generate KML

  python3 phantomtrace.py -t manual -k session_location
```
Expose the local port using ngrok, cloudflared, or any tunneling service of your choice.

 🗺️ Output

Real-time terminal output

CSV logging (db/results.csv)

Optional KML file (Google Earth)

Direct Google Maps link

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
