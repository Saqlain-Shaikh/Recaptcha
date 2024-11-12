import frappe
import requests
from frappe import _

@frappe.whitelist(allow_guest=True)
def login_with_recaptcha():
    """
    Custom login method with reCAPTCHA verification.
    """
    data = frappe.local.form_dict
    username = data.get('usr')
    password = data.get('pwd')
    recaptcha_response = data.get('recaptcha_response')

    # Fetch secret key from Recaptcha Settings
    secret_key = frappe.db.get_single_value('Recaptcha Settings', 'secret_key')

    # Verify reCAPTCHA
    recaptcha_verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    recaptcha_payload = {
        'secret': secret_key,
        'response': recaptcha_response
    }
    recaptcha_result = requests.post(recaptcha_verify_url, data=recaptcha_payload).json()

    if not recaptcha_result.get('success'):
        frappe.local.response["http_status_code"] = 400
        frappe.local.response["message"] = _('reCAPTCHA verification failed')
        return

    # Proceed with ERPNext authentication logic
    try:
        frappe.auth.login_as(username)
        frappe.local.response["message"] = _('Logged In')
    except frappe.exceptions.AuthenticationError:
        frappe.local.response["http_status_code"] = 401
        frappe.local.response["message"] = _('Invalid login credentials')
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Login Error"))
        frappe.local.response["http_status_code"] = 500
        frappe.local.response["message"] = _('Login failed. Please try again.')
