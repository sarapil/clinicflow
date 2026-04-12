---
title: CF Clinic Invoice — Patient Billing
icon: receipt
context_type: doctype
context_reference: CF Clinic Invoice
priority: 7
roles: [CF Billing Officer, Administrator]
---

# CF Clinic Invoice — Patient Billing

The **CF Clinic Invoice** manages all patient billing, including service charges, insurance splits, and payment tracking.

## ## patient

Link to the **CF Patient** being invoiced.

## ## consultation

Link to the **CF Consultation** that generated this invoice. The invoice items are auto-populated from the consultation's services.

## ## invoice_date

The **date** of service (defaults to today).

## ## items (child table)

List of **services billed** in this invoice. Each item includes:

- Service (link to CF Service)
- Quantity
- Unit price (pulled from CF Service)
- Insurance covered amount
- Patient payable amount

## ## total_amount

Sum of all invoice item amounts. **Auto-calculated** from the items table.

## ## insurance_policy

Link to the patient's **CF Insurance Policy**. When set:

- Insurance coverage percentage is applied automatically
- Covered amount and patient share are calculated

## ## insurance_amount

The **amount covered by insurance**. Auto-calculated based on the insurance policy percentages.

## ## patient_amount

The **amount the patient must pay** (total minus insurance coverage).

## ## payment_status

| Status               | Meaning                           |
| -------------------- | --------------------------------- |
| Unpaid               | No payment received               |
| Partial              | Partial payment received          |
| Paid                 | Fully settled                     |
| Waived               | Amount waived (charity/emergency) |
| Insurance Processing | Awaiting insurance reimbursement  |

## Insurance Claim Workflow

1. Add insurance policy to invoice
2. System calculates patient share and insurance amount
3. Click "Submit Insurance Claim" → Creates CF Insurance Claim
4. Insurance processes claim → Update claim status
5. Receive payment → Mark invoice as Paid

## ## Payment Methods

- Cash
- Card (POS terminal)
- Bank Transfer
- Mobile Money (MTN MoMo, Opay, etc.)
- NHIA/HMO Direct

## Quick Actions

- **Record Payment**: Click "Make Payment" to create a CF Clinic Payment
- **Submit Insurance Claim**: Auto-generates CF Insurance Claim
- **Print Invoice**: Patient-readable invoice in EN or AR
- **Send to Patient**: Email or WhatsApp invoice via NotifyPro
