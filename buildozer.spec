[app]

# (str) Title of your application
title = FF NetCutter

# (str) Package name
package.name = ffnetcutter

# (str) Package domain (needed for android packaging)
package.domain = org.netcutter

# (str) Source files where the include (let it be empty to include all files)
source.dir = .

# (list) Source files to include (let it be empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,CHANGE_NETWORK_STATE,SYSTEM_ALERT_WINDOW

# (list) Supported architectures
android.archs = arm64-v8a

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use
android.sdk = 33

# (str) Android build tools version to use
android.build_tools_version = 33.0.2

# (bool) Skip / delete old copies before building
android.skip_update = False

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color
# android.presplash_color = #FFFFFF

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug command)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
