# Copyright (c) 2024, Arkan Lab and contributors
# For license information, please see license.txt

import frappe
import pytest


class TestClinicFlowServices:
    """Unit tests for ClinicFlow service layer."""

    def test_module_import(self):
        """Verify clinicflow module can be imported."""
        import clinicflow
        assert clinicflow is not None

    def test_hooks_loaded(self):
        """Verify hooks.py is valid and loadable."""
        from clinicflow import hooks
        assert hasattr(hooks, "app_name")
        assert hooks.app_name == "clinicflow"

    def test_seed_module_exists(self):
        """Verify seed.py exists and is importable."""
        from clinicflow import seed
        assert hasattr(seed, "seed_data")

    def test_exceptions_module(self):
        """Verify custom exceptions are defined."""
        from clinicflow import exceptions
        assert hasattr(exceptions, "AppBaseException")

    def test_api_response_helpers(self):
        """Verify API response helpers exist."""
        from clinicflow.api import response
        assert callable(getattr(response, "success", None))
        assert callable(getattr(response, "error", None))
        assert callable(getattr(response, "paginated", None))
