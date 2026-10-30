# Warranty Tracker

Open `warranty-tracker.html` in a browser (Edge/Chrome). No install needed.

It opens on the **Dashboard**, which ranks every ticked depot. Use the *Rank depots by* buttons
to rank by lost £, cancel rate, cancelled, not started, supplier rejected or missing FBF reason.

1. **System export (.xlsx)**: the warranty claims export (STORE, CLAIMCODE, CLAIMSTATUS, REJECTREASON, CLAIMAMOUNT …).
2. **Local cancel log (.xlsx)**: the depots' *Warranty Cancel Log* workbook, one tab per depot with
   Date · Warranty Claim Number · Reason for Cancelling · Cancelled By Head of Stores.

Local reasons are matched to the export on claim number and replace the system reject reason.

## Buckets
- **Cancelled**: Stores cancelled, Warranty Cancelled (includes Engineer Cancelled)
- **Processed**: Successful Claim / Completed, Warranty Approved, Uplifted by Supplier
- **Supplier Rejected**: shown on its own
- **Open / In Progress**: Awaiting Collection, Stores approved A/B
- **Not Started**: Unfinished
- **Lost value**: total CLAIMAMOUNT of cancelled claims

## Depot names
Store codes are mapped to depot names in `STORE_NAMES` near the top of the script,
for example `'2261': 'Hunslet Park',`. Unmapped codes show as `Store 1234`.

## Show / hide depots
Untick a depot in the sidebar to hide it. Hidden depots are left out of the All Depots
totals, the depot comparison and the Unfinished PDF. **Show all / Hide all** switch every
depot at once. Your selection is remembered in this browser.

## Unfinished report (PDF)
The **Unfinished report (PDF)** button downloads a summary page plus one page per depot
listing every claim at *Unfinished*, oldest first. On **All Depots** it covers every depot;
on a depot tab it covers just that depot. The fail date filter applies.

## Shareable copy
A copy is published as a claude.ai artifact. To rebuild it after changes:
`python3 tools/build_artifact.py /path/to/out.html`, then republish that file.
No claim data is stored in the page; everyone uploads their own exports.
