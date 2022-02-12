import sys

from setuptools import setup, find_packages

try:
    from setuptools_rust import RustExtension, Binding, Strip
except ImportError:
    import subprocess

    errno = subprocess.call([sys.executable, '-m', 'pip', 'install', 'setuptools-rust'])
    if errno:
        print("Please install the setuptools-rust package.")
        raise SystemExit(errno)
    else:
        from setuptools_rust import RustExtension, Binding, Strip

try:
    import toml
except ImportError:
    import subprocess

    errno = subprocess.call([sys.executable, '-m', 'pip', 'install', 'toml'])
    if errno:
        print("Please install the toml package.")
        raise SystemExit(errno)
    else:
        import toml

cfg = toml.load("Cargo.toml")
package_meta = cfg['package']


setup_requires = [
    'setuptools',
    'setuptools-rust>=0.10.1'
]

setup(
    name="package_name",
    version=package_meta['version'],
    author=package_meta['authors'][0],
    license="BSD-3-Clause",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Rust",
        "Programming Language :: Python :: 3",
    ],
    rust_extensions=[
        RustExtension(
            'package_name.package_name_rs',
            'Cargo.toml',
            binding=Binding.PyO3,
            strip=Strip.Debug),
    ],
    packages=find_packages(),
    setup_requires=setup_requires,
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.6',
)
