import os
import sys
import unittest
import django
from django.test.utils import get_runner
from django.conf import settings
from django.db import connection
import time

# Set the settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'threef_backend.settings')

# Now set up Django
django.setup()

# Ensure Django settings are configured
if not settings.configured:
    import django
    django.setup()

def terminate_active_connections(retries=5, delay=2):
    """Terminate active connections to the test database."""
    for _ in range(retries):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT pg_terminate_backend(pg_stat_activity.pid)
                FROM pg_stat_activity
                WHERE pg_stat_activity.datname = 'test_postgres'
                AND pid <> pg_backend_pid();
            """)
        time.sleep(delay)
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*)
                FROM pg_stat_activity
                WHERE pg_stat_activity.datname = 'test_postgres'
                AND pid <> pg_backend_pid();
            """)
            active_connections = cursor.fetchone()[0]
            if active_connections == 0:
                break
    else:
        raise Exception("Failed to terminate all active connections to the test database.")

def run_tests(test_labels=None):
    """Run the specified test cases or all tests."""
    settings.DATABASES['default'] = settings.DATABASES['test']
    terminate_active_connections()  # Terminate active connections before running tests
    test_runner = get_runner(settings)()
    failures = test_runner.run_tests(test_labels)
    return failures

def display_menu():
    """Display the test options menu"""
    print("Choose a test category:")
    print("1. Run xx tests")
    print("2. Run xx tests")
    print("3. Run xx tests")
    print("4. Run xx tests")
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
            failures = run_tests([""])
        elif choice == "2":
            print("Running serializer tests...")
            failures = run_tests([""])
        elif choice == "3":
            print("Running view tests...")
            failures = run_tests([""])
        elif choice == "4":
            print("Running URL tests...")
            failures = run_tests([""])
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
