# test_chainanchor.py
"""
Tests for ChainAnchor module.
"""

import unittest
from chainanchor import ChainAnchor

class TestChainAnchor(unittest.TestCase):
    """Test cases for ChainAnchor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainAnchor()
        self.assertIsInstance(instance, ChainAnchor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainAnchor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
