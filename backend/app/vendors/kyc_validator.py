"""
Automated Vendor KYC Identification Verification & Checksum Validator.
Implements Indian GSTIN (ISO/IEC 7064 Mod 11,10), PAN structure verification,
and Bank IFSC routing codes.
"""

import re
from typing import Dict, Optional, Tuple, Any


class KycValidationEngine:
    # Character conversion mapping for GSTIN Mod 11,10 algorithm
    CHAR_MAP = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @staticmethod
    def validate_gstin(gstin: str) -> Tuple[bool, Optional[str]]:
        """
        Validates 15-digit Indian GSTIN format and checksum.
        Format: 2 digits (State) + 10 chars (PAN) + 1 digit (Entity) + 'Z' + 1 checksum char.
        """
        clean_gst = gstin.strip().upper()
        if not re.match(r"^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$", clean_gst):
            return False, "Invalid GSTIN format structure (Expected 15 alphanumeric characters e.g. 27AAACH7409R1ZZ)."

        # Mod 11,10 checksum validation
        factor = 1
        total = 0
        mod = len(KycValidationEngine.CHAR_MAP)

        for i in range(len(clean_gst) - 1):
            char = clean_gst[i]
            code_point = KycValidationEngine.CHAR_MAP.index(char)
            digit = code_point * factor
            factor = 2 if factor == 1 else 1
            digit = (digit // mod) + (digit % mod)
            total += digit

        calculated_check = (mod - (total % mod)) % mod
        expected_char = KycValidationEngine.CHAR_MAP[calculated_check]

        if clean_gst[-1] != expected_char:
            return False, f"GSTIN checksum mismatch (Provided: {clean_gst[-1]}, Expected: {expected_char})."

        return True, None

    @staticmethod
    def validate_pan(pan: str) -> Tuple[bool, Optional[str]]:
        """
        Validates 10-character Permanent Account Number (PAN).
        4th character denotes entity type:
        P = Individual, C = Company, H = HUF, F = Firm, A = AOP, T = Trust.
        """
        clean_pan = pan.strip().upper()
        if not re.match(r"^[A-Z]{3}[PCHFATBLJG][A-Z]{1}[0-9]{4}[A-Z]{1}$", clean_pan):
            return False, "Invalid PAN format (Expected 10 characters e.g. AAACH7409R)."
        return True, None

    @staticmethod
    def validate_bank_ifsc(ifsc: str) -> Tuple[bool, Optional[str]]:
        """
        Validates 11-character Indian Financial System Code (IFSC).
        Format: 4 letters (Bank) + '0' + 6 alphanumeric characters.
        """
        clean_ifsc = ifsc.strip().upper()
        if not re.match(r"^[A-Z]{4}0[A-Z0-9]{6}$", clean_ifsc):
            return False, "Invalid IFSC format (Expected 11 characters e.g. HDFC0000123)."
        return True, None
