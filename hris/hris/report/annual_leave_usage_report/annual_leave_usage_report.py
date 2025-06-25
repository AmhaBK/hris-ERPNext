import frappe
from frappe.utils import nowdate

def execute(filters=None):
    filters = filters or {}
    year = filters.get("year") or frappe.utils.nowdate().split("-")[0]
    employee_filter = filters.get("employee")

    conditions = f"YEAR(from_date) = '{year}'"
    if employee_filter:
        conditions += f" AND employee = '{employee_filter}'"

    results = frappe.db.sql(f"""
        SELECT 
            employee,
            SUM(total_days) as used_days
        FROM `tabLeave Request`
        WHERE docstatus = 1 AND {conditions}
        GROUP BY employee
    """, as_dict=True)

    data = []
    for row in results:
        remaining = 30 - (row.used_days or 0)
        data.append({
            "employee": row.employee,
            "used_days": row.used_days,
            "remaining": remaining
        })

    columns = [
        {"label": "Employee", "fieldname": "employee", "fieldtype": "Link", "options": "Employee", "width": 150},
        {"label": "Total Leave Days Used", "fieldname": "used_days", "fieldtype": "Float", "width": 180},
        {"label": "Remaining Balance", "fieldname": "remaining", "fieldtype": "Float", "width": 180}
    ]

    return columns, data

