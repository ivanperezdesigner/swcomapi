"""Connecting to a real SOLIDWORKS.

Skipped unless ``SWCOMAPI_LIVE=1``. Nothing here opens, changes or saves a
document: it only reads identity and window state, so it is safe to run against
a session you are working in.

Run it with::

    set SWCOMAPI_LIVE=1
    .venv\\Scripts\\python -m pytest tests/live -v
"""

import pytest

import swcomapi as sw
from swcomapi import com
from swcomapi.api.app import SolidWorks

pytestmark = pytest.mark.live


@pytest.fixture(scope="module")
def app():
    """The SOLIDWORKS already on screen, or a new one if none is open.

    `visible=None` so that a session a human is using is left exactly as it
    was found.
    """
    try:
        return sw.attach(visible=None)
    except sw.SwNotRunningError:
        pytest.skip("no SOLIDWORKS session is open; start one to run the live tests")


class TestIdentity:
    def test_it_is_a_wrapper_not_a_raw_com_object(self, app):
        assert isinstance(app, SolidWorks)
        assert app.com is not None

    def test_revision_number_looks_like_a_version(self, app):
        revision = app.revision_number
        assert isinstance(revision, str)
        # Something like '34.3.0'.
        assert revision.split(".")[0].isdigit()

    def test_the_year_is_plausible(self, app):
        assert 2020 <= app.year <= 2100

    def test_build_numbers_are_three_strings(self, app):
        """Proof that the three [out] BSTR parameters were read correctly.

        Called the way the documentation reads - GetBuildNumbers2(True) - this
        raises "Type mismatch" instead.
        """
        builds = app.build_numbers
        assert len(builds) == 3
        assert all(isinstance(b, str) for b in builds)
        assert builds[0].startswith("sw")

    def test_the_base_version_agrees_with_the_derived_year(self, app):
        """Two independent sources of the year have to say the same thing.

        `year` is arithmetic on RevisionNumber; the base version string spells
        the year out. If these ever disagree, the +1992 rule has broken.
        """
        assert str(app.year) in app.build_numbers[0]

    def test_service_pack_is_a_small_int(self, app):
        assert 0 <= app.service_pack <= 20

    def test_version_reads_like_a_sentence(self, app):
        version = app.version
        assert version.startswith("SOLIDWORKS ")
        assert str(app.year) in version

    def test_process_id_is_a_live_process(self, app):
        import os

        pid = app.process_id
        assert isinstance(pid, int)
        assert pid > 0
        assert pid != os.getpid()

    def test_repr(self, app):
        assert repr(app).startswith("<SolidWorks SOLIDWORKS ")


class TestRawAccess:
    def test_the_escape_hatch_reaches_anything(self, app):
        """The promise that nothing in the API is ever out of reach."""
        assert app.com.RevisionNumber == app.revision_number

    def test_call_reads_a_property(self, app):
        assert com.call(app.com, "RevisionNumber") == app.revision_number

    def test_a_member_that_does_not_exist_says_so_clearly(self, app):
        with pytest.raises(sw.SwMemberNotFoundError) as caught:
            com.call(app.com, "ThisMethodWasNeverInAnyVersion")
        assert "ThisMethodWasNeverInAnyVersion" in str(caught.value)

    def test_a_bad_argument_gives_a_readable_hresult(self, app):
        """The error translation, on a real com_error rather than a fake."""
        with pytest.raises(sw.SwCallError) as caught:
            com.call(app.com, "GetBuildNumbers2", True)
        assert caught.value.hresult == 0x80020005  # DISP_E_TYPEMISMATCH
        assert "Type mismatch" in str(caught.value)


class TestWaitUntilReady:
    def test_an_already_running_application_answers_at_once(self, app):
        assert sw.wait_until_ready(app.com, timeout=5) == app.revision_number


class TestAttach:
    def test_attach_returns_the_same_application_twice(self, app):
        """SOLIDWORKS is a singleton server: attaching again finds the same
        process, it does not start a second one."""
        again = sw.attach(visible=None)
        assert again.process_id == app.process_id

    def test_connect_finds_the_running_one_rather_than_starting_another(self, app):
        again = sw.connect(visible=None)
        assert again.process_id == app.process_id
