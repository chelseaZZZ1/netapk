[app]

title = FF NetCutter

package.name = ffnetcutter
package.domain = org.netcutter

version = 0.1

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

requirements = python3,kivy

orientation = portrait

android.permissions = INTERNET,ACCESS_NETWORK_STATE,CHANGE_NETWORK_STATE,SYSTEM_ALERT_WINDOW

android.archs = arm64-v8a

android.api = 33
android.minapi = 21
android.ndk = 25b

android.skip_update = False

fullscreen = 0

[buildozer]

log_level = 2
warn_on_root = 0
