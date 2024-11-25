import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_recaptcha_sitekey():
    """
    API endpoint to fetch the reCAPTCHA site key
    """
    site_key = frappe.db.get_single_value('Recaptcha Settings', 'site_key')
    if not site_key:
        frappe.throw(_("Recaptcha site key not configured."))
    return {"site_key": site_key}
