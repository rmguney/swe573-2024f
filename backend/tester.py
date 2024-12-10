import os
import sys
import django
from django.test.utils import get_runner
from django.conf import settings
from django.db import connection

# Set the settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'threef_backend.settings')

# Initialize Django
django.setup()


def terminate_test_database_connections():
    """Forcefully terminate all connections to the test database."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT pg_terminate_backend(pid) 
                FROM pg_stat_activity 
                WHERE datname = current_database()
                AND pid <> pg_backend_pid()
            """)
    except Exception as e:
        print(f"Warning: Could not terminate connections: {e}")


def run_tests(test_labels=None):
    """Run the specified test cases or all tests."""
    try:
        # Ensure clean connections
        terminate_test_database_connections()
        connection.close()

        # Configure test settings
        settings.TEST_RUNNER = 'threef.tests.test_runner.NoDbTestRunner'
        
        # Initialize and run tests
        test_runner = get_runner(settings)(keepdb=True, interactive=False)
        failures = test_runner.run_tests(test_labels)
        
        return failures

    except Exception as e:
        print(f"Error running tests: {e}")
        if input("Would you like to try again? (y/n): ").lower() == 'y':
            return run_tests(test_labels)
        return 1


def display_menu():
    print("\nChoose a test category:")
    print("1. Run model tests")
    print("2. Run serializer tests")
    print("3. Run URL tests")
    print("4. Run all tests")
    print("5. Exit")


def main():
    while True:
        # Display menu
        display_menu()

        # Get user input
        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        # Define test paths based on user choice
        if choice == "1":
            print("Running model tests...")
            test_labels = ["threef.tests.test_models"]
        elif choice == "2":
            print("Running serializer tests...")
            test_labels = ["threef.tests.test_serializers"]
        elif choice == "3":
            print("Running URL tests...")
            test_labels = ["threef.tests.test_urls"]
        elif choice == "4":
            print("Running all tests...")
            test_labels = ["threef.tests.test_urls"]
            test_labels = ["threef.tests.test_serializers"]
            test_labels = ["threef.tests.test_models"]
        elif choice == "5":
            print("Exiting the test runner.")
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")
            continue

        # Run tests and handle results
        failures = run_tests(test_labels)

        if failures is None or failures > 0:
            print(f"Test run failed or {failures} test(s) failed!")
        else:
            print("All tests passed!")

        # Ask if the user wants to run more tests
        run_again = input("\nDo you want to run more tests? (y/n): ").strip().lower()
        if run_again != 'y':
            print("Exiting the test runner.")
            sys.exit(0)


if __name__ == "__main__":
    main()
