import os
import json
from soda.scan import Scan
from slack_sdk import WebClient

def run_scan(s: Scan, f: str, dir: str) -> list:
    dataset = f.split(".")[0]
    s.set_data_source_name(dataset)
    s.add_sodacl_yaml_file(f"{dir}/{f}")
    s.execute()
    return [e.get_dict() for e in s.get_checks_warn_or_fail()]

def post_slack_message(errors: list) -> None:
    slack_token = os.environ["SLACK_TOKEN"]
    slack_channel = os.environ["SLACK_CHANNEL"]
    client = WebClient(token=slack_token)
    client.chat_postMessage(channel=slack_channel if slack_channel.startswith("#") else "#"+slack_channel, text=json.dumps(errors))

if __name__ == "__main__":
    s = Scan()

    config_path = os.environ["SODA_CONFIG"]
    s.add_configuration_yaml_file(file_path=config_path)

    errors = []
    checks_path = os.environ["SODA_CHECKS_FOLDER"]
    for f in os.listdir(checks_path):
        errors_new = run_scan(s, f, checks_path)
        errors += errors_new

    if len(errors) > 0:
        post_slack_message(errors)
        print("errors", errors)