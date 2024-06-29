def get_smtp_server(email_address):
    smtp_servers = {
        'gmail.com': ('smtp.gmail.com', 587),
        'googlemail.com': ('smtp.gmail.com', 587),
        'protonmail.com': ('smtp.protonmail.com', 587),
        'outlook.com': ('smtp.office365.com', 587),
        'hotmail.com': ('smtp.office365.com', 587),
        'yahoo.com': ('smtp.mail.yahoo.com', 587),
    }

    domain = email_address.split('@')[-1]

    if domain in smtp_servers:
        return smtp_servers[domain]
    else:
        return 'smtp.otherprovider.com', 587
