def get_ticket_tier(days_before_event):
    """
    Determine the EventSphere ticket pricing tier for a registration,
    based on how many days before the event date the attendee registers.

    Tiers:
      30-365 days before -> "Early Bird"
      15-29 days before -> "Regular"
      3-14 days before -> "Late"
      0-2 days before -> "Last Minute"

    Raises:
      ValueError if days_before_event is outside the valid 0-365 range.
    """
    if days_before_event < 0 or days_before_event > 365:
        raise ValueError("days_before_event must be between 0 and 365")

    if days_before_event >= 30:
        return "Early Bird"
    elif days_before_event >= 15:
        return "Regular"
    elif days_before_event >= 3:
        return "Late"
    else:
        return "Last Minute"
