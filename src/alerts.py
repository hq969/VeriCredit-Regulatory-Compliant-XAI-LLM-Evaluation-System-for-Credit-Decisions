def send_alert(alerts):
    if alerts:
        print("🚨 REGULATORY ALERT TRIGGERED 🚨")
        for k, v in alerts.items():
            print(f"{k} breached: {v}")
