
DEBUG = False 


ALLOWED_HOSTS = ['your_domain.com', 'www.your_domain.com', '127.0.0.1', 'localhost'] # <--- IMPORTANT: Update this for your domain



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'csp.middleware.CSPMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
]



AUTH_USER_MODEL = 'users.CustomUser'


SECURE_SSL_REDIRECT = True 

SECURE_HSTS_SECONDS = 31536000 

SECURE_HSTS_INCLUDE_SUBDOMAINS = True 

SECURE_HSTS_PRELOAD = True 


SESSION_COOKIE_SECURE = True 

CSRF_COOKIE_SECURE = True 

X_FRAME_OPTIONS = 'DENY' 

SECURE_CONTENT_TYPE_NOSNIFF = True 
SECURE_BROWSER_XSS_FILTER = True 

SECURE_REFERRER_POLICY = 'same-origin' 

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'", "'unsafe-eval'", "https://cdn.jsdelivr.net")
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "https://fonts.googleapis.com", "https://cdn.jsdelivr.net")
CSP_IMG_SRC = ("'self'", "data:", "https://*.unsplash.com", "https://via.placeholder.com")
CSP_FONT_SRC = ("'self'", "https://fonts.gstatic.com")
CSP_CONNECT_SRC = ("'self'",)
CSP_FRAME_SRC = ("'self'",)
CSP_OBJECT_SRC = ("'none'",)
CSP_BASE_URI = ("'self'",)
CSP_FORM_ACTION = ("'self'",)
CSP_FRAME_ANCESTORS = ("'self'",)

