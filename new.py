import os
import subprocess
import pickle
import requests
import base64
import sqlite3

def check_sql_injection(input_string):
    sql_injection_patterns = ['"', '|', '=', '--', "' OR 1=1 --"]
    for pattern in sql_injection_patterns:
        if pattern in input_string:
            print(f"⚠ Potential SQL Injection detected: {pattern}") 
            return f"Potential SQL Injection detected: '{pattern}' found."
    return "No SQL Injection detected."


def unsafe_pickle():
    with open("test.pkl", "wb") as f:
        pickle.dump({"command": "print('This should not execute arbitrary code')"}, f)

    with open("test.pkl", "rb") as f:
        data = pickle.load(f) 
        print("✅ Pickle loaded successfully:", data)

API_KEY = "sk-12345-test-key"

def send_data():
    sample_data = {"username": "admin", "status": "test"}
    requests.post("http://example.com/api", json=sample_data) 

def decode_obfuscated():
    encoded_payload = base64.b64encode(b"print('Test Payload Execution')").decode()
    decoded = base64.b64decode(encoded_payload).decode()
    print("🔍 Decoded Payload:", decoded)  # Instead of executing with eval

def unsafe_file_access():
    try:
        with open("test_config.txt", "r") as file:
            content = file.read()
            print("⚠ Read file content:", content[:50])
    except FileNotFoundError:
        print("File not found. Safe behavior.")

def run_command():
    command = "echo Hello World"  # Harmless command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("✅ Command Output:", result.stdout)

input_string = input("Enter a string to check for SQL injection: ")
result = check_sql_injection(input_string)
print(result)

unsafe_pickle()
send_data()
decode_obfuscated()
unsafe_file_access()
run_command()
Footer
