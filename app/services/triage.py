def classify_ticket(title: str, description: str):
    text = f"{title} {description}".lower()

    # Security keywords
    if any(word in text for word in ["phishing", "password", "login", "breach", "hacked"]):
        return "Security", "High"

    # Network keywords
    if any(word in text for word in ["vpn", "network", "wifi", "latency", "connection"]):
        return "Network", "Medium"

    # Hardware keywords
    if any(word in text for word in ["laptop", "screen", "keyboard", "battery", "printer"]):
        return "Hardware", "Low"

    # Default
    return "Software", "Low"
