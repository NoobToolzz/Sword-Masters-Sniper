from pathlib import Path


class Others:
    @staticmethod
    def clean_up_cache() -> None:
        for p in Path(".").rglob("*.py[co]"):
            p.unlink()
        for p in Path(".").rglob("__pycache__"):
            p.rmdir()
