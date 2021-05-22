import datetime
from typing import List, Optional


def project_count() -> int:
    return 34


def latest_projects(limit: int = 5) -> List:
    return [
        {
            "id": "5z2v341ypg4f6b684n4gra3myk",
            "name": "STR-16-011-BatteryDesulfator",
            "description": "Battery Desulfator",
        },
        {
            "id": "5hhxy81gm44f69rn3mkpz8c6tn",
            "name": "Dog Bark Stop",
            "description": "Project to stop dog barking",
        },
        {
            "id": "e77wqg1h364f69rn3mkpz8c6tn",
            "name": "STR-15-011-PiCluster",
            "description": "Raspberry Pi Cluster",
        },
    ][:limit]
