# Free Geek Loop

**Turn every corporate tech refresh into community access.**

Free Geek Loop helps Free Geek Toronto (FGT) turn local organizations' laptop refreshes (schools, firms, clinics) into a predictable supply of high-value devices to refurbish and sell. Built for the FUSE Blueprint 2026 case competition.

- **Live web app:** https://c1vical.github.io/free-geek-loop/
- **Video:** [YOUTUBE UNLISTED LINK]

## The problem

About 77% of FGT's roughly $240K yearly revenue comes from sales, mostly refurbished tech. But trade-in programs pull the best laptops away from donation, and FGT has no corporate partners, so it rarely gets the large batches of uniform business laptops it can refurbish fastest. FGT doesn't have a demand problem first. It has a predictable supply problem.

## The solution

A web app that turns a business's next device refresh into a planned pickup for FGT:

1. **Plan:** the business logs its next refresh date.
2. **Pledge:** devices are scored for reuse before pickup.
3. **Collect:** FGT's existing business pickup service brings them in.
4. **Refurbish:** data wiped, tested and repaired as one uniform batch.
5. **Match:** laptops are matched to nonprofit requests.
6. **Report:** the business gets a shareable impact report, which brings it back for the next refresh.

## What's in the app

| Tab | What it does |
|---|---|
| **Partner portal** | An organization picks or registers its account, uploads its device list (CSV) or enters it by hand, sees a live reuse fit check, creates a pledge and books a pickup. Below that, nonprofits waiting for laptops are listed and new requests can be logged and matched instantly. |
| **FGT dashboard** | Staff see KPIs, a 12-month supply forecast and every pledge's status, advanced step by step to Deployed. |
| **Impact report** | Devices reused and recycled, e-waste diverted, estimated CO₂ avoided and which organizations received the laptops. Projected until devices are deployed, then verified. Includes a ready-to-post LinkedIn update. |

## Run it

The app is one HTML file with no framework, build step or server. Open `index.html` in a browser, or use the live link above.

Data is saved in your browser. Use **Reset demo data** in the footer (click twice) to start over. A sample device list is in `data/stl_laptop_refresh.csv`; the **Load sample list** button loads the same list.

## How it works

- **Reuse fit score (0 to 100):** device type (laptop 45, desktop 25, monitor 20, printer -25) + age (4 years or less +35, 6 or less +22, 8 or less +8, older -15) + condition (working +20, minor wear +8, not working -20). 70+ is High reuse, 40 to 69 Medium, under 40 Recycle.
- **Batch uniformity:** share of a pledge that is one model. 75%+ is a uniform batch, which FGT can refurbish in bulk.
- **Demand Match:** laptops are ready 21 days after pickup; nonprofit requests are filled in need-by order from batches ready in time.

Example: the St. Theresa of Lisieux CHS sample has 42 devices: 36 high reuse, 4 medium, 2 recycle, and 86% one model (a uniform batch).

All figures are illustrative estimates. Sample companies and organizations are demo data.

## Team

[Name 1], [Name 2], [Name 3], [Name 4]
