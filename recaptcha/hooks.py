# hooks.py
app_name = "recaptcha"
app_title = "Recaptcha"
app_publisher = "Saqlain Shaikh"
app_description = "reCAPTCHA Integration for Login"
app_email = "saqlains@preciholesports.com"
app_license = "MIT"

# Override the default login method with our custom reCAPTCHA method
override_whitelisted_methods = {
    "frappe.core.doctype.user.user.login": "recaptcha.recaptcha.login_validation.login_with_recaptcha"
}

# Enable CORS for API requests during development (for local testing)
cors = ["*"]

