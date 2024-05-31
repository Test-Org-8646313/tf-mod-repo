def parse_json_data(data):
    try:
        print("---------Version 2-------\n")
        print(f"Organization Name: {data['organization']}")
        print(f"Total Employee Count: {data['employees']}\n")
        print("---------------------------")
    except Exception as error:
        print("Error Occurred: ",error)
