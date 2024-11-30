### README

---

# KuCoin Valid Email Checker Bot

## Overview

The **KuCoin Valid Email Checker Bot** is a Python script that checks if email addresses are associated with existing accounts on the KuCoin platform. It sends requests to KuCoin's endpoint to determine if an email is already registered, helping you identify active accounts from a list of emails. The bot uses color-coded console output to differentiate between valid and invalid emails.

### Features

- **Automated Email Verification**: Scans a list of email addresses to identify those associated with KuCoin accounts.
- **Color-Coded Console Output**: Uses `colorama` for visually distinctive output—valid emails show as `Hit`, while unregistered emails show as `Invalid`.
- **Thread Mode**: Placeholder to support threading in future enhancements.
- **Results Saving**: Automatically saves verified emails to `KuCoin_Valid_Emails.txt` for easy reference.
- **Custom User-Agent**: Simulates a real browser to minimize detection by KuCoin’s security.

### Requirements

- **Python 3.x**
- **Libraries**:
  - `requests`: For making HTTP requests.
  - `colorama`: For adding color to console output.

Install the libraries with:

```bash
pip install requests colorama
```

### Usage

1. **Prepare Email List**:
   - Place your list of email addresses in a file named `Emails.txt`, within a `Files` directory in the same location as the script.

2. **Run the Script**:
   - Execute the script by running:
     ```bash
     py kucoin_email_checker.py
     ```

3. **Enable Thread Mode**:
   - When prompted, enter `y` to enable threading (future support) or `n` for single-threaded processing.

4. **Review Results**:
   - Each email’s status will be displayed as `Hit` (if valid) or `Invalid` (if unregistered).
   - The total number of valid emails will be summarized at the end.

5. **Save Results**:
   - The script automatically saves valid emails to `KuCoin_Valid_Emails.txt` for easy reference.

### Example Output

```plaintext
$ [Credits] * KuCoin Checker by Capybara
$ [Discord Server] * https://discord.gg/YourDiscordLink
$ [Mode (v.1)] * KuCoin Account Email Checker

% [Enable Threads (y/n)] ..> y

$ [Scanning] * 100 Emails

$ [Hit] * example1@example.com
$ [Invalid] * example2@example.com
...

$ [Total Hits] * 25
Results saved to KuCoin_Valid_Emails.txt
```

### Important Notes

- **Ethical Use**: This script is intended for educational and personal use only. Ensure you have permission to verify each email address.
- **Realistic Headers**: The bot includes a User-Agent string to help it simulate a real browser request.
- **File Setup**: Ensure `Emails.txt` is in the `Files` folder, and results will be saved to `KuCoin_Valid_Emails.txt`.

### Future Enhancements

- **Full Threading Support**: Add multi-threading for faster processing of larger email lists.
- **Proxy Rotation**: Implement proxy support to avoid IP restrictions.
- **Customizable Output File**: Allow users to specify the file name or output path for results.
- **Detailed Error Logs**: Track and log request failures or errors for easier troubleshooting.

---

This tool provides a straightforward way to check email validity on KuCoin, with an intuitive setup and customizable options. Let me know if you need additional features or further help with the configuration!print('oepgrjlsze')