import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Literal, Optional, Tuple, get_args

import click
import toml
from loguru import logger

__all__ = [
    "BuildType",
    "generate_final_project_info",
    "get_current_project_info",
    "load_toml",
    "update_toml",
]


BuildType = Literal["release", "nightly", "dev"]


def load_toml(toml_path: str) -> dict:
    """
    Load the TOML file.

    :param toml_path: Path to the TOML file.
    :return: The loaded TOML file.
    """
    with Path(toml_path).open() as file:
        return toml.load(file)


def get_current_project_info(toml_data: Dict[str, Any]) -> Tuple[str, str]:
    """
    Get the current project name and version from the TOML file.

    :param toml_data: The loaded TOML file.
    :return: Tuple of the current project name and version.
    """
    current_name = toml_data["project"]["name"]
    current_version = toml_data["project"]["version"]

    return current_name, current_version


def generate_final_project_info(
    package_name: str,
    package_version: str,
    build_type: BuildType,
    build_number: str,
) -> Tuple[str, str]:
    """
    Generate the final project name and version based on the build type.

    :param package_name: the package name to finalize
    :param package_version: the package version to finalize
    :param build_type: the build type to generate the final project name and version
    :param build_number: the build number for dev builds
    :return: Tuple of the final project name and version
    """
    if not re.match(r"^\d+\.\d+\.\d+$", package_version):
        raise ValueError(
            f"Version '{package_version}' does not match the "
            f"semantic versioning pattern '#.#.#'",
        )

    if build_type == "dev":
        project_name = f"{package_name}-dev"
        version = f"{package_version}.{build_number}"
    elif build_type == "nightly":
        project_name = f"{package_name}-nightly"
        date_str = datetime.now().strftime("%Y%m%d")
        version = f"{package_version}.{date_str}"
    elif build_type == "release":
        project_name = package_name
        version = package_version
    else:
        raise ValueError(f"Unknown build type: {build_type}")

    return project_name, version


@click.command()
@click.option(
    "--build_type",
    type=click.Choice(get_args(BuildType)),
    required=True,
    help="Type of build: release, nightly, or dev.",
)
@click.option(
    "--dev_build_number", type=str, default="0", help="Build number for dev builds."
)
@click.option(
    "--name_override", type=str, default=None, help="Optional package name override."
)
@click.option(
    "--version_override",
    type=str,
    default=None,
    help="Optional package version override.",
)
@click.option(
    "--toml_path",
    type=str,
    default="pyproject.toml",
    help="Path to the TOML file to load.",
)
@click.option(
    "--output_path",
    type=str,
    default="pyproject.toml",
    help="Path to save the updated TOML file.",
)
def update_toml(
    build_type: BuildType,
    dev_build_number: str,
    name_override: Optional[str],
    version_override: Optional[str],
    toml_path: str,
    output_path: str,
):
    """
    Update the project name and version in the TOML file.

    :param build_type:
    :param dev_build_number:
    :param name_override:
    :param version_override:
    :param toml_path:
    :param output_path:
    :return:
    """
    try:
        toml_data = load_toml(toml_path)
        current_name, current_version = get_current_project_info(toml_data)
        project_name, version = generate_final_project_info(
            package_name=name_override if name_override else current_name,
            package_version=version_override if version_override else current_version,
            build_type=build_type,
            build_number=dev_build_number,
        )

        toml_data["project"]["name"] = project_name
        toml_data["project"]["version"] = version

        with Path(output_path).open("w") as file:
            toml.dump(toml_data, file)

        logger.info(
            f"Updated project name to: {project_name} and version to: {version}"
        )

    except Exception as err:
        logger.error(f"Failed to update the TOML file: {err}")
        raise


if __name__ == "__main__":
    update_toml()
