frappe.ui.form.on('Leave Request', {
    from_date: calculate_days,
    to_date: calculate_days,

    total_days(frm) {
        if (frm.doc.total_days > 15) {
            frappe.msgprint(__('Leave exceeds 15 days. Please confirm with HR.'));
        }
    }
});

function calculate_days(frm) {
    if (frm.doc.from_date && frm.doc.to_date) {
        const from = frappe.datetime.str_to_obj(frm.doc.from_date);
        const to = frappe.datetime.str_to_obj(frm.doc.to_date);
        const diff = frappe.datetime.get_diff(to, from) + 1;
        frm.set_value('total_days', diff);
    }
}

