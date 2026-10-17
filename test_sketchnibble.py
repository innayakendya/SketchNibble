# test_sketchnibble.py
"""
Tests for SketchNibble module.
"""

import unittest
from sketchnibble import SketchNibble

class TestSketchNibble(unittest.TestCase):
    """Test cases for SketchNibble class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SketchNibble()
        self.assertIsInstance(instance, SketchNibble)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SketchNibble()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
