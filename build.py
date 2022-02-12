import sys
import os
import subprocess

# run cargo build --release
# check if cargo build was successful
if subprocess.run(["cargo", "build", "--release"]).returncode != 0:
    print("cargo build failed")
    sys.exit(1)

# move and rename ./target/release/package_name_rs.dll to ./package_name/package_name_rs.pyd
os.rename("./target/release/package_name_rs.dll", "./package_name/package_name_rs.pyd")
