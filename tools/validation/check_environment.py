"""Validate the main Quantum Computing Lab dependencies."""

from importlib.metadata import PackageNotFoundError, version

PACKAGES = [
    "qiskit",
    "qiskit-aer",
    "pennylane",
    "cirq",
    "qutip",
    "jupyterlab",
    "numpy",
    "scipy",
    "matplotlib",
]


def get_version(package: str) -> str:
    """Return the installed version of a package."""
    try:
        return version(package)
    except PackageNotFoundError:
        return "NOT INSTALLED"


def main() -> None:
    """Print the status of the main laboratory dependencies."""
    print("Quantum Computing Lab environment")
    print("=" * 40)

    failed = False

    for package in PACKAGES:
        package_version = get_version(package)
        status = "OK" if package_version != "NOT INSTALLED" else "MISSING"
        print(f"{package:<16} {package_version:<16} {status}")

        if status == "MISSING":
            failed = True

    if failed:
        raise SystemExit("Environment validation failed.")

    print("=" * 40)
    print("Environment validation completed successfully.")


if __name__ == "__main__":
    main()
