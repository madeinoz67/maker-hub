from typing import List


def get_part_count() -> int:
    return 283


def get_total_stock() -> int:
    return 1_00


def get_stock_value() -> int:
    return 1_500


def get_latest_parts(limit: int = 5) -> List:
    return [
        {
            "id": "cfc3w1ypx6g6x81ftygyzhk4ak",
            "name": "DMG1012T-7",
            "description": "Transistor: N-MOSFET; unipolar; 20V; 0.45A; 0.28W; SOT523",
        },
        {
            "id": "fv5vatbcprgx2910n2h3czc1xv",
            "name": "SK-3296S-01-L1",
            "description": "SPDT 50mA @ 12VDC 12V On-On SMD Toggle Switches RoHS",
        },
        {
            "id": "ath9dj6w8pjjf94g2sysfmv3f3",
            "name": "AO3400A",
            "description": "N-Channel 30V 5.8A 1.4V @ 250uA 28mΩ @ 5.8A,10V 1.4W MOSFET",
        },
    ][:limit]
