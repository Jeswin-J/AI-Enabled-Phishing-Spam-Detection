import shutil
import json

def filter_and_save_domains(malicious_urls_file, blocked_domains_file, block_count_threshold=100000):
  """
  Filters domains from malicious_urls.json and saves them to blocked_domains.json.

  Args:
    malicious_urls_file: Path to the malicious URLs file.
    blocked_domains_file: Path to the file where filtered domains will be saved.
    block_count_threshold: Minimum block count for inclusion (default: 100000).
  """

  with open(malicious_urls_file, 'r') as f_in:
    data = json.load(f_in)

  filtered_domains = []
  for item in data:
    try:
      if item['block_count'] >= block_count_threshold:
        if isinstance(item['phishing_url'], str):  # Check if it's a string
          domain = item['phishing_url'].split("//")[1].split("/")[0]  # Extract domain
          filtered_domains.append({"domain": domain, "block_count": item['block_count']})
        else:
          print(f"Warning: 'phishing_url' is not a string: {item}")
    except (KeyError, IndexError) as e:
      print(f"Error processing item: {item}")

  with open(blocked_domains_file, 'w') as f_out:
    json.dump(filtered_domains, f_out, indent=4)

  # Copy the filtered data using shutil.copyfile
  try:
    shutil.copyfile(blocked_domains_file, blocked_domains_file + ".original")
    print(f"Filtered domains saved to: {blocked_domains_file}")
  except OSError as e:
    print(f"Error copying data: {e}")

# Example usage
malicious_urls_file = "malicious_urls.json"
blocked_domains_file = "filtered_domains.json"
filter_and_save_domains(malicious_urls_file, blocked_domains_file)
