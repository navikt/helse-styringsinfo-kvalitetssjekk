import os
from soda.scan import Scan
import json
import warnings

warnings.filterwarnings("ignore", message='Your application has authenticated using end user credentials', category=Warning)

for f in os.listdir("soda-checks"):
    s = Scan()
    s.add_configuration_yaml_file(file_path="soda-config/config.yaml")
    dataset = f.split(".")[0]
    s.set_data_source_name(dataset)
    s.add_sodacl_yaml_file(f"soda-checks/{f}")
    s.execute()

    # print(json.dumps(s.get_scan_results(), indent=4, sort_keys=True))

    scan_result = s.get_scan_results()

    messages = [log["message"] for log in scan_result["logs"]]

    print()
    print(f"===== Report for {dataset} =========")
    print()
    for message in messages:
        print(message)
    print()
    print(f"===== Report for {dataset} end =====")
    print()
