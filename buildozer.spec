[app]
title = TaxSoftwareMobile
package.name = taxsoftwaremobile
package.domain = org.alok
source.dir = .
source.include_exts = py,png,json
source.main = mobile_main.py
version = 1.0.0
requirements = python3,kivy

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1

fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
