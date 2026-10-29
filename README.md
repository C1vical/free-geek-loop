# 🔄 Free Geek Loop

> **Turn every corporate tech refresh into community access.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FUSE Blueprint 2026](https://img.shields.io/badge/Competition-FUSE%20Blueprint%202026-blue)](https://devpost.com)

---

## 📌 Executive Summary

Free Geek Toronto (FGT) relies on technology sales for ~77% of its non-grant revenue, yet faces a shrinking supply of quality incoming consumer donations due to retail trade-in programs. While FGT thrives on uniform laptop batches, it currently operates with **zero corporate partners**.

**Free Geek Loop** is a dual-sided circular platform that digitizes corporate IT Asset Disposition (ITAD). It allows Toronto SMBs to pledge future hardware refreshes, automates device compatibility pre-screening, matches incoming inventory with nonprofit demand, and generates corporate ESG impact reports.

---

## ✨ Core Features

1. **Refresh Calendar:** B2B portal allowing companies to pledge upcoming device refresh cycles (e.g., 40 laptops in Q1) to give FGT forward-looking inventory visibility.
2. **Device Fit Checker:** Automated CSV pre-screening engine that scores incoming equipment for refurbishment yield before scheduling pickup.
3. **Demand Matcher:** Direct circular matching engine linking corporate hardware pledges to submitted community nonprofit hardware requests.
4. **FGT Operations Dashboard:** Internal triage & inventory forecast portal built for FGT's lean team (1 FT, 5 PT staff).
5. **ESG Impact Generator:** Provides corporate donors with verifiable Scope 3 carbon reduction and digital access impact metrics.
6. **Scenario Calculator:** Interactive revenue & impact simulator for financial forecasting.

---

## 🛠️ Tech Stack & Open-Source Tools

- **Frontend & UI:** Streamlit / React (Tailwind CSS)
- **Data Engine:** Pandas / Python 3.11
- **Data Security:** NIST 800-88 / DoD sanitization protocol compliance logging
- **Deployment:** Vercel / Streamlit Community Cloud (Zero-cost hosting footprint)

---

## 🚀 Quickstart & Local Setup

```bash
# 1. Clone the repository
git clone [https://github.com/YOUR_USERNAME/free-geek-loop.git](https://github.com/YOUR_USERNAME/free-geek-loop.git)
cd free-geek-loop

# 2. Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run application
streamlit run src/main.py
