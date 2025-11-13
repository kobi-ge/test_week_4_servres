import json

def load_data(file_name="endpoints_data.json"):
    with open(file_name, "r") as file:
        return json.load(file)

def save_data(data):
    with open("endpoints_data.json", "a") as file:
        data = json.dumps(data, indent=4)
        file.write(data)

def create_dict(current_url, current_method):
    new_dict = [{
            "url": current_url,
            "method": current_method,
            "stats": {
            "total_requests_received": 1,
            "avg_handling_time": 0
            }
        }]
    return new_dict


def update(current_url, current_method):
        file_data = load_data()
        dict_info = create_dict(current_url, current_method)
        if not file_data:
            save_data(dict_info)
            return {"state": "success"}
        for method in file_data:
            if method["url"] == current_url:
                file_data["total_requests_received"] += 1
                file_data["method"] = current_method
            else:
                file_data.append(dict_info)
        save_data(file_data)
        return {"state": "success"}

# def update_summary():
#     file_data = load_data("summary.json")
#     if not file_data:
