import io
import os

from six import StringIO
from stix.core import STIXPackage
import stixmarx

import pytest
from stix2elevator import (elevate,
                           elevate_file,
                           elevate_package,
                           elevate_string)
from stix2elevator.options import initialize_options, set_option_value
from stix2elevator.utils import find_dir

# This module only tests for the main functions used to interact with the elevator from a programmatic or
# interactive point of view. Actual idioms tests are done in test_idioms.py


def setup_options():
    version = os.environ["VERSION"]
    policy = os.environ["MISSING_POLICY"]

    initialize_options()
    set_option_value("missing_policy", policy)
    set_option_value("log_level", "DEBUG")
    set_option_value("spec_version", version)
    set_option_value("validator_args", "--version " + version)
    set_option_value("policy", "no_policy")


def test_elevate_with_marking_container():
    setup_options()

    directory = os.path.dirname(__file__)
    xml_idioms_dir = find_dir(directory, "idioms-xml")
    archive_file = os.path.join(xml_idioms_dir, "141-TLP-marking-structures.xml")

    with io.open(archive_file, mode="r", encoding="utf-8") as f:
        input_stix = f.read()

    container = stixmarx.parse(StringIO(input_stix))
    json_result = elevate(container)
    assert json_result
    print(json_result)


def test_elevate_with_stix_package():
    setup_options()

    directory = os.path.dirname(__file__)
    xml_idioms_dir = find_dir(directory, "idioms-xml")
    archive_file = os.path.join(xml_idioms_dir, "141-TLP-marking-structures.xml")

    with io.open(archive_file, mode="r", encoding="utf-8") as f:
        input_stix = f.read()

    json_result = elevate(STIXPackage.from_xml(StringIO(input_stix)))
    assert json_result
    print(json_result)


def test_elevate_with_text_string():
    setup_options()

    directory = os.path.dirname(__file__)
    xml_idioms_dir = find_dir(directory, "idioms-xml")
    archive_file = os.path.join(xml_idioms_dir, "141-TLP-marking-structures.xml")

    with io.open(archive_file, mode="r", encoding="utf-8") as f:
        input_stix = f.read()

    json_result = elevate(input_stix)
    assert json_result
    print(json_result)


def test_elevate_with_binary_string():
    setup_options()

    directory = os.path.dirname(__file__)
    xml_idioms_dir = find_dir(directory, "idioms-xml")
    archive_file = os.path.join(xml_idioms_dir, "141-TLP-marking-structures.xml")

    with io.open(archive_file, mode="r", encoding="utf-8") as f:
        input_stix = f.read().encode("utf-8")

    json_result = elevate(input_stix)
    assert json_result
    print(json_result)


def test_elevate_with_file():
    setup_options()

    directory = os.path.dirname(__file__)
    xml_idioms_dir = find_dir(directory, "idioms-xml")
    archive_file = os.path.join(xml_idioms_dir, "141-TLP-marking-structures.xml")

    json_result = elevate(archive_file)
    assert json_result
    print(json_result)


def test_deprecated_elevate_file():
    setup_options()

    directory = os.path.dirname(__file__)
    xml_idioms_dir = find_dir(directory, "idioms-xml")
    archive_file = os.path.join(xml_idioms_dir, "141-TLP-marking-structures.xml")

    with pytest.warns(DeprecationWarning):
        json_result = elevate_file(archive_file)

    assert json_result
    print(json_result)


def test_deprecated_elevate_string():
    setup_options()

    directory = os.path.dirname(__file__)
    xml_idioms_dir = find_dir(directory, "idioms-xml")
    archive_file = os.path.join(xml_idioms_dir, "141-TLP-marking-structures.xml")

    with pytest.warns(DeprecationWarning):
        with io.open(archive_file, mode="r", encoding="utf-8") as f:
            input_stix = f.read()
        json_result = elevate_string(input_stix)

    assert json_result
    print(json_result)


def test_deprecated_elevate_package():
    setup_options()

    directory = os.path.dirname(__file__)
    xml_idioms_dir = find_dir(directory, "idioms-xml")
    archive_file = os.path.join(xml_idioms_dir, "141-TLP-marking-structures.xml")

    with pytest.warns(DeprecationWarning):
        with io.open(archive_file, mode="r", encoding="utf-8") as f:
            input_stix = f.read()
        json_result = elevate_package(STIXPackage.from_xml(StringIO(input_stix)))

    assert json_result
    print(json_result)
