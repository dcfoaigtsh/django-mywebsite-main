"""
Django settings for mywebsite project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ododn+p3v06x981i+(l*j2-tt&qs@k@#!-byks8a@@y50@$jy2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app001',
    'students',
    'cookiessessions',
    'flower',
    'news',
    'captcha',
    
    # django-allauth相關，第三方認證登入
    # 需要先安裝 pip install django-allauth   pip install pyjwt
    # 1. 需要執行資料庫遷移以支援 django-allauth
    # 2. 訪問 Google Cloud Console (https://console.cloud.google.com/)
    # 3. 創建新項目
    # 4. 啟用 Google+ API 或 Google OAuth2 API
    # 5. 配置 OAuth 同意螢幕 (OAuth consent screen)
    # 6. 創建 OAuth 客戶端 ID
    # 7. 應用類型: Web 應用程式
    # 8. 名稱: MyWebSite
    # 9. 授權的重定向 URI: http://127.0.0.1:8000/accounts/google/login/callback/
    # 10. 獲取客戶端 ID 和密鑰後，需要將這些設定到 Django admin 介面：
    # 1. admin 頁面 (http://127.0.0.1:8000/admin/)
    # 2. 登入管理員帳號
    # 3. 在 "Sites" 下，修改 example.com 為您的網站地址或 localhost
    # 4. 在 "Social applications" 下，添加新的社交應用：
    # 5. 提供者: Google
    # 6. 名稱: Google
    # 7. 客戶端 ID: (您的 Google 客戶端 ID)
    # 8. 密鑰: (您的 Google 客戶端密鑰)
    # 9. 密鑰: (留空)
    # 10. 選擇站點: 添加您剛才修改的站點
    # 完成配置後，您的系統將支援 Google 登入。使用者可以透過 Google 帳號登入，並且登入後將能夠訪問受保護的功能和頁面。
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 在 MIDDLEWARE 設定中添加 AccountMiddleware
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'mywebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # .html
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mywebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# 語系，default: en-us
LANGUAGE_CODE = 'zh-hant'
# 時區
TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# 媒體文件
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ======================================================================
# django-allauth設定
AUTHENTICATION_BACKENDS = [
    # Django內建後端
    'django.contrib.auth.backends.ModelBackend',
    # allauth特定的認證方法，例如電子郵件
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# allauth設定
ACCOUNT_EMAIL_VERIFICATION = 'none'  # 暫時不驗證電子郵件
ACCOUNT_LOGIN_METHODS = {'username', 'email'}  # 新格式：允許使用用戶名或電子郵件登入
ACCOUNT_SIGNUP_FIELDS = ['email', 'username*', 'password1*', 'password2*']  # 新格式：*表示必填欄位
ACCOUNT_UNIQUE_EMAIL = True  # 電子郵件必須唯一
ACCOUNT_USERNAME_MIN_LENGTH = 3  # 用戶名最小長度

# Provider特定設定
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'FIELDS': [
            'email',
            'name',
            'first_name',
            'last_name',
            'picture'
        ],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
    },
    'github': {
        'SCOPE': ['user', 'repo', 'read:org'],
    },
}


# 登入後跳轉
LOGIN_REDIRECT_URL = '/cookiessessions/login/'
LOGOUT_REDIRECT_URL = '/cookiessessions/login/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/cookiessessions/login/'

# ======================================================================
