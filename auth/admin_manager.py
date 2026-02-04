
import os
import csv
from datetime import datetime

# SOLE PROPRIETOR / ADMIN CONFIGURATION
ADMIN_ID = "SOLE_PROPRIETOR"
ADMIN_EMAIL = "Rutterchristopher@gmail.com"
APP_OWNER_ROLE = "ADMIN"

class AdminLedger:
    """
    Manages the master list of users/visitors for the Sole Proprietor.
    Access Level: RESTRICTED (Admin Only)
    """
    def __init__(self, ledger_file="secure_user_ledger.csv"):
        self.ledger_file = ledger_file
        self.admin_contact = ADMIN_EMAIL
        self._ensure_ledger_exists()

    def _ensure_ledger_exists(self):
        """Creates the secure ledger if it doesn't exist."""
        if not os.path.exists(self.ledger_file):
            with open(self.ledger_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "User Email", "Status", "Role"])
            print(f"Admin Ledger initialized: {self.ledger_file}")

    def register_user(self, email):
        """
        Registers a new user into the system.
        Triggers: Notification to Admin.
        """
        entry_time = datetime.now().isoformat()
        with open(self.ledger_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([entry_time, email, "PENDING_VERIFICATION", "USER"])
        
        self._notify_admin(email)
        return True

    def _notify_admin(self, user_email):
        """
        Internal protocol to queue this user for the Admin's weekly export.
        """
        print(f"LOG: New user {user_email} captured. Ready for export to {self.admin_contact}.")

    def generate_admin_export(self):
        """
        Generates the downloadable file for the Sole Proprietor.
        """
        return {
            "recipient": self.admin_contact,
            "file": self.ledger_file,
            "status": "READY_FOR_DOWNLOAD"
        }

if __name__ == "__main__":
    # System Check
    admin = AdminLedger()
    print(f"System initialized for {APP_OWNER_ROLE}: {ADMIN_EMAIL}")
