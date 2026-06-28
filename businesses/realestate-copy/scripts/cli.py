# CLI — realestate_copy_cli.py

"""CLI for real estate copy intake, routing, delivery archive ops."""
from __future__ import annotations

import argparse
import sys

from automation_scheduler import create_client_folder, route_to_production


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="realestate_copy")
    sub = parser.add_subparsers(dest="cmd")

    p_intake = sub.add_parser("intake", help="Create client folder from intake")
    p_intake.add_argument("--name", required=True)
    p_intake.add_argument("--order-id")
    p_intake.add_argument("--tier", default="subscription")
    p_intake.add_argument("--voice", default="")
    p_intake.add_argument("--property-type", default="")

    p_route = sub.add_parser("route", help="Route existing order to production")
    p_route.add_argument("--order-id", required=True)

    args = parser.parse_args(argv)

    if args.cmd == "intake":
        path = create_client_folder(
            args.name,
            order_id=args.order_id,
            tier=args.tier,
            voice=args.voice,
            property_type=args.property_type,
        )
        print(path)
        return 0
    if args.cmd == "route":
        print(route_to_production(args.order_id))
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
