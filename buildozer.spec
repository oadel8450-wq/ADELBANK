[app]

title = خدمات البنك
package.name = bankservices
package.domain = org.adelomar

source.dir = .
source.main = main.py

version = 1.0

requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, SEND_SMS, READ_SMS

android.api = 33
android.minapi = 21
android.arch = arm64-v8a

android.accept_sdk_license = True

source.include_exts = py,png,jpg,jpeg,kv,atlas,db,sqlite3,json,txt
source.exclude_exts = spec,pyc,pyo
source.exclude_dirs = .git,.buildozer,__pycache__

android.presplash_color = #FFFFFF

log_level = 2


[buildozer]

log_level = 2
warn_on_root = 1
