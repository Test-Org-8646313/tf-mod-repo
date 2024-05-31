def parse_json_data(data):
    try:
        print("---------Version 1-------\n")
        print(f"Organization: {data['organization']}")
        print(f"Total Employees: {data['employees']}\n")
        print("---------------------------")
    except Exception as error:
        print("Error Occurred: ",error)
