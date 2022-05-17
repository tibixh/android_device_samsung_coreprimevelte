import os

copyrightText = """
#
# Copyright (C) 2020 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License."""

vendordir = '../../../vendor/samsung/coreprimevelte'
lines = []

if not os.path.exists(f'{vendordir}/BoardConfigVendor.mk'):
    f = open(f'{vendordir}/BoardConfigVendor.mk', "w")
    f.write(f"# This file was generated by {os.getcwd()}/setup-makefiles.py")
    f.close()
    print("Generated BoardConfigVendor.mk")

if not os.path.exists(f'{vendordir}/coreprimevelte-vendor.mk'):
    f = open(f'{vendordir}/coreprimevelte-vendor.mk', "w")
    f.write(copyrightText)
    f.write(f"# This file was generated by {os.getcwd()}/setup-makefiles.py")
    f.write("\n$(call inherit-product, vendor/samsung/coreprimevelte/coreprimevelte-vendor-blobs.mk)")
    f.close()
    print("Generated coreprimevelte-vendor.mk")

f = open(f'{vendordir}/coreprimevelte-vendor-blobs.mk','w')
f.write("VENDOR_PATH := vendor/samsung/coreprimevelte\n\nPRODUCT_COPY_FILES += \\")
for subdir, dir, files in os.walk(f'{vendordir}/proprietary/'):
    for file in files:
        path = os.path.join(subdir, file)
        path = path.split("proprietary")[1]
        lines.append(f"\n    $(VENDOR_PATH)/proprietary{path}:system{path}")

for line in lines:
    f.write(line)
    if lines.index(line) +1 < len(lines):
        f.write(" \\")
print("Generated coreprimevelte-vendor-blobs.mk")
f.close()

if not os.path.exists(f'{vendordir}/Android.mk'):
    f = open(f'{vendordir}/Android.mk', 'w')
    f.write(copyrightText)
    f.close()
    print("Android.mk may be edited for additional modules!")

print("setup-makefiles.py done")