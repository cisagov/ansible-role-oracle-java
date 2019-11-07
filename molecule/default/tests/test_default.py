"""Module containing the tests for the default scenario."""

import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "pkg", ["oracle-java11-installer-local", "oracle-java11-set-default-local"]
)
def test_packages(host, pkg):
    """Test that the expected packages were installed."""
    assert host.package(pkg).is_installed
