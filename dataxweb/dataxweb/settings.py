"""
Django settings for dataxweb project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _
import django.utils.log
import logging
import logging.handlers

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4q@%gatxy8hi)rn6!qt6+59n(^eki-ght5*6tzqtpbvaukpemy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dataxweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend/dist'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'backend.views.global_setting',
            ],
        },
    },
]

WSGI_APPLICATION = 'dataxweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    #     'NAME': 'chf',
    #     'USER': 'root',
    #     'PASSWORD': '123456',
    #     'OPTIONS': {
    #         "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
    #     }
    # }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/dist/static'),
]


SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 60 * 30  # 30分钟
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 会话cookie可以在用户浏览器中保持有效期。True：关闭浏览器，则Cookie失效

# 自定义用户model 否则会报：HINT: Add or change a related_name argument to the definition
# for ‘User.user_permissions’ or ‘User.user_permissions’.
# AUTH_USER_MODEL = 'backend.ChfUserProfile'


APPEND_SLASH = True

SITE_NAME = _('DataXWeb')
SITE_DESC = _('DataXWeb官网')
SITE_AUTHOR = 'flack'

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads').replace('\\', '/')  # 设置静态文件路径为主目录下的uploads文件夹


# 首页配置
# SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
# 首页标题
# SIMPLEUI_HOME_TITLE = '百度一下你就知道'
# 首页图标
# SIMPLEUI_HOME_ICON = 'fa fa-user'
# 设置simpleui 点击首页图标跳转的地址
SIMPLEUI_INDEX = 'http://www.dataxweb.cn/index'
# 自定义SIMPLEUI的Logo 修改LOGO
SIMPLEUI_LOGO = STATIC_URL + 'images/login_logo.jpg'

# 服务器信息
SIMPLEUI_HOME_INFO = False
# 快速操作
SIMPLEUI_HOME_QUICK = True
# 最近动作
SIMPLEUI_HOME_ACTION = True
# 统计分析信息
SIMPLEUI_ANALYSIS = False

# 默认图标
# SIMPLEUI_DEFAULT_ICON = True
# SIMPLEUI_ICON = {
#     '系统': 'fab fa-apple',
#     '信息管理': 'fas fa-user-tie'
# }

SIMPLEUI_CONFIG = {
    'system_keep': False,
    # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'menu_display': [
        _('系统'),
        _('信息管理'),
        _('产品管理'),
        _('简介管理'),
        _('留言管理'),
        _('招聘管理'),
        _('管理员管理'),
        # _('中英文版管理'),
        # _('权限认证')
    ],
    'menus': [
        {
            'name': _('系统'),
            'icon': 'fas fa-cog',
            'models': [
                {
                    'name': _('导航菜单'),
                    'icon': 'fa fa-book-open',
                    # 'url': 'home/sysnav/'
                },
                {
                    'name': _('网站配置'),
                    'icon': 'fa fa-book-open',
                    # 'url': 'home/sysconfig/'
                },
                {
                    'name': _('问题列表'),
                    'icon': 'fa fa-book-open',
                    # 'url': 'home/chfquestion/'
                },
                {
                    'name': _('清除系统缓存'),
                    'icon': 'fa fa-broom',
                },
                {
                    'name': _('系统日志'),
                    'icon': 'fa fa-cat',
                    'url': 'logentry/',
                },
                {
                    'name': _('数据库备份'),
                    'icon': 'fa fa-coins',
                },
                {
                    'name': _('关键词管理'),
                    'icon': 'fa fa-book-open',
                }
            ]
        },
        # {
        #     'name': _('信息管理'),
        #     'icon': 'fas fa-sitemap',
        #     'models': [
        #         {
        #             'name': _('首页模块'),
        #             'icon': 'fa fa-info',
        #             'url': 'home/chfindexplate/'
        #         },
        #         {
        #             'name': _('Banner图'),
        #             'icon': 'fa fa-book-open',
        #             'url': 'home/chfbanner/'
        #         },
        #         {
        #             'name': _('用户浇水记录'),
        #             'icon': 'fa fa-tint',
        #             'url': 'home/chfuserwateringrecord/'
        #         },
        #         {
        #             'name': _('用户抢券记录'),
        #             'icon': 'fa fa-certificate',
        #             'url': 'home/chfapplyrecord/'
        #         },
        #         {
        #             'name': _('浇水水量余额'),
        #             'icon': 'fa fa-water',
        #             'url': 'home/chfwateringqty/'
        #         },
        #         {
        #             'name': _('新闻资讯'),
        #             'icon': 'fa fa-newspaper',
        #             'url': 'home/chfnews/'
        #         },
        #         # {
        #         #     'name': _('合作伙伴'),
        #         #     'icon': 'fa fa-glass-cheers',
        #         #     'url': 'home/chfpartner/'
        #         # },
        #         {
        #             'name': _('合作共赢'),
        #             'icon': 'fa fa-glass-cheers',
        #             'url': 'home/chfcooperation/'
        #         },
        #         {
        #             'name': _('申请表管理'),
        #             'icon': 'fa fa-allergies',
        #             'url': 'home/chftabletemplate/'
        #         }
        #     ]
        # },
        # {
        #     'name': _('产品管理'),
        #     'icon': 'fas fa-pepper-hot',
        #     'models': [
        #         {
        #             'name': _('产品列表'),
        #             'icon': 'fa fa-project-diagram',
        #             'url': 'home/chfproduct/'
        #         },
        #         {
        #             'name': _('产品类型'),
        #             'icon': 'fa fa-tape',
        #             'url': 'home/chfproducttype/'
        #         }
        #     ]
        # },
        # {
        #     'name': _('简介管理'),
        #     'icon': 'fas fa-pencil-alt',
        #     'models': [
        #         {
        #             'name': _('品牌介绍'),
        #             'icon': 'fa fa-beer',
        #             'url': 'home/chfabout/'
        #         },
        #         {
        #             'name': _('品牌图片资源'),
        #             'icon': 'fa fa-images',
        #             'url': 'home/chfaboutresource/'
        #         },
        #         {
        #             'name': _('发展历程'),
        #             'icon': 'fa fa-dharmachakra',
        #             'url': 'home/chfcompanyhistory/'
        #         },
        #         {
        #             'name': _('秦始皇故事'),
        #             'icon': 'fa fa-dharmachakra',
        #             'url': 'home/chfstory/'
        #         }
        #     ]
        # },
        # {
        #     'name': _('留言管理'),
        #     'icon': 'fas fa-comments',
        #     'models': [
        #         {
        #             'name': _('留言列表'),
        #             'icon': 'fa fa-comment-dots',
        #             'url': ''
        #         }
        #     ]
        # },
        # {
        #     'name': _('招聘管理'),
        #     'icon': 'fas fa-users',
        #     'models': [
        #         {
        #             'name': _('招聘列表'),
        #             'icon': 'fa fa-user-friends',
        #             'url': 'home/chfjobrecruit/'
        #         }
        #     ]
        # },
        # {
        #     'name': _('管理员管理'),
        #     'icon': 'fas fa-users-cog',
        #     'models': [
        #         {
        #             'name': _('用户'),
        #             'icon': 'fas fa-user',
        #             'url': 'home/chfuserprofile/'
        #         },
        #         {
        #             'app': 'auth',
        #             'name': _('用户组'),
        #             'icon': 'fa fa-user-tag',
        #             'url': 'auth/group/'
        #         }
        #     ]
        # },
        # {
        #     'name': '中英文版管理',
        #     'icon': 'fas fa-compact-disc',
        #     'models': []
        # },
        # {
        #     'app': 'auth',
        #     'name': '权限认证',
        #     'icon': 'fas fa-user-shield',
        #     'models': [{
        #         'name': '用户',
        #         'icon': 'fa fa-user',
        #         'url': 'home/chfuserprofile/'
        #     }]
        # }
    ]
}


LOG_PATH = os.path.join(BASE_DIR, 'log')
if not os.path.join(LOG_PATH):
    os.mkdir(LOG_PATH)

# 日志系统的记录器，处理器，过滤器和格式器
LOGGING = {
    # 指明dictConfig的版本
    'version': 1,
    # 设置True将禁用所有的已经存在的日志配置
    'disable_existing_loggers': False,
    # 格式器
    'formatters': {
        'standard': {
            'fotmat': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] '
                      '[%(levelname)s]- %(message)s'  # 日志格式
        },
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {asctime} {message}',
            'style': '{',
        },
    },
    # 过滤器
    'filters': {
        # 'special': {
        #     '()': 'home.logging.SpecialFilter',
        #     'foo': 'bar',
        # },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    # 处理器 定义了4个处理器
    'handlers': {
        # 'default': {
        #     'level': 'DEBUG',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': 'log/all.log',                # 日志输出文件
        #     'maxBytes': 1024*1024*5,                  # 文件大小
        #     'backupCount': 2,                         # 备份份数
        #     'formatter': 'standard',                  # 使用哪种formatters日志格式
        # },
        # 'error': {
        #     'level': 'ERROR',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': 'log/error.log',
        #     'maxBytes': 1024*1024*5,
        #     'backupCount': 2,
        #     'formatter': 'standard',
        # },
        # # 文件处理器，所有高于（包括）而error的消息会被发送给站点管理员，使用的是special格式器
        # 'file_handler': {
        #     'level': 'NOTSET',
        #     # 'class': 'logging.FileHandler',
        #     'class': 'logging.handlers.TimedRotatingFileHandler',
        #     'when': 'W0',  # 日志文件每周第一天翻转
        #     'filename': 'log/error.log',  # 日志文件的存储地址
        #     'formatter': 'verbose',
        #     'backupCount': 500,  # 最多可以保存500个文件
        #     # 'filters': ['require_debug_true'],
        # },
        # 邮件处理器，所有高于（包括）而error的消息会被发送给站点管理员，使用的是special格式器
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
        },
        # 流处理器，所有的高于（包括）debug的消息会被传到stderr，使用的是simple格式器
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            # 'filters': ['require_debug_true'],
        },
        # Null处理器，所有高于（包括）debug的消息会被传到/dev/null
        # 'null': {
        #     'level': 'DEBUG',
        #     # 'class': 'logging.NullHandler',
        #     'class': 'django.utils.log.NullHandler',
        # },
        # 'request_handler': {
        #     'level': 'DEBUG',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': '/sourceDns/log/script.log',
        #     'maxBytes': 1024*1024*5,
        #     'backupCount': 5,
        #     'formatter': 'standard',
        # },
        # 'scripts_handler': {
        #     'level': 'DEBUG',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': '/sourceDns/log/script.log',
        #     'maxBytes': 1024*1024*5,
        #     'backupCount': 5,
        #     'formatter': 'standard',
        # }
    },
    # 定义了三个记录器
    'loggers': {
        # 所有高于（包括）error的消息会被发往mail_admins处理器，消息不向父层次发送
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # 所有高于（包括）info的消息同时会被发往console和mail_admins处理器，使用special过滤器
        # 'my.custom': {
        #     'handlers': ['console', 'mail_admins'],
        #     'level': 'INFO',
        #     'filters': ['special'],
        # }
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    },
}

