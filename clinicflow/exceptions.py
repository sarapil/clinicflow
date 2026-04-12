# Copyright (c) 2026, Arkan Lab — ClinicFlow
# SPDX-License-Identifier: GPL-3.0


class ClinicFlowBaseException(Exception):
    http_status_code = 500
    error_code = "UNKNOWN_ERROR"


class ValidationError(ClinicFlowBaseException):
    http_status_code = 400
    error_code = "VALIDATION_ERROR"


class PermissionDenied(ClinicFlowBaseException):
    http_status_code = 403
    error_code = "PERMISSION_DENIED"


class NotFound(ClinicFlowBaseException):
    http_status_code = 404
    error_code = "NOT_FOUND"


class ConflictError(ClinicFlowBaseException):
    http_status_code = 409
    error_code = "CONFLICT"


class AppointmentConflict(ConflictError):
    error_code = "APPOINTMENT_CONFLICT"


class PatientNotFound(NotFound):
    error_code = "PATIENT_NOT_FOUND"


class PractitionerUnavailable(ValidationError):
    error_code = "PRACTITIONER_UNAVAILABLE"


class InsuranceClaimError(ClinicFlowBaseException):
    http_status_code = 400
    error_code = "INSURANCE_CLAIM_ERROR"
