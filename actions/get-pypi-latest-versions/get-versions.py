import argparse  # noqa: INP001
from dataclasses import dataclass
from functools import cached_property

import requests
from rss_parser import RSSParser

DEFAULT_NUM_VERSIONS = 1


@dataclass
class Config:
    package_name: str
    num_versions: int


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("package_name", type=str)
    parser.add_argument(
        "-n",
        "--num_versions",
        type=int,
        default=DEFAULT_NUM_VERSIONS,
        dest="num_versions",
    )
    args = parser.parse_args()
    return Config(args.package_name, args.num_versions)


class PackageVersionFeed:
    def __init__(self, package: str) -> None:
        self.feed_url = f"https://pypi.org/rss/project/{package}/releases.xml"
        response = requests.get(self.feed_url, timeout=30)
        self.feed = RSSParser.parse(response.text)

    @cached_property
    def versions(self) -> list[str]:
        _versions: list[str] = []
        for item in self.feed.channel.items:
            _versions.append(str(item.title.content))
        return _versions


if __name__ == "__main__":
    config = parse_args()
    pvf = PackageVersionFeed(config.package_name)
    print(";".join(pvf.versions[: config.num_versions]))  # noqa: T201
