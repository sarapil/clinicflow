---
title: CF Insurance Claim — Insurance Claims Management
icon: shield
context_type: doctype
context_reference: CF Insurance Claim
priority: 6
roles: [CF Billing Officer, Administrator]
---

# CF Insurance Claim — Insurance Claims Management

The **CF Insurance Claim** tracks insurance reimbursement requests submitted on behalf of patients.

## ## invoice

Link to the **CF Clinic Invoice** this claim is for.

## ## policy

Link to the patient's **CF Insurance Policy** (NHIA, Hygeia, THT, Reliance, AIICO, etc.).

## ## claim_amount

The **total amount** being claimed from the insurance provider.

## ## items (child table)

Each claimed service, with the covered amount per service line.

## ## claim_status

| Status           | Meaning                |
| ---------------- | ---------------------- |
| Submitted        | Claim sent to insurer  |
| Under Review     | Insurer reviewing      |
| Approved         | Claim approved         |
| Partial Approval | Only part approved     |
| Rejected         | Claim denied           |
| Paid             | Reimbursement received |

## ## rejection_reason

If rejected, the insurance provider's reason code or explanation.

## Nigerian HMO Workflow

1. Patient presents HMO card → Link insurance policy in CF Patient
2. Doctor completes consultation → CF Clinic Invoice auto-calculates HMO portion
3. Billing officer creates CF Insurance Claim
4. Exports claim in HMO-required format (NHIA, Hygeia portal, etc.)
5. Receives reimbursement → Updates claim status to "Paid"

## Supported Providers

| Provider      | System                 | Notes                       |
| ------------- | ---------------------- | --------------------------- |
| NHIA          | Federal government HMO | Required for civil servants |
| Hygeia HMO    | Private HMO            | Common in Lagos/Abuja       |
| Reliance HMO  | Private HMO            | Growing Pan-Nigeria         |
| THT           | Total Health Trust     | Enterprise clients          |
| AIICO Medical | Private insurer        | Traditional insurance       |
