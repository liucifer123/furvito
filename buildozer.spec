[app]

# (str) Title of your application
title = Predicciones Futbol Pro

# (str) Package name
package.name = futbolpro

# (str) Package domain (needed for android packaging)
package.domain = org.futbol

# (str) Source file where the main.py file lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,html,css

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,openssl,requests,flask,jinja2,werkzeug,click,MarkupSafe,itsdangerous

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 31

# (str) Android NDK version to use
android.ndk = 25b

# (list) Area of application architecture
android.archs = arm64-v8a

# (bool) Automatically accept android SDK license
android.accept_sdk_license = True

# Log level
log_level = 2
