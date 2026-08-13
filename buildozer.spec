[app]
title = TaxSoftwareMobile
package.name = taxsoftwaremobile
package.domain = org.alok
source.dir = .
source.include_exts = py,png,json
source.main = mobile_main.py
version = 1.0.0
requirements = python3,kivy==2.3.0

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0

fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
