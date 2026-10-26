# Warranty Tracker

Open `warranty-tracker.html` in a browser (Edge/Chrome). No install needed.

1. **System export (.xlsx)**: the warranty claims export (STORE, CLAIMCODE, CLAIMSTATUS, REJECTREASON, CLAIMAMOUNT …).
2. **Local cancel log (.xlsx)**: the depots' *Warranty Cancel Log* workbook, one tab per depot with
   Date · Warranty Claim Number · Reason for Cancelling · Cancelled By Head of Stores.

Local reasons are matched to the export on claim number and replace the system reject reason.

## Buckets
- **Cancelled**: Stores cancelled, Warranty Cancelled (includes Engineer Cancelled)
- **Processed**: Successful Claim / Completed, Warranty Approved, Stores approved A/B
- **Supplier Rejected**: shown on its own
- **Open**: Awaiting Collection, Uplifted by Supplier, Unfinished
- **Lost value**: total CLAIMAMOUNT of cancelled claims

## Depot names
Tabs show store codes until you add names to `STORE_NAMES` near the top of the script,
for example `'2261': 'Hunslet',`.
