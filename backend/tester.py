import os
import sys
import unittest
import django
from django.test.utils import get_runner
from django.conf import settings

# Set the settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'threef_backend.settings')

# Now set up Django
django.setup()

# Ensure Django settings are configured
if not settings.configured:
    import django
    django.setup()

def run_tests(test_labels=None):
    """Run the specified test cases or all tests."""
    test_runner = get_runner(settings)()
    failures = test_runner.run_tests(test_labels)
    return failures

def display_menu():
    """Display the test options menu"""
    print("Choose a test category:")
    print("1. Run model tests")
    print("2. Run serializer tests")
    print("3. Run view tests")
    print("4. Run all tests")
    print("5. Exit")

def main():
    while True:
        # Display menu
        display_menu()
        
        # Get user input
        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        # Run corresponding tests based on user's choice
        if choice == "1":
            print("Running model tests...")
            failures = run_tests(["threef.tests.test_models"])
        elif choice == "2":
            print("Running serializer tests...")
            failures = run_tests(["threef.tests.test_serializers"])
        elif choice == "3":
            print("Running view tests...")
            failures = run_tests(["threef.tests.test_views"])
        elif choice == "4":
            print("Running all tests...")
            failures = run_tests()
        elif choice == "5":
            print("Exiting the test runner.")
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")
            continue

        # Check if there were failures
        if failures:
            print(f"{failures} test(s) failed!")
        else:
            print("All tests passed!")
        
        # Ask if the user wants to run more tests
        run_again = input("Do you want to run more tests? (y/n): ").strip().lower()
        if run_again != 'y':
            print("Exiting the test runner.")
            sys.exit(0)

if __name__ == "__main__":
    main()
