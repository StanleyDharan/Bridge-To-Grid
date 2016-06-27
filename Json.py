class Json_Data():
#ACCEPTS A STRING
    def search_results_json(item, function, result):
        json_data = "[{\"function\": \""+ function +"\"}, {\"result\": \""+ str(result) +"\"}, "
        if(function == "find"):
            item = item.split(", \n")
            for item_type in item:
                json_data += "{\"item\": \"" + item_type + "\"}, "
            size = len(json_data) - 2
            json_data = json_data[:size] + json_data[size+2:]
            json_data += " ]"
        elif(function == "search"):
            json_data += "{\"item\": \"" + item + "\"}]"

        return json_data
