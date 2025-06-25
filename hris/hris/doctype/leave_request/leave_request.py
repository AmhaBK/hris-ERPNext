from frappe.model.document import Document
from frappe import _
from frappe.utils import getdate
import frappe

class LeaveRequest(Document):
    def validate(self):
        if self.from_date and self.to_date:
            from_date = getdate(self.from_date)
            to_date = getdate(self.to_date)

            delta = (to_date - from_date).days + 1
            self.total_days = delta

            # Calculate total leaves taken this year
            total_taken = frappe.db.sql("""
                SELECT SUM(total_days) FROM `tabLeave Request`
                WHERE employee = %s AND leave_type = %s
                AND YEAR(from_date) = YEAR(CURDATE())
                AND name != %s
            """, (self.employee, self.leave_type, self.name))[0][0] or 0

            if total_taken + self.total_days > 30:
                remaining = 30 - total_taken
                frappe.throw(_("Leave balance exceeded. Only {} days remaining.").format(remaining))

