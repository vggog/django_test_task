def get_price_in_dollars(price_in_cents: int) -> float:
    """
    Because the price is stored in cents in the database,
    you need to convert it to dollars.
    """
    return price_in_cents / 100
