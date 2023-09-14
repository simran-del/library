import unittest
from member import Member

class TestMember(unittest.TestCase):
    def test_member_creation(self):
        member = Member("John Doe", "M001")
        self.assertEqual(member.name, "John Doe")
        self.assertEqual(member.membership_number, "M001")
        self.assertEqual(member.outstanding_debt, 0)

    def test_outstanding_debt(self):
        member = Member("Jane Smith", "M002")
        
        # Simulate a member accumulating a debt
        member.outstanding_debt = 100
        
        # Ensure outstanding debt is correctly recorded
        self.assertEqual(member.outstanding_debt, 100)

if __name__ == '__main__':
    unittest.main()
