# How to Use
- Step 1: Open Instagram to Export Your Data
    - Accounts Center -> Your Information and Permissions -> Export Your Information -> Select JSON in format
- Step 2: Clone this Repository
- Step 3: Extract all files from the downloadable zip Folder from Instagram into `data/`
- Step 4: Run `python <path to file>/instagram.py`

# Current Functionality
- Finds Unfollowers (People who do not follow you back)

# Notes:
- Unfollowers will also display deactivated accounts from people who actually follow you when active, so manually remove them from the `following.json` file