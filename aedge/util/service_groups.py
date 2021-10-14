from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "aedge_harvester aedge_timelord_launcher aedge_timelord aedge_farmer aedge_full_node aedge_wallet".split(),
    "node": "aedge_full_node".split(),
    "harvester": "aedge_harvester".split(),
    "farmer": "aedge_harvester aedge_farmer aedge_full_node aedge_wallet".split(),
    "farmer-no-wallet": "aedge_harvester aedge_farmer aedge_full_node".split(),
    "farmer-only": "aedge_farmer".split(),
    "timelord": "aedge_timelord_launcher aedge_timelord aedge_full_node".split(),
    "timelord-only": "aedge_timelord".split(),
    "timelord-launcher-only": "aedge_timelord_launcher".split(),
    "wallet": "aedge_wallet aedge_full_node".split(),
    "wallet-only": "aedge_wallet".split(),
    "introducer": "aedge_introducer".split(),
    "simulator": "aedge_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
