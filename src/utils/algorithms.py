"""
Core scoring engines and data sanitization compliance loggers.
"""
import datetime

def calculate_fit_score(cpu: str, ram: int, storage: int, powers_on: bool, condition: str) -> float:
    """
    Evaluates hardware viability for refurbishment (0.0 to 100.0).
    """
    if not powers_on:
        return 0.0  # Immediate recycling recommendation
    
    score = 0.0
    
    # RAM Scoring
    if ram >= 16:
        score += 40
    elif ram >= 8:
        score += 30
    elif ram >= 4:
        score += 10

    # CPU Scoring
    if "i5" in cpu.lower() or "i7" in cpu.lower() or "ryzen" in cpu.lower():
        score += 40
    elif "i3" in cpu.lower():
        score += 20
    
    # Physical Condition Scoring
    if condition.lower() == "good":
        score += 20
    elif "minor" in condition.lower():
        score += 10
    
    return min(score, 100.0)

def calculate_esg_impact(device_count: int) -> dict:
    """
    Calculates environmental and social metrics per refurbished unit.
    """
    return {
        "ewaste_kg": round(device_count * 2.1, 1),
        "co2_saved_kg": round(device_count * 160.0, 1),
        "digital_access_units": device_count
    }

def log_nist_sanitization(device_id: str, serial: str, status: str = "COMPLETED") -> dict:
    """
    Logs NIST 800-88 compliance events for corporate data security.
    """
    return {
        "device_id": device_id,
        "serial_number": serial,
        "standard": "NIST 800-88 Rev 1 Clear/Purge",
        "timestamp": datetime.datetime.now().isoformat(),
        "status": status
    }