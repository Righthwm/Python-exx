def summary_dict(string_data):
    my_list = [{str(line.replace(": ", ":").replace(" message",", message").replace(" receiver",", receiver").replace(" sender",", sender").replace("_",":"))} for line in string_data.splitlines()]
    return my_list