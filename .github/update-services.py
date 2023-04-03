from pathlib import Path
import sys

import yaml

sys.path.append(str(Path(__file__).parent.parent))

from custom_components.adaptive_lighting import const  # noqa: E402

services_filename = "custom_components/adaptive_lighting/services.yaml"
with open(services_filename) as f:
    services = yaml.safe_load(f)

for service_name, dct in services.items():
    _docs = {"set_manual_control": const.DOCS_MANUAL_CONTROL, "apply": const.DOCS_APPLY}
    alternative_docs = _docs.get(service_name, const.DOCS)
    for field_name, field in dct["fields"].items():
        description = alternative_docs.get(field_name, const.DOCS[field_name])
        field["description"] = description

with open(services_filename, "w") as f:
    yaml.dump(services, f, sort_keys=False, width=1000)
