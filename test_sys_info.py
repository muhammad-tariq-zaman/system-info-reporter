import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest
from sys_info import info
class T(unittest.TestCase):
    def test_fields(self):
        r = info()
        self.assertTrue(r["os"]); self.assertGreaterEqual(r["cpu_count"], 1); self.assertTrue(r["python"])
if __name__ == "__main__": unittest.main()
