#!/usr/bin/env python3
"""
Script to calculate the remaining days of GitHub Student Developer Pack access.
"""

from datetime import datetime

def calculate_remaining_days():
    """Calculate days remaining until GitHub Student Developer Pack expires."""
    # Current date
    today = datetime.now()
    
    # Expiration date: October 2027 (assuming end of October, 31st)
    expiration_date = datetime(2027, 10, 31)
    
    # Calculate the difference
    remaining_days = (expiration_date - today).days
    
    return remaining_days, expiration_date

def main():
    """Main function to display access information."""
    remaining_days, expiration_date = calculate_remaining_days()
    
    print("=" * 60)
    print("GitHub Student Developer Pack Access Information")
    print("=" * 60)
    print(f"\nExpiration Date: {expiration_date.strftime('%B %d, %Y')}")
    print(f"Today's Date: {datetime.now().strftime('%B %d, %Y')}")
    print(f"\n🎁 Days Remaining: {remaining_days} days")
    print(f"🎓 Approximately {remaining_days // 365} years and {remaining_days % 365} days")
    print("\n" + "=" * 60)
    print("\nFeatures included in GitHub Student Developer Pack:")
    print("  • GitHub Copilot")
    print("  • GitHub Pro")
    print("  • GitHub Actions minutes")
    print("  • GitHub Packages storage")
    print("  • And many more development tools and resources")
    print("\nFor more information, visit:")
    print("  https://education.github.com/pack")
    print("=" * 60)

if __name__ == "__main__":
    main()
