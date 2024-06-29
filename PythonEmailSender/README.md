
### Files Description

- **`main.py`**: Coordinates the process of reading recipient emails from `recipients.xlsx`, fetching SMTP server details, and sending emails using `send_email.py`.
  
- **`send_email.py`**: Contains the function to send emails using the `smtplib` library.

- **`get_smtp_server.py`**: Provides the function to determine the SMTP server and port based on the recipient's email domain.

- **`email_content.py`**: Includes the function to prompt the user for email subject and body content.

- **`recipients.xlsx`**: Excel file containing a list of recipient email addresses under the 'Email' column.

## Usage

1. **Setup Environment:**

   - Ensure Python 3.x is installed on your system.
   - Install required libraries using `pip install pandas`.

2. **Configuration:**

   - Update `email_sender` and `email_password` variables in `main.py` with your email credentials.
   - Modify `recipients.xlsx` to include the desired recipient email addresses.

3. **Run the Script:**

   Navigate to the project directory and execute `main.py`:

   ```bash
   python main.py
