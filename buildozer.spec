[app]

# (str) Title of your application
title = Predicciones Futbol Pro

# (str) Package name
package.name = futbolpro

# (str) Package domain (needed for android packaging)
package.domain = org.futbol

# (str) Source file where the main.py file lives
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,html,css

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,openssl,requests,flask,jinja2,werkzeug,click,MarkupSafe,itsdangerous

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 31

# (str) Android NDK version to use
android.ndk = 25b

# (list) Area of application architecture
android.archs = arm64-v8a

# (bool) Automatically accept android SDK license
android.accept_sdk_license = True

# Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2
