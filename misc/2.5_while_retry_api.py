max_api_calls = 5
api_calls = 0

while api_calls < max_api_calls:
    # Simulating an API call
    api_response = input("Did the API call succeed? (yes/no): ")

    if api_response.lower() in ("y", "yes"):
        print("API call was successful!")
        break
    else:
        print("API call failed. Retrying...")
        api_calls += 1
else:
    print("Failed to get a response from the API after multiple attempts.")
