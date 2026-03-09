# Singapore CPF, SDL, SHG calculations
# These functions are added to salary slip formula whitelisted_globals
# so they can be called directly in Salary Component formulas.

from frappe.utils import flt, getdate
from datetime import date

OW_CEILING = 6800

# CPF rates: (age_from, age_to, employee_rate, employer_rate)
_RATES_CITIZEN = [
    (0, 55, 0.20, 0.17),
    (55, 60, 0.15, 0.145),
    (60, 65, 0.095, 0.11),
    (65, 70, 0.07, 0.085),
    (70, 999, 0.05, 0.075),
]
_RATES_PR1 = [
    (0, 55, 0.05, 0.04),
    (55, 60, 0.05, 0.04),
    (60, 65, 0.05, 0.035),
    (65, 70, 0.05, 0.035),
    (70, 999, 0.05, 0.035),
]
_RATES_PR2 = [
    (0, 55, 0.15, 0.09),
    (55, 60, 0.125, 0.075),
    (60, 65, 0.05, 0.055),
    (65, 70, 0.05, 0.055),
    (70, 999, 0.05, 0.055),
]


def _get_age(dob):
    if not dob:
        return 30
    dob = getdate(dob)
    today = date.today()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age


def _get_rates(age, pr_status):
    pr = pr_status or "Singapore Citizen"
    if pr == "Foreigner":
        return (0.0, 0.0)
    if pr == "PR - 1st Year":
        table = _RATES_PR1
    elif pr == "PR - 2nd Year":
        table = _RATES_PR2
    else:
        table = _RATES_CITIZEN
    for a1, a2, er, ee in table:
        if a1 <= age < a2:
            return (er, ee)
    return (0.0, 0.0)


def sg_cpf_employee(basic, dob, pr_status):
    """Employee CPF deduction. Call as: sg_cpf_employee(BS, date_of_birth, sg_pr_status)"""
    age = _get_age(dob)
    emp_rate, _ = _get_rates(age, pr_status)
    return round(min(flt(basic), OW_CEILING) * emp_rate)


def sg_cpf_employer(basic, dob, pr_status):
    """Employer CPF contribution. Call as: sg_cpf_employer(BS, date_of_birth, sg_pr_status)"""
    age = _get_age(dob)
    _, er_rate = _get_rates(age, pr_status)
    return round(min(flt(basic), OW_CEILING) * er_rate)


def sg_sdl(basic):
    """Skills Development Levy. Call as: sg_sdl(BS)"""
    if flt(basic) <= 0:
        return 0
    return min(max(round(flt(basic) * 0.0025, 2), 2.0), 11.25)


def sg_shg(basic, ethnicity):
    """SHG Fund (CDAC/MBMF/SINDA/ECF). Call as: sg_shg(BS, sg_ethnicity)"""
    w = flt(basic)
    e = ethnicity or ""
    if e == "Chinese":
        if w < 500: return 0
        if w < 1000: return 0.5
        if w < 1500: return 1.0
        if w < 2000: return 1.5
        if w < 2500: return 2.0
        if w < 3500: return 3.0
        if w < 5000: return 5.0
        if w < 7500: return 7.0
        if w < 10000: return 9.0
        return 11.0
    if e == "Malay":
        if w < 1000: return 0
        if w < 2000: return 3.0
        if w < 3000: return 4.5
        if w < 5000: return 6.5
        if w < 7500: return 15.0
        return 22.0
    if e == "Indian":
        if w < 1000: return 0
        if w < 1500: return 1.0
        if w < 2500: return 3.0
        if w < 5000: return 5.0
        if w < 7500: return 7.0
        if w < 10000: return 9.0
        return 12.0
    if e == "Eurasian":
        if w < 1000: return 0
        return 2.0
    return 0
