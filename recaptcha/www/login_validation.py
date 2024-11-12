import frappe
import requests
from frappe import _

SECRET_KEY = '6LcfmQYqAAAAANoUgs2TDjyWdodz3lWYdT6fCc7z'

@frappe.whitelist(allow_guest=True)
def login_with_recaptcha():
    """
    Custom login method with reCAPTCHA verification develop by saqlain shaikh.
    """
    data = frappe.local.form_dict
    username = data.get('usr')
    password = data.get('pwd')
    recaptcha_response = data.get('recaptcha_response')

    # Verify reCAPTCHA
    recaptcha_verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    recaptcha_payload = {
        'secret': SECRET_KEY,
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
